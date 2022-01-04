from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.views import APIView


class RegistrationView(APIView):
    pass


class ActivationView(APIView):
    pass


class LoginView(ObtainAuthToken):
    pass


class LogoutView(APIView):
    pass


# class ForgotPasswordView(APIView):
#     pass
#
#
# class ForgotPasswordCompleteView(APIView):
#    pass
