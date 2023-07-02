from rest_framework.permissions import BasePermission


class IsOwner(BasePermission):
    def has_permission(self, request, view):
        # her tetiklendiğinde çalışır, önceliklidir.
        # this has priority. this run every trigger.
        print("has_permission calisti")
        print(request.user.is_authenticated)
        print(request.user)
        return request.user and request.user.is_authenticated

    message = "You must be the owner of this object or superuser"

    def has_object_permission(self, request, view, obj):
        # sadece delete işlemi yapıldığında çalışır
        # this is called just in delete process
        print("has_object_permission calisti")
        return obj.user == request.user or request.user.is_superuser
