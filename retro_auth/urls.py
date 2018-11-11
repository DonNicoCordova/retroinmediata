from django.urls import path
from retro_auth import views

urlpatterns = [
    path('login/', views.auth_login, name="login"),
    path('logout/', views.auth_logout, name="auth_logout"),
]
