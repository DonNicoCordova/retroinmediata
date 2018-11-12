from django.shortcuts import render
from .models import*

# Create your views here.
def NOTIFICATION(request):
	lista = []
	lista_hilo = []
	TEMPLATE_NAME = "base.html"
	notificaciones = notification.objects.all()
	notificaciones_hilo =  ThreadFollower.objects.all()

	for x in notificaciones:
		print(x)
		if "franco" == str(x.user_ask.user):
			if x.status == True:
				lista.append(x)

	for y in notificaciones_hilo:
		if "Mahana23" == str(y.userprofile.user):
			lista_hilo.append(y)

#NO SE HACEN 2 USUARIOS, SE HACE UN USUARIO GENERAL UTILIZANDO EL REQUEST.USER PARA RECONOCER
#EL USUARIO QUE ESTA CONECTADO
#ESTA REGLA DEBE CUMPLIRSE PARA AMBOS, PARA THREAD FOLLOWER COMO PARA NOTIFICATION

#para thread, al momento de crear un post se debe levantar una notificacion

	cantidad = len(lista)
	cantidad2 = len(lista_hilo)
	return render(request,TEMPLATE_NAME,{"notificaciones":lista,"cantidad":cantidad,"lista_hilo":lista_hilo,"cantidad2":cantidad2})
