from django.urls import path
from employees.views import (
    EmployeeListCreateAPIView,
    EmployeeDeleteAPIView,
)

urlpatterns = [
    path("", EmployeeListCreateAPIView.as_view(), name="employee-list-create"),
    path("<int:pk>/", EmployeeDeleteAPIView.as_view(), name="employee-delete"),
]