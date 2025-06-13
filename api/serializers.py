from django.contrib.auth.models import User
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


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=6)

    class Meta:
        model = User
        fields = ("username", "email", "password")


    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data["username"],
            email=validated_data["email"],
            password=validated_data["password"]
        )
        return user