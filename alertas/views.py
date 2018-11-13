from django.shortcuts import render
from .models import*
from retro.models import PostFollower

# Create your views here.
def NOTIFICATION(request):
	lista = []
	lista_hilo = []
	lista_Seguimiento = []
	TEMPLATE_NAME = "base.html"
	notificaciones = notification.objects.all()
	notificaciones_hilo =  ThreadFollower.objects.all()
	Seguimiento = PostFollower.objects.all()
	estado = True
	hilo = ThreadFollower.objects.get(pk=1)

	if hilo.status == True:
		print("hilo.status")
		estado = "No Seguir"
	else:
		print("else")
		estado= "Seguir"


	if request.method == 'POST':

		datas =  ThreadFollower.objects.get(pk=1)

		if request.POST['status'] != "No Seguir":
			#"ESTATUS -> NO SEGUIR"
			datas.status = False
			datas.save()

		if request.POST['status'] !="Seguir"  :
			#"STATUS -> SEGUIR"
			datas.status = True
			datas.save()
			


	else:
		for a in Seguimiento:
			if str(request.user) == str(a.userprofile.user):
				if a.status == True:
					lista_Seguimiento.append(a)

		for x in notificaciones:
			if str(request.user) == str(x.user_ask.user):
				if x.status == True:
					lista.append(x)

		for y in notificaciones_hilo:
			if str(request.user) == str(y.userprofile.user):
				if x.status == True:
					lista_hilo.append(y)


	




#NO SE HACEN 2 USUARIOS, SE HACE UN USUARIO GENERAL UTILIZANDO EL REQUEST.USER PARA RECONOCER
#EL USUARIO QUE ESTA CONECTADO
#ESTA REGLA DEBE CUMPLIRSE PARA AMBOS, PARA THREAD FOLLOWER COMO PARA NOTIFICATION

#para thread, al momento de crear un post se debe levantar una notificacion

	cantidad = len(lista)
	cantidad2 = len(lista_hilo)
	return render(request,TEMPLATE_NAME,{"notificaciones":lista,"cantidad":cantidad,"lista_hilo":lista_hilo,"cantidad2":cantidad2,"Seguir":lista_Seguimiento,"hilo":estado})
