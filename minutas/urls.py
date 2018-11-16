from django.urls import path
from . import views

urlpatterns = [
    path('', views.minutas, name="minutas"),
    path('crear_minuta/', views.crear_minuta, name="crear_minuta"),
    path('edit_minuta/<int:pk>/', views.edit_minute, name="edit_minuta")
]