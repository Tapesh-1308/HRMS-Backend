from django.db import models
from django.core.validators import EmailValidator

class Employee(models.Model):
    employee_id = models.BigAutoField(primary_key=True)
    full_name = models.CharField(max_length=100)
    email = models.EmailField(
        unique=True,
        validators=[EmailValidator()]
    )
    department = models.CharField(max_length=100)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.full_name} ({self.employee_id})"