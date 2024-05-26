from rest_framework.permissions import BasePermission

class CustomPermission(BasePermission):
    message = 'Custom permission check failed.'

    def has_permission(self, request, view):
        # Ensure the user is authenticated
        if not request.user or not request.user.is_authenticated:
            return False

        # Add more complex permission logic here
        if request.user.is_admin:
            return True

        return False