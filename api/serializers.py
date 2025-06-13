from rest_framework import serializers

from api.models import Habit, HabitRecord


class HabitSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)

    # def get_user(self, obj):
    #     return obj.user.username

    class Meta:
        model = Habit
        fields = "__all__"

class HabitRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = HabitRecord
        fields = "__all__"