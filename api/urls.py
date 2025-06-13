from django.urls import path, include
from rest_framework import routers, permissions

from api.views import HabitViewSet, HabitRecordViewSet, RegisterView

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="Habit Tracker API",
      default_version='v1',
      description="Документация for Habit Tracker API",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="habit@habit.com"),
      license=openapi.License(name="BSD License"),
   ),
    public=True,
    permission_classes=(permissions.AllowAny,),
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
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]