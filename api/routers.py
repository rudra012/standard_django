# -*- coding: utf-8 -*-
"""
This urls.py is for all API related URLs.

URL Naming Pattern (lowercased & underscored)
<app_name>_<model_name> or
<app_name>_<specific_action>

For base name use:
<app_name>
"""

from rest_framework import routers

from api.users import user_api

api_router = routers.DefaultRouter(trailing_slash=False)

api_router.register(r'users', user_api.UserViewSet, base_name='api_users')

# urlpatterns = api_router.urls
