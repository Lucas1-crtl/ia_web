from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path("limpar/", views.limpar_chat, name="limpar_chat")
]

