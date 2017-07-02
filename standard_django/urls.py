"""standard_django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

from django.conf import settings
from django.conf.urls import url, include
from django.contrib import admin
from rest_framework_swagger.views import get_swagger_view

from api.routers import api_router

schema_view = get_swagger_view(title='Standard Django API')

urlpatterns = [
    url(r'^admin/', admin.site.urls),
]

urlpatterns += [
    url(r'front/', include('front_web.urls')),
    url(r'front-ajax/', include('front_web.urls')),

    # Rest API
    url(r'^api/', include(api_router.urls)),

]

if settings.DEBUG:
    urlpatterns += [
        # Swagger Doc
        url(r'^doc_swagger$', schema_view)
    ]
