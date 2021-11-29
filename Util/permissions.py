from rest_framework import permissions
# class SenderPermission is specifying permissions to Senders users only
class SenderPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        # return "True" for senders , "False" for else
        return bool(not request.user.is_anonymous and not request.user.is_customer )


# class IsAnonymousUser is specifying permissions to Anonymous and Admin users only
class IsAnonymousUser(permissions.BasePermission):
    def has_permission(self, request, view):
        # return "True" for anonymous and admin users , "False" for else
        return bool(request.user.is_anonymous or request.user.admin)
