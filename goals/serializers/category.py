from rest_framework import serializers
from goals.models.models import GoalCategory, BoardParticipant
from core.serializers import ProfileSerializer


class CategoryCreateSerializer(serializers.ModelSerializer):
	user = serializers.HiddenField(default=serializers.CurrentUserDefault())

	class Meta:
		model = GoalCategory
		read_only_fields = ("id", "created", "updated", "user")
		fields = "__all__"

	def validate_board(self, value):
		if value.is_deleted:
			raise serializers.ValidationError("not allowed in deleted board")

		user = value.participants.filter(user=self.context["request"].user).first()
		if not user:
			raise serializers.ValidationError("not owner or writer of the board")
		elif user.role not in [BoardParticipant.Role.owner, BoardParticipant.Role.writer]:
			raise serializers.ValidationError("not owner or writer of the board")

		return value


class CategorySerializer(serializers.ModelSerializer):
	user = ProfileSerializer(read_only=True)

	class Meta:
		model = GoalCategory
		fields = "__all__"
		read_only_fields = ("id", "created", "updated", "user", "board")
