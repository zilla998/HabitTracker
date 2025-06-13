from rest_framework import permissions
from rest_framework.viewsets import ModelViewSet

from api.models import Habit, HabitRecord
from api.serializers import HabitSerializer, HabitRecordSerializer


class HabitViewSet(ModelViewSet):
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class HabitRecordViewSet(ModelViewSet):
    queryset = HabitRecord.objects.all()
    serializer_class = HabitRecordSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return self.queryset.filter(habit__user=self.request.user)

    def perform_create(self, serializer):
        habit_record = serializer.save()

        if habit_record.done:
            habit = habit_record.habit
            habit.is_active = False
            habit.save()