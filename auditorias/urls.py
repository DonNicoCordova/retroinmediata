from django.urls import path
from . import views


urlpatterns = [
    # path('', views.index, name="index"),
    path('',views.coincidencia, name="coincidencia"),
    path('auditoria/',views.auditorias, name="auditorias"),
    #path('repetido/',views.repetido, name="repetido"),
]
