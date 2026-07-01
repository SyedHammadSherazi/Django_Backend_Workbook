from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Project 
from .models import Task
from .serializers import ProjectSerializer
from .serializers import TaskSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
def home(request):
 return HttpResponse("Hello Backend")
# class ProjectDetailAPIView(APIView):
#   def get(self,request):
#     projects=Project.objects.all()
#     serialzer=ProjectSerializer(projects, many=True)
#     return Response(serialzer.data)


# class ProjectListAPIView(APIView):

#     def get(self, request, id):
#         project = Project.objects.get(id=id)
#         serializer = ProjectSerializer(project)
#         return Response(serializer.data)
#     def put(self,request,id):
#        projects=Project.objects.get(id=id)
#        serialzer=ProjectSerializer(projects, data=request.data)
#        if serialzer.is_valid():
#           serialzer.save()
#           return Response(serialzer.data)
#        return Response(serialzer.errors)
class ProjectViewSet(ModelViewSet):

    queryset = Project.objects.all()

    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated]
   
class TaskViewSet(ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    @action(detail=True, methods=["patch"])
    def change_status(self, request, pk=None):

        task = self.get_object()

        task.status = request.data.get("status")

        task.save()

        return Response(
            {
                "message": "Task status updated successfully.",
                "status": task.status
            },
            status=status.HTTP_200_OK
        )
   