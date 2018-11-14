from django.urls import path
from . import views

urlpatterns = [
<<<<<<< HEAD
    path('', views.NOTIFICATION, name='NOTIFICATION'),
    path('viewNotifications/', views.viewNotifications, name='viewNotifications'),
=======
    # path('', views.index, name="index"),
    path('',views.alerta, name="alerta"),
>>>>>>> Scrum-4
]
