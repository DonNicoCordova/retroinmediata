from django.urls import path
from retro import views

urlpatterns = [
    path('', views.index, name="index"),
    path('Seccion/<int:pk>/', views.section_details, name="section_details"),
	path('question/', views.question, name="question"),
    path('forum/', views.forum, name="forum"),
]
