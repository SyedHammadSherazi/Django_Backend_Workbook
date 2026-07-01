from django.contrib.auth.models import User
from rest_framework import serializers
from .models import RoleBaseSystem, Company


class SignupSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ["username", "email", "password"]

        extra_kwargs = {
            "password": {
                "write_only": True
            }
        }

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class UserSerializer(serializers.ModelSerializer):

    company = serializers.CharField(
        source="rolebasesystem.company.name",
        read_only=True
    )

    role = serializers.CharField(
        source="rolebasesystem.role",
        read_only=True
    )

    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "email",
            "company",
            "role",
        ]


class UserCreateSerializer(serializers.ModelSerializer):

    company = serializers.PrimaryKeyRelatedField(
        queryset=Company.objects.all(),
        write_only=True
    )

    role = serializers.ChoiceField(
        choices=RoleBaseSystem.ROLE_CHOICES,
        write_only=True
    )

    class Meta:
        model = User
        fields = [
            "username",
            "email",
            "password",
            "company",
            "role",
        ]

        extra_kwargs = {
            "password": {
                "write_only": True
            }
        }

    def create(self, validated_data):

        company = validated_data.pop("company")
        role = validated_data.pop("role")

        user = User.objects.create_user(
            username=validated_data["username"],
            email=validated_data["email"],
            password=validated_data["password"],
        )

        RoleBaseSystem.objects.create(
            user=user,
            company=company,
            role=role
        )

        return user