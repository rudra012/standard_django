from django.contrib.auth import login, logout
from rest_framework import status, mixins
from rest_framework import viewsets
from rest_framework.authtoken.models import Token
from rest_framework.decorators import list_route
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from base import response
from users.models import User
from . import serializers


class UserViewSet \
            (
            # mixins.RetrieveModelMixin,
            mixins.ListModelMixin,
            viewsets.GenericViewSet,
            # mixins.UpdateModelMixin,
        ):
    """
    For get request return response will be all users details 
    """
    queryset = User.objects.filter(is_active=True)
    serializer_class = serializers.UserSerializer

    @list_route(methods=['post'])
    def register(self, request):
        """
        
        :param request: 
        :return: 
        """
        serializer = serializers.UserRegisterSerializer(data=self.request.data)
        serializer.is_valid(raise_exception=True)
        user_obj = serializer.save()

        user = serializers.UserSerializer(user_obj)
        response_json = {'user': user.data}
        user_token = ""
        try:
            user_token = Token.objects.get(user=user_obj).key
        except:
            pass
        if not user_token:
            user_token = Token.objects.create(user=user_obj).key

        response_json['user'].update({"token": user_token})

        return response.Created(response_json)
        # if user.is_active:
        # return response.Created({"success": "Account successfully created."})

    @list_route(methods=['post'])
    def login(self, request):
        """
        device_id : For  notification purpose (iOS and Android)
        
        :param request: 
        :return: 
        """
        serializer = serializers.UserLoginSerializer(data=self.request.data)
        serializer.is_valid(raise_exception=True)
        user_obj = serializer.validated_data.get("user")
        user = serializers.UserSerializer(user_obj, context={'request': self.request})
        response_json = {'user': user.data}
        user_token = ""
        try:
            user_token = Token.objects.get(user=user_obj).key
        except:
            pass
        if not user_token:
            user_token = Token.objects.create(user=user_obj).key

        response_json['user'].update({"token": user_token})
        login(request, user_obj)
        return Response(response_json)

    @list_route(methods=['get'], permission_classes=(IsAuthenticated,))
    def me(self, request):
        return response.Ok(serializers.UserSerializer(self.request.user, context={'request': self.request}).data)

    @list_route(methods=['post'], permission_classes=(IsAuthenticated,))
    def set_password(self, request):
        user = request.user
        serializer = serializers.ChangePasswordSerializer(data=request.data, context={'request': self.request})
        serializer.is_valid(raise_exception=True)
        user.set_password(serializer.data.get('password'))
        user.save()
        return Response({'status': 'password set'})

    @list_route(methods=['get'], permission_classes=(IsAuthenticated,))
    def logout(self, request):
        """
        Logout based on the token in the header for logged in user.
        """
        if request.user and request.user.is_authenticated():
            if request.user.device_id:
                request.user.device_id = None
                request.user.save()

            Token.objects.filter(user=request.user).delete()
            logout(request)

            return Response({'message': 'Successfully Logged out'}, status=status.HTTP_200_OK)
        else:
            return Response(status=401)
