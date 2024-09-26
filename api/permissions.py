from rest_framework.permissions import IsAuthenticated


class IsAuthorAndOwnerPermission(IsAuthenticated):

    def has_object_permission(self, request, view, obj):
        return (obj.user == request.user)
