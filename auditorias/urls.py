from django.urls import path
from . import views


urlpatterns = [
    path('', views.auditorias, name="auditorias"),
    path('editUmbral/', views.edit_Umbral, name="edit_Umbral"),
    path('is_teacher/', views.is_teacher, name='is_teacher'),
    path('auditorias_aut', views.auditorias_aut, name='auditorias_aut')
]