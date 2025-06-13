from django.urls import path, include
from rest_framework import routers

from api.views import HabitViewSet, HabitRecordViewSet, RegisterView

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

app_name="api"

router = routers.DefaultRouter()
router.register("habit", HabitViewSet)
router.register("habit_record", HabitRecordViewSet)



urlpatterns = [
    path('', include(router.urls)),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('auth/register/', RegisterView.as_view(), name="register"),
]