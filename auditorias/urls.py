from django.urls import path
from . import views


urlpatterns = [
    path('', views.auditorias, name="auditorias"),
]