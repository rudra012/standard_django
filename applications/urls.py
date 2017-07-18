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
from django.views.generic import TemplateView
from rest_framework_swagger.views import get_swagger_view

from api.v0_x.routers import api_router as api_router_0x

schema_view = get_swagger_view(title='Standard Django API')

urlpatterns = [
    url(r'^admin/', admin.site.urls),
]

urlpatterns += [
    url(r'front/', include('front_web.urls')),
    # url(r'front-ajax/', include('front_web.urls_ajax')),

    url(r'react001/', include('react001.urls')),
    # url(r'react001-ajax/', include('react001.urls_ajax')),

    # Angular1 First Web
    url(r'angular1-web001/', TemplateView.as_view(template_name='angular1001/index.html'), name="angular1001_home"),

    # Rest API
    url(r'^v0.1-dev/', include(api_router_0x.urls)),

]

if settings.DEBUG:
    urlpatterns += [
        # Swagger Doc
        url(r'^doc_swagger$', schema_view)
    ]
