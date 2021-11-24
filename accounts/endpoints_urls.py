from django.utils.translation import gettext_lazy as _
from rest_framework import mixins
from rest_framework import viewsets
from rest_framework.views import APIView
from Util.permissions import IsAnonymousUser


# this class is used to log the user out
class Logout(APIView):
    def post(self, request):

        from rest_framework_simplejwt.tokens import RefreshToken
        from rest_framework.response import Response
        from rest_framework import status
        try:
            refresh_token = request.data["refresh_token"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)


# this class is used to register new users
class RegisterUserViewSet(viewsets.GenericViewSet, mixins.CreateModelMixin):
    """
        API endpoint that allows to register new users
        this endpoint allows only POST function
        permissions to this view is restricted as the following:
        - anonymous users and system backend users (Admin and Staff )
         only can access this api to create an account
         Data will be submitted in the following format using POST function:
       {
        "id": 26,
        "full_name": "ali hassan hamid",
        "address": "Al-Khartoum,Sudan",
        "password":"password",
        "confirm_password":"confirm_password",
        "email": "ali@gmail.com",
        "phone_number": "922367654",
        }
      """
    from accounts.serializers import RegisterSerializer

    def get_view_name(self):
        return _("Register New User")

    from .models import User
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [IsAnonymousUser]
