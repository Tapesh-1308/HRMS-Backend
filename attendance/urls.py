from django.urls import path
from .views import (
    AttendanceCreateAPIView,
    AttendanceListAPIView,
)

urlpatterns = [
    path("", AttendanceListAPIView.as_view(), name="attendance-list"),
    path("mark/", AttendanceCreateAPIView.as_view(), name="attendance-create"),
]