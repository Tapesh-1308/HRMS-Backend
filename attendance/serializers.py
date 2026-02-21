from rest_framework import serializers
from .models import Attendance
from employees.models import Employee
from datetime import date


class AttendanceSerializer(serializers.ModelSerializer):

    employee_name = serializers.CharField(source="employee.full_name", read_only=True)
    employee_id = serializers.IntegerField()

    class Meta:
        model = Attendance
        fields = [
            "employee_id",
            "employee_name",
            "date",
            "status",
            "created_at",
        ]
        read_only_fields = ["employee_id", "created_at", "employee_name"]

    def validate_date(self, value):
        if value > date.today():
            raise serializers.ValidationError("Attendance date cannot be in the future.")
        return value

    def validate(self, attrs):
        employee_id = attrs.get("employee_id")
        attendance_date = attrs.get("date")

        try:
            employee = Employee.objects.get(employee_id=employee_id)
        except Employee.DoesNotExist:
            raise serializers.ValidationError(
                {"employee_id": "Employee with this ID does not exist."}
            )

        # Prevent duplicate attendance (extra safety)
        if Attendance.objects.filter(employee=employee, date=attendance_date).exists():
            raise serializers.ValidationError(
                "Attendance already marked for this employee on this date."
            )

        attrs["employee"] = employee
        return attrs

    def create(self, validated_data):
        validated_data.pop("employee_id")
        return Attendance.objects.create(**validated_data)
