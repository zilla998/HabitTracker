from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework_simplejwt.tokens import RefreshToken

from api.models import Habit, HabitRecord
from api.serializers import HabitSerializer, HabitRecordSerializer, RegisterSerializer


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



class RegisterView(APIView):
    def post(self, request):
        serializer =RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()

            refresh = RefreshToken.for_user(user)
            return Response({
                'message': 'Пользователь успешно зарегистрирован',
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            }, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)