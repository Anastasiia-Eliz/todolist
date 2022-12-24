from django.core.validators import MinLengthValidator
from django.db import models
from django.utils.crypto import get_random_string


class TgUser(models.Model):
	tg_user_id = models.BigIntegerField(unique=True)
	tg_chat_id = models.BigIntegerField()
	tg_username = models.CharField(max_length=32, validators=[MinLengthValidator(5)])
	verification_code = models.CharField(max_length=10, unique=True)
	user = models.ForeignKey('core.User', on_delete=models.CASCADE, null=True)

	def generate_verification_code(self) -> str:
		code = get_random_string(10)
		self.verification_code = code
		self.save()
		return code
