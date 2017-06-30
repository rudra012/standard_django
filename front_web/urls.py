from django.conf.urls import url

from front_web import views

urlpatterns = [
    url(r'^$', views.FrontHome.as_view(), name="front_home"),
]
