from rest_framework.permissions import BasePermission

class IsAuthenticatedAndOwner(BasePermission):
    def has_permission(self, request, view):
        # Only allow logged-in users to create an order
        return request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        # Only allow users to view their own orders
        return obj.user == request.user
