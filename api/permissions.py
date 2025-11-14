from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):

    def has_permission(self, request, view):
        # Allow read-only for everyone
        if request.method in permissions.SAFE_METHODS:
            return True
        
        # For create/update/delete require user to be authenticated
        return bool(request.user and request.user.is_authenticated)

    def has_object_permission(self, request, view, obj):
        # Read-only allowed for everyone
        if request.method in permissions.SAFE_METHODS:
            return True
        
        # Staff/admin can modify anything
        if request.user and request.user.is_staff:
            return True
        
        # Only the owner can update/delete the movie
        return obj.user == request.user