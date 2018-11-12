from django.urls import path
from . import views


urlpatterns = [
    # path('', views.index, name="index"),
    path('',views.auditorias, name="auditorias"),
    #path('repetido/',views.repetido, name="repetido"),
]
