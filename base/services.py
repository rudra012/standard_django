from rest_framework.authtoken.models import Token

from base.utils.custom_generate import generate_token


def get_user_token(user_obj):
    user_token = ""
    try:
        user_token = Token.objects.get(user=user_obj).key
    except:
        pass
    if not user_token:
        user_token = Token.objects.create(user=user_obj).key
    return user_token


def get_user_updated_token(user_obj):
    user_token = ""
    try:
        token_obj = Token.objects.get(user=user_obj)
        token_obj.key = generate_token()
        token_obj.save()
    except:
        pass
    if not user_token:
        user_token = Token.objects.create(user=user_obj).key
    return user_token


def get_user_by_token(user_token):
    """
    
    :param user_token: Login user token
    :return: 
    """
    user_obj = False
    try:
        user_obj = Token.objects.get(key=user_token).user
    except:
        pass
    return user_obj


def delete_user_token(user_obj):
    """
    To delete user token from db so user will logout from token authentication
    :param user_obj: User model object
    :return: 
    """
    Token.objects.filter(user=user_obj).delete()
