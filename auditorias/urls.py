from django.urls import path
from . import views


urlpatterns = [
    path('', views.auditorias, name="auditorias"),
    path('editUmbral/', views.edit_Umbral, name="edit_Umbral"),
    path('auditorias_aut/', views.auditorias_aut, name="auditorias_aut"),
]