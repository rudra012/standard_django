from django.conf.urls import url
from django.views.generic import TemplateView

from . import views

urlpatterns = [
    url(r'^$', views.Home.as_view(), name="react_home"),
    url(r'^jsx/$', TemplateView.as_view(template_name="react001/jsx.html")),
]
