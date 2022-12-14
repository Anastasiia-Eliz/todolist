from django.db import transaction
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import permissions, filters
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.pagination import LimitOffsetPagination
from goals.models import GoalCategory, GoalComment, Board
from goals.permissions import BoardPermissions, CategoryPermissions, CommentPermissions, GoalPermissions
from goals.serializers.board import BoardCreateSerializer, BoardSerializer, BoardListSerializer
from goals.serializers.category import CategoryCreateSerializer, CategorySerializer
from goals.filters import GoalDateFilter
from goals.models import Goal
from goals.serializers.comment import CommentSerializer, CommentCreateSerializer
from goals.serializers.goal import GoalCreateSerializer, GoalSerializer


class GoalCategoryCreateView(CreateAPIView):
	model = GoalCategory
	permission_classes = [permissions.IsAuthenticated]
	serializer_class = CategoryCreateSerializer


class GoalCategoryListView(ListAPIView):
	model = GoalCategory
	permission_classes = [CategoryPermissions]
	serializer_class = CategorySerializer
	pagination_class = LimitOffsetPagination
	filter_backends = [
		filters.OrderingFilter,
		filters.SearchFilter,
	]
	ordering_fields = ["title", "created"]
	ordering = ["title"]
	search_fields = ["title"]

	def get_queryset(self):
		return GoalCategory.objects.filter(
			user=self.request.user, is_deleted=False
		)


class GoalCategoryView(RetrieveUpdateDestroyAPIView):
	model = GoalCategory
	serializer_class = CategorySerializer
	permission_classes = [permissions.IsAuthenticated]

	def get_queryset(self):
		return GoalCategory.objects.filter(user=self.request.user, is_deleted=False)

	def perform_destroy(self, instance):
		instance.is_deleted = True
		instance.save()
		return instance


class GoalCreateView(CreateAPIView):
	model = Goal
	permission_classes = [permissions.IsAuthenticated]
	serializer_class = GoalCreateSerializer


class GoalListView(ListAPIView):
	model = Goal
	permission_classes = [permissions.IsAuthenticated]
	serializer_class = GoalSerializer
	pagination_class = LimitOffsetPagination
	filter_backends = [
		DjangoFilterBackend,
		filters.OrderingFilter,
		filters.SearchFilter,
	]
	filterset_class = GoalDateFilter
	ordering_fields = ["priority", "due_date"]
	ordering = ["priority", "due_date"]
	search_fields = ["title"]

	def get_queryset(self):
		return Goal.objects.filter(user=self.request.user)


class GoalView(RetrieveUpdateDestroyAPIView):
	model = Goal
	serializer_class = GoalSerializer
	permission_classes = [GoalPermissions]

	def get_queryset(self):
		return Goal.objects.filter(
			user=self.request.user
		)

	def perform_destroy(self, instance):
		instance.status = Goal.Status.archived
		instance.save()
		return instance


class CommentCreateView(CreateAPIView):
	model = GoalComment
	permission_classes = [permissions.IsAuthenticated]
	serializer_class = CommentCreateSerializer

	def perform_create(self, serializer: CommentCreateSerializer):
		serializer.save(goal_id=self.request.data['goal'])


class CommentListView(ListAPIView):
	model = GoalComment
	permission_classes = [permissions.IsAuthenticated]
	serializer_class = CommentSerializer
	pagination_class = LimitOffsetPagination
	filter_backends = [filters.OrderingFilter, DjangoFilterBackend]
	filterset_fields = ["goal"]
	ordering = ["-id"]

	def get_queryset(self):
		return GoalComment.objects.filter(
			user=self.request.user
		)


class CommentView(RetrieveUpdateDestroyAPIView):
	model = GoalComment
	serializer_class = CommentSerializer
	permission_classes = [CommentPermissions]

	def get_queryset(self):
		return GoalComment.objects.filter(
			user=self.request.user
		)


class BoardCreateView(CreateAPIView):
	model = Board
	permission_classes = [permissions.IsAuthenticated]
	serializer_class = BoardCreateSerializer


class BoardView(RetrieveUpdateDestroyAPIView):
	model = Board
	permission_classes = [permissions.IsAuthenticated, BoardPermissions]
	serializer_class = BoardSerializer

	def get_queryset(self):
		return Board.objects.filter(participants__user=self.request.user, is_deleted=False)

	def perform_destroy(self, instance: Board):
		with transaction.atomic():
			instance.is_deleted = True
			instance.save()
			instance.categories.update(is_deleted=True)
			Goal.objects.filter(category__board=instance).update(
				status=Goal.Status.archived
			)
		return instance


class BoardListView(ListAPIView):
	model = Board
	permission_classes = [permissions.IsAuthenticated]
	pagination_class = LimitOffsetPagination
	serializer_class = BoardListSerializer
	filter_backends = [
		filters.OrderingFilter,
	]
	ordering = ["title"]

	def get_queryset(self):
		return Board.objects.filter(participants__user=self.request.user, is_deleted=False)
