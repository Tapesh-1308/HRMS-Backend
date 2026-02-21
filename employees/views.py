from rest_framework import generics, status
from rest_framework.response import Response
from django.db import IntegrityError
from employees.models import Employee
from employees.serializers import EmployeeSerializer


class EmployeeListCreateAPIView(generics.ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        try:
            self.perform_create(serializer)
        except IntegrityError:
            return Response(
                {
                    "success": False,
                    "message": "Employee with this email already exists."
                },
                status=status.HTTP_400_BAD_REQUEST
            )

        return Response(
            {
                "success": True,
                "data": serializer.data,
                "message": "Employee created successfully."
            },
            status=status.HTTP_201_CREATED
        )


class EmployeeDeleteAPIView(generics.DestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)

        return Response(
            {
                "success": True,
                "message": "Employee deleted successfully."
            },
            status=status.HTTP_200_OK
        )