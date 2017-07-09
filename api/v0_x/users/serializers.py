from django.contrib.auth import authenticate
from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.exceptions import NotFound

from applications.users.models import User


class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('first_name', 'last_name', 'email', 'password')
        write_only_fields = ('password',)

    def create(self, validated_data):
        print(validated_data)
        user = User.objects.create_user(**validated_data)
        return user


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email', 'first_name', 'last_name')
        read_only_fields = ('id', 'email')


class ChangePasswordSerializer(serializers.Serializer):
    password = serializers.CharField(required=True)
    confirm_password = serializers.CharField(required=True)

    class Meta:
        fields = ('password', 'confirm_password')

    def validate(self, attrs):
        request = self.context.get('request')
        user = authenticate(email=request.user.email, password=attrs.get("password"))
        if not user:
            raise NotFound('Old password incorrect!')
        return attrs


class UserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(required=True)

    class Meta:
        fields = ('email', 'password')

    def validate(self, attrs):
        # print(attrs)
        user = authenticate(email=attrs.get("email"), password=attrs.get("password"))
        if not user:
            raise NotFound('Email or password incorrect!')
        attrs["user"] = user
        return attrs
