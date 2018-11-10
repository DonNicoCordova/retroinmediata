from django.urls import path
from retro import views

urlpatterns = [
    path('', views.index, name="index"),
    path('Seccion/<int:pk>/', views.section_details, name="section_details"),
    path('editPost/<int:pk>/', views.edit_Post, name="edit_Post"),
    path('editComment/<int:pk>/', views.edit_Comment, name="edit_Comment"),
]
