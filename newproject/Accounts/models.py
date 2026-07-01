from django.db import models
from django.contrib.auth.models import User

class Company(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class RoleBaseSystem(models.Model):

    ROLE_CHOICES = [
        ("Admin", "Admin"),
        ("Manager", "Manager"),
        ("Employee", "Employee"),
    ]

    role = models.CharField(
        max_length=20,
        choices=ROLE_CHOICES,
        default="Employee"
    )

    company = models.ForeignKey(
        Company,
        on_delete=models.CASCADE,
       
    )

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        
    )

    def __str__(self):
        return f"{self.user.username} - {self.role} - {self.company.name}"