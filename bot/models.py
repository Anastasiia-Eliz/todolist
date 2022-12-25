import string
import random

from django.db import models
from core.models import User


class TgUser(models.Model):
	tg_user_id = models.BigIntegerField(unique=True)
	tg_chat_id = models.BigIntegerField()
	tg_username = models.CharField(max_length=32, null=True, blank=True, default=None)
	verification_code = models.CharField(max_length=10, unique=True)
	user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

	def set_verification_code(self):
		length = 10
		digits = string.digits
		v_code = ''.join(random.sample(digits, length))
		self.verification_code = v_code

	class Meta:
		verbose_name = 'TG User'
		verbose_name_plural = 'TG Users'
