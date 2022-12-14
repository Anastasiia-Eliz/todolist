from rest_framework import serializers

from core.serializers import ProfileSerializer
from goals.models import GoalComment, BoardParticipant


class CommentCreateSerializer(serializers.ModelSerializer):
	user = serializers.HiddenField(default=serializers.CurrentUserDefault())

	class Meta:
		model = GoalComment
		read_only_fields = ('id', 'user', 'created', 'updated', 'goal')
		fields = '__all__'

	def validate(self, attrs):
		roll = BoardParticipant.objects.filter(
			user=attrs.get('user'),
			board=attrs.get('board'),
			role__in=[BoardParticipant.Role.owner, BoardParticipant.Role.writer],
		).exists()
		if roll:
			return attrs
		raise serializers.ValidationError('You do not have permission to perform this action')

class CommentSerializer(serializers.ModelSerializer):
	user = ProfileSerializer(read_only=True)

	class Meta:
		model = GoalComment
		read_only_fields = ('id', 'user', 'created', 'updated', 'goal')
		fields = '__all__'
