"""
URL configuration for newproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from newapp import views
# from newapp.views import ProjectListAPIView
# from newapp.views import ProjectDetailAPIView
from newapp.views import ProjectViewSet
from rest_framework.routers import DefaultRouter
from newapp.views import TaskViewSet
router = DefaultRouter()

# ViewSet register karo
router.register("projects", ProjectViewSet, basename="projects")
router.register("tasks",TaskViewSet,basename="tasks")
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home),
    # path("projects/",ProjectDetailAPIView.as_view(),
    #      name="projects"),
    # path("projects/<int:id>/", ProjectListAPIView.as_view(), name="project-detail")
     path("", include(router.urls)),
]
