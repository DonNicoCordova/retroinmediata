from django.shortcuts import render
from .models import *


# Create your views here.
def NOTIFICATION(request):
    lista = []
    lista_hilo = []
    TEMPLATE_NAME = "base.html"
    print(request.user)
    notificaciones = notification.objects.filter(status=True, user_ask=request.user.userprofile)
    notificaciones_hilo = ThreadFollower.objects.filter(userprofile=request.user.userprofile)

    for x in notificaciones:
        lista.append(x)

    for y in notificaciones_hilo:
        lista_hilo.append(y)

    # NO SE HACEN 2 USUARIOS, SE HACE UN USUARIO GENERAL UTILIZANDO EL REQUEST.USER PARA RECONOCER
    # EL USUARIO QUE ESTA CONECTADO
    # ESTA REGLA DEBE CUMPLIRSE PARA AMBOS, PARA THREAD FOLLOWER COMO PARA NOTIFICATION

    # para thread, al momento de crear un post se debe levantar una notificacion

    cantidad = len(lista)
    cantidad2 = len(lista_hilo)
    return render(request, TEMPLATE_NAME,
                  {"notificaciones": lista, "cantidad": cantidad, "lista_hilo": lista_hilo, "cantidad2": cantidad2})
