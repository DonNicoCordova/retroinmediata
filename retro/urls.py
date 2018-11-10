from django.urls import path
from retro import views

urlpatterns = [
    path('', views.index, name="index"),
    path('Seccion/<int:pk>/', views.section_details, name="section_details"),
    path('delete_post/<int:id>/', views.delete_post, name="delete_post"),
]