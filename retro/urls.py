from django.urls import path
from retro import views

urlpatterns = [
    path('', views.index, name="index"),
    path('Seccion/<int:pk>/', views.section_details, name="section_details"),
    path('Post', views.post, name="post")
]
