from django.urls import path
from . import views

urlpatterns = [
    path('crear_minuta/', views.crear_minuta, name="crear_minuta"),
]