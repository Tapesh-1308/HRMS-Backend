from rest_framework import serializers
from employees.models import Employee


class EmployeeSerializer(serializers.ModelSerializer):
    total_present_days = serializers.SerializerMethodField()

    class Meta:
        model = Employee
        fields = [
            "employee_id",
            "full_name",
            "email",
            "department",
            "created_at",
            "total_present_days"
        ]
        read_only_fields = ["employee_id", "created_at", "total_present_days"]

    def get_total_present_days(self, obj):
        return obj.attendances.filter(status='Present').count()

    def validate_full_name(self, value):
        if not value.strip():
            raise serializers.ValidationError("Full name cannot be empty.")
        return value

    def validate_department(self, value):
        if not value.strip():
            raise serializers.ValidationError("Department cannot be empty.")
        return value