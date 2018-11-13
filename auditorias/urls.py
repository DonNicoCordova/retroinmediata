from django.urls import path
from . import views

urlpatterns = [
    # path('', views.index, name="index"),
    path('',views.auditorias, name="auditorias"),
    path('buscar_auditorias/',views.buscar_auditorias, name="buscar_auditorias"),
    path('historial_auditorias/',views.historial_auditorias, name="historial_auditorias"),
    #path('repetido/',views.repetido, name="repetido"),
]
