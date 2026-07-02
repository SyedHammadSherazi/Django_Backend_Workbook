from rest_framework.permissions import BasePermission

class IsAdminRole(BasePermission):

    def has_permission(self, request, view):

        if not request.user.is_authenticated:
            return False

        # Django Superuser ko allow karo
        if request.user.is_superuser:
            return True

        # Role based Admin ko allow karo
        if hasattr(request.user, "rolebasesystem"):
            return request.user.rolebasesystem.role == "Admin"

        return False