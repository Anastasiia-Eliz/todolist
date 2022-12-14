from django.contrib.auth import authenticate
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from rest_framework.exceptions import AuthenticationFailed

from .models import User


class SignUpSerializer(serializers.ModelSerializer):
	id = serializers.IntegerField(required=False)
	username = serializers.CharField(required=True, max_length=50)
	first_name = serializers.CharField(required=False, allow_blank=True, max_length=50)
	last_name = serializers.CharField(required=False, allow_blank=True, max_length=50)
	email = serializers.EmailField(required=False, allow_blank=True)
	password = serializers.CharField(required=True)

	def is_valid(self, raise_exception=False):
		"""Get password_repeat and remove from initial data"""
		self._password_repeat = self.initial_data.pop('password_repeat')
		return super().is_valid(raise_exception=raise_exception)

	def validate_username(self, value):
		"""Ensure username doesn't exist"""
		if self.Meta.model.objects.filter(username=value).exists():
			raise serializers.ValidationError(['User with such username already exists'])
		return value

	def validate_password(self, value):
		"""Ensure password is valid"""
		validate_password(value)
		return value

	def validate(self, data):
		"""Ensure passwords match"""
		print(data.get('password'))
		print(self._password_repeat)
		if data.get('password') != self._password_repeat:
			raise serializers.ValidationError({'password_repeat': ['Passwords must match']})
		return data

	def create(self, validated_data):
		"""Create user"""
		user = User.objects.create(**validated_data)
		user.set_password(user.password)
		user.save()
		return user

	class Meta:
		model = User
		fields = ['id', 'username', 'first_name', 'last_name', 'email', 'password']


class LoginSerializer(serializers.ModelSerializer):
	username = serializers.CharField(required=True)
	password = serializers.CharField(required=True, write_only=True)

	def create(self, validated_data):
		user = authenticate(
			username=validated_data['username'],
			password=validated_data['password'],
		)
		if not user:
			raise AuthenticationFailed
		return user

	class Meta:
		model = User
		fields = ['id', 'username', 'first_name', 'last_name', 'email', 'password']


class ProfileSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ['id', 'username', 'first_name', 'last_name', 'email']


class PasswordUpdateSerializer(serializers.Serializer):
	user = serializers.HiddenField(default=serializers.CurrentUserDefault())
	old_password = serializers.CharField(required=True)
	new_password = serializers.CharField(required=True)

	def validate_new_password(self, value):
		validate_password(value)
		return value
