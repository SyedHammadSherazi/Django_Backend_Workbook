from django.db import models

# Create your models here.
class Project(models.Model):
    name=models.CharField(max_length=50)
    description=models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name

class Task(models.Model):
    title=models.CharField(max_length=100)
    description=models.TextField()
    STATUS_CHOICES = [
    ("pending", "Pending"),
    ("in-progress", "In Progress"),
    ("completed", "Completed"),
]

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="pending"
    )
    due_date=models.DateField()
    added_by=models.ForeignKey(Project,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title