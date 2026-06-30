from django.contrib import admin
from .models import Project, Task


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "description", "start_date", "end_date")
    list_per_page = 1
    search_fields = ("name",)
    list_editable = ("name",)
@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "status", "due_date", "added_by")
   