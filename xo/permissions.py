from rest_framework.permissions import BasePermission


class IsAuthed(BasePermission):
    def has_permission(self, request, view):
        return hasattr(request, 'user_id') and request.user_id != -1