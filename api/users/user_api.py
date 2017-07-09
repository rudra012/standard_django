from django.contrib.auth import login, logout
from rest_framework import status, mixins
from rest_framework import viewsets
from rest_framework.decorators import list_route
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from applications.users.models import User
from base import response
from base.services import get_user_token, delete_user_token, get_user_updated_token
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
        user_token = get_user_token(user_obj)

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
        user_token = get_user_updated_token(user_obj)

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

            # To remove token login
            delete_user_token(request.user)
            # To flush session login
            logout(request)

            return Response(
                {'message': 'Successfully Logged out'},
                status=status.HTTP_200_OK
            )
        else:
            return Response(status=401)
