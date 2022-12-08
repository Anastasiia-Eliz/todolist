from rest_framework import serializers

from core.serializers import ProfileSerializer
from goals.models import GoalCategory, GoalComment, Goal


class GoalCreateSerializer(serializers.ModelSerializer):
	user = serializers.HiddenField(default=serializers.CurrentUserDefault())

	class Meta:
		model = GoalCategory
		read_only_fields = ("id", "created", "updated", "user")
		fields = "__all__"


class GoalSerializer(serializers.ModelSerializer):
	user = ProfileSerializer(read_only=True)

	class Meta:
		model = Goal
		read_only_fields = ("id", "created", "updated", "user")
		fields = "__all__"


class CategoryCreateSerializer(serializers.ModelSerializer):
	user = serializers.HiddenField(default=serializers.CurrentUserDefault())

	class Meta:
		model = GoalCategory
		read_only_fields = ("id", "created", "updated", "user")
		fields = "__all__"


class CategorySerializer(serializers.ModelSerializer):
	user = ProfileSerializer(read_only=True)

	class Meta:
		model = GoalCategory
		fields = "__all__"
		read_only_fields = ("id", "created", "updated", "user")

	def validate_category(self, value):
		if value.is_deleted:
			raise serializers.ValidationError('not allowed in deleted category')
		if value.user != self.context['request'].user:
			raise serializers.ValidationError('not owner of category')

		return value


class CommentCreateSerializer(serializers.ModelSerializer):
	user = serializers.HiddenField(default=serializers.CurrentUserDefault())

	class Meta:
		model = GoalComment
		read_only_fields = ('id', 'user', 'created', 'updated', 'goal')
		fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
	user = ProfileSerializer(read_only=True)

	class Meta:
		model = GoalComment
		read_only_fields = ('id', 'user', 'created', 'updated', 'goal')
		fields = '__all__'
