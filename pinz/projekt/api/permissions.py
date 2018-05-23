from rest_framework.permissions import BasePermission

class IsAdminOrCurrUser(BasePermission):
    """
    Object-level permission to only allow owners of an object to edit it.
    Assumes the model instance has an `owner` attribute.
    """

    def has_object_permission(self, request, view, obj):

        #
        return obj.id == request.user.id or (request.user and request.user.is_staff)
