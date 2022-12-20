from rest_framework import serializers

from core.serializers import ProfileSerializer
from goals.models.models import Goal, BoardParticipant


class GoalCreateSerializer(serializers.ModelSerializer):
	user = serializers.HiddenField(default=serializers.CurrentUserDefault())

	class Meta:
		model = Goal
		read_only_fields = ("id", "created", "updated", "user")
		fields = "__all__"

	def validate_category(self, value):
		if value.is_deleted:
			raise serializers.ValidationError("not allowed in deleted category")

		user = value.board.participants.filter(user=self.context["request"].user).first()
		if not user:
			raise serializers.ValidationError("not owner or writer in the related board")
		elif user.role not in [BoardParticipant.Role.owner, BoardParticipant.Role.writer]:
			raise serializers.ValidationError("not owner or writer in the related board")

		return value

class GoalSerializer(serializers.ModelSerializer):
	user = ProfileSerializer(read_only=True)

	class Meta:
		model = Goal
		read_only_fields = ("id", "created", "updated", "user")
		fields = "__all__"

