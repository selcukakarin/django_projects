from rest_framework.permissions import BasePermission


class IsOwner(BasePermission):
    # has_permission sayfaya girerken çalışır
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated
    message = "You must be the owner of this object."

    # has_object_permission silme işlemi tetiklendiğinde çalışır
    def has_object_permission(self, request, view, obj):
        print("has_obj_perm çalıştı")
        return (obj.user == request.user) or request.user.is_superuser
