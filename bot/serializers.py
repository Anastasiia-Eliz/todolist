from rest_framework import serializers

from .models import TgUser


class TgUserUpdateSerializer(serializers.ModelSerializer):

	class Meta:
		model = TgUser
		fields = ('verification_code')
