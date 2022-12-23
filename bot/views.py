from rest_framework import permissions, status
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from todolist.settings import TG_TOKEN
from .models import TgUser
from .serializers import TgUserUpdateSerializer
from .tg import TgClient


class TgUserUpdateView(GenericAPIView):
	model = TgUser
	permission_classes = [permissions.IsAuthenticated]
	http_method_names = ['patch']
	serializer_class = TgUserUpdateSerializer

	def patch(self, request, *args, **kwargs):
		data = self.serializer_class(request.data).data
		tg_client = TgClient(TG_TOKEN)
		tg_user = TgUser.objects.filter(verification_code=data['verification_code']).first()
		if not tg_user:
			return Response(status=status.HTTP_400_BAD_REQUEST)
		tg_user.user = request.user
		tg_user.save()
		tg_client.send_message(chat_id=tg_user.tg_chat_id, text='Успешно')
		return Response(data=data, status=status.HTTP_201_CREATED)
