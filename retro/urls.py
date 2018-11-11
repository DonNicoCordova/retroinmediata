from django.urls import path
from retro import views

urlpatterns = [
    path('', views.index, name="index"),
    path('Seccion/<int:pk>/', views.section_details, name="section_details"),
    path('Post', views.post, name="post"),
	path('question/', views.question, name="question"),
    path('forum/', views.forum, name="forum"),
    path('comment_post/', views.comment_post, name="comment_post"),
    path('delete_post/', views.delete_post, name="delete_post"),
    path('delete_comment/', views.delete_comment, name="delete_comment"),
]
