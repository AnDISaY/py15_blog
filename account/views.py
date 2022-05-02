from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import RegistrationSerializer, ActivationSerializer, LoginSerializer


class RegistrationView(APIView):
    def post(self, request):
        data = request.data
        serializer = RegistrationSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.create()
        return Response('Вы успешно зарегистрировались. Вам отправлено смс с подтверждением')


class ActivationView(APIView):
    def post(self, request):
        data = request.data
        serializer = ActivationSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.activate()
        return Response('Ваш аккаунт активирован')


class LoginView(ObtainAuthToken):
    serializer_class = LoginSerializer


class LogoutView(APIView):
    pass


# class ForgotPasswordView(APIView):
#     pass
#
#
# class ForgotPasswordCompleteView(APIView):
#    pass
