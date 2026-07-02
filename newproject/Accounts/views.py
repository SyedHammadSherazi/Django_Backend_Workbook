from django.contrib.auth.models import User
from django.contrib.auth import authenticate

from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

from .serializers import (
    SignupSerializer,
    UserSerializer,
    UserCreateSerializer,
)

from .permissions import IsAdminRole


class SignupView(APIView):
    permission_classes = []

    def post(self, request):
        serializer = SignupSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(
                {"message": "User created successfully."},
                status=status.HTTP_201_CREATED,
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST,
        )


class LoginView(APIView):
    permission_classes = []

    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")

        user = authenticate(
            username=username,
            password=password,
        )

        if user is not None:
            return Response(
                {"message": "Login successful"},
                status=status.HTTP_200_OK,
            )

        return Response(
            {"error": "Invalid username or password"},
            status=status.HTTP_401_UNAUTHORIZED,
        )


class UserListView(generics.ListCreateAPIView):

    queryset = User.objects.all()

    def get_permissions(self):

        # GET -> sab authenticated users
        if self.request.method == "GET":
            return [IsAuthenticated()]

        # POST -> sirf Superuser ya Role Admin
        return [IsAuthenticated(), IsAdminRole()]

    def get_serializer_class(self):
        if self.request.method == "POST":
            return UserCreateSerializer
        return UserSerializer


class UserDeleteView(generics.DestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated, IsAdminRole]