from rest_framework import serializers
from .models import Project, Task


class ProjectSerializer(serializers.ModelSerializer):
    name = serializers.CharField(
        error_messages={
            "blank": "Project name cannot be empty."
        }
    )
    class Meta:
        model = Project
        fields = "__all__"

    


class TaskSerializer(serializers.ModelSerializer):
    title = serializers.CharField(
        error_messages={
            "blank": "Task name cannot be empty."
        }
    )

    class Meta:
        model = Task
        fields = "__all__"

   