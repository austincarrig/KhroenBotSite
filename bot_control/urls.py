from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^', views.BotControl.as_view(), name='control'),
    url(r'^commands/', views.BotCommands.as_view(), name='commands'),
]