from django.db import models

# Create your models here.
class Project(models.Model):
    name=models.CharField(max_length=50)
    description=models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()

class Task(models.Model):
    title=models.CharField(max_length=100)
    description=models.TextField()
    status=models.CharField(max_length=30)
    due_date=models.DateField()
    added_by=models.ForeignKey(Project,on_delete=models.CASCADE)