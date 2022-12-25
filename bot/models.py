import string
from random import random

from django.core.validators import MinLengthValidator
from django.db import models
from django.utils.crypto import get_random_string


class TgUser(models.Model):
	tg_user_id = models.BigIntegerField(unique=True)
	tg_chat_id = models.BigIntegerField()
	tg_username = models.CharField(max_length=32, validators=[MinLengthValidator(5)])
	verification_code = models.CharField(max_length=10, unique=True)
	user = models.ForeignKey('core.User', on_delete=models.CASCADE, null=True)

	def set_verification_code(self) -> None:
		length = 10  # Длина кода подтверждения
		digits = string.digits
		v_code = ''.join(random.sample(digits, length))
		self.verification_code = v_code

	class Meta:
		verbose_name = 'TG User'
		verbose_name_plural = 'TG Users'
