from django.contrib import admin
from .models import Company, RoleBaseSystem
# Register your models here.

@admin.register(Company)
class Company_Record(admin.ModelAdmin):
    list_display=(
       "id","name","address"
    )

@admin.register(RoleBaseSystem)
class Profile_record(admin.ModelAdmin):
    list_display=(
        "id","role","company"
    )
    search_fields=("name","id")