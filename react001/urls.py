from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.Home.as_view(), name="react_home"),
    url(r'^jsx', views.JSX.as_view(), name="react_jsx"),
]
