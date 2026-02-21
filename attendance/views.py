from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.db.models import Count, Q
from .models import Attendance
from .serializers import AttendanceSerializer
from employees.models import Employee


class AttendanceCreateAPIView(generics.CreateAPIView):
    serializer_class = AttendanceSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        return Response(
            {
                "success": True,
                "data": serializer.data,
                "message": "Attendance marked successfully.",
            },
            status=status.HTTP_201_CREATED,
        )


class AttendanceListAPIView(generics.ListAPIView):
    serializer_class = AttendanceSerializer

    def get_queryset(self):
        queryset = Attendance.objects.select_related("employee").all()

        employee_id = self.request.query_params.get("employee_id")
        date = self.request.query_params.get("date")

        if employee_id:
            queryset = queryset.filter(employee__employee_id=employee_id)

        if date:
            queryset = queryset.filter(date=date)

        return queryset.order_by("-date")
