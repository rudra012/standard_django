from django.conf.urls import url

from front_web import views

urlpatterns = [
    url(r'^$', views.FrontHome.as_view(), name="front_home"),
    url(r'^celery-mail$', views.CeleryMail.as_view(), name="celery_mail"),
    url(r'^celery-mass-mail$', views.CeleryMassMail.as_view(), name="celery_mass_mail"),
]
