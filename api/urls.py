from django.urls import path, include
from rest_framework import routers

from api.views import HabitViewSet, HabitRecordViewSet

app_name="api"

router = routers.DefaultRouter()
router.register("habit", HabitViewSet)
router.register("habit_record", HabitRecordViewSet)



urlpatterns = [
    path('', include(router.urls))
]