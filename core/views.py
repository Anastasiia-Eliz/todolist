from django.contrib.auth import authenticate, login, logout
from rest_framework import status, generics
from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView, UpdateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import User
from .serializers import SignUpSerializer, ProfileSerializer, PasswordUpdateSerializer, LoginSerializer


class SignUpView(CreateAPIView):
	"""Create new user"""
	queryset = User.objects.all()
	serializer_class = SignUpSerializer


class LoginView(generics.GenericAPIView):
	"""Login user"""
	serializer_class = LoginSerializer

	def post(self, request, *args, **kwargs):
		serializer = self.get_serializer(data=request.data)
		serializer.is_valid(raise_exception=True)
		user = serializer.save()
		login(request=request, user=user)
		return Response(serializer.data)


class ProfileView(generics.RetrieveUpdateDestroyAPIView):
	queryset = User.objects.all()
	serializer_class = ProfileSerializer
	permission_classes = [IsAuthenticated]

	def get_object(self):
		return self.request.user

	def delete(self, request, *args, **kwargs):
		logout(request)
		return Response(status=status.HTTP_200_OK)


class PasswordUpdateView(UpdateAPIView):
	serializer_class = PasswordUpdateSerializer
	model = User
	permission_classes = [IsAuthenticated]

	def get_object(self):
		return self.request.user

	def update(self, request, *args, **kwargs):
		self.object = self.get_object()
		serializer = self.get_serializer(data=request.data)

		if serializer.is_valid():
			if not self.object.check_password(serializer.data.get('old_password')):
				return Response({"old_password": ["Wrong password passed, try again."]},
				                status=status.HTTP_400_BAD_REQUEST)
			self.object.set_password(serializer.data.get('new_password'))
			self.object.save()
			return Response(status=status.HTTP_204_NO_CONTENT)

		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
