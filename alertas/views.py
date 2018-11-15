from alertas.forms import *
from retro_auth.models  import *
from retro.models import *
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from retro_auth.models import UserProfile
from django.contrib import messages
from django.shortcuts import render
from .models import*
from django.http import JsonResponse


# Create your views here.
def NOTIFICATION(request):

	countPost = 0 #Contador de post  no vistos
	countThreads = 0 #Contador  de Threads no vistos
	TEMPLATE_NAME = "base.html" #Template  en la cual enviaremos los datos al final de la funcion

	connected_user = UserProfile.objects.get(user = request.user) #Traemos la lista de usuario que hay en la BDD
	notificaciones = notification.objects.filter(user_ask = connected_user) #Traemos las notificaciones correspondientes al usuario conectado
	notificaciones_hilo =  ThreadFollower.objects.filter(userprofile = connected_user) #Traemos los hilos correspondientes al usuario conectado
	follow_post = PostFollower.objects.filter(userprofile = connected_user) #Traemos los post a los cuales se sigue correspondientes al usuario conectado
	estado = True

	for hilo in notificaciones_hilo:
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
		for x in notificaciones: #Recorremos la lista de notificaciones que se  obtuvieron
			if x.status == True: #Comprobamos si estan "disponibles", True = no se han visto, False = ya fueron vistas
				countPost += 1

		for y in notificaciones_hilo: #Recorremos la lista de notificaciones que se  obtuvieron
			if y.status == True: #Comprobamos si estan "disponibles", True = no se han visto, False = ya fueron vistas
				countThreads += 1

		return render(request,TEMPLATE_NAME,{"notificaciones":notificaciones,"countPost":countPost,"lista_hilo":notificaciones_hilo,"countThreads":countThreads})


def viewNotifications(request):
	response = {}

	pks = request.POST.getlist('info[]', False)

	for pk in pks:
		notifications = notification.objects.get(pk = int(pk))
		notifications.status = False
		
		notifications.save()

	return JsonResponse(response)

#NO SE HACEN 2 USUARIOS, SE HACE UN USUARIO GENERAL UTILIZANDO EL REQUEST.USER PARA RECONOCER
#EL USUARIO QUE ESTA CONECTADO
#ESTA REGLA DEBE CUMPLIRSE PARA AMBOS, PARA THREAD FOLLOWER COMO PARA NOTIFICATION

#para thread, al momento de crear un post se debe levantar una notificacion
#UTILIZAR AJAX PARA CUANDO SE OMENTE AGREGAR UNA NOTIFICACION EN ESTADO TRUE


# Create your views here.
def alerta(request):
    data = {}
    data["request"] = request
    if request.method == "POST":
        data['form2'] = Alerta2Form(request.POST)
        data['form'] = AlertaForm(request.POST)

        if data['form'].is_valid() and data['form2'].is_valid():
            aux = data['form2'].save()
            # aca el formulario valido
            aux2 = data['form'].save(commit=False)
            aux2.report = aux
            aux2.student = request.user.userprofile
            aux2.save()

            return HttpResponseRedirect(reverse('alerta'))

    else:
        data['form'] = AlertaForm()
        data['form2'] = Alerta2Form()
    template_name = 'alertas.html'
    return render(request, template_name, data)
