from django.shortcuts import render
from .models import*
from django.http import JsonResponse
from datetime import datetime,timedelta


# Create your views here.
def NOTIFICATION(request):
	lista = []
	lista_hilo = []
	countNotifications = 0 
	TEMPLATE_NAME = "base.html"

	userprofile = UserProfile.objects.get(user = request.user)
	notificaciones = notification.objects.filter(user_ask = userprofile)
	notificaciones_hilo =  ThreadFollower.objects.filter(userprofile = userprofile)

	for x in notificaciones:
		lista.append(x)
		if x.status == True:
			countNotifications += 1

	for y in notificaciones_hilo:
		lista_hilo.append(y)
		if y.status == True:
			countNotifications += 1


	cantidad2 = len(lista_hilo)
	return render(request,TEMPLATE_NAME,{"notificaciones":lista,"countNotifications":countNotifications,"lista_hilo":lista_hilo})


def viewNotifications(request):
	response = {}

	pks = request.POST.getlist('info[]', False)

	for pk in pks:
		notifications = notification.objects.get(pk = int(pk))
		notifications.status = False
		
		notifications.save()

	return JsonResponse(response)


#funcion que indica al profesor que:
#1.)su umbral de tiempo de respuesta en un determinado post está a punto de vencer
#2.)su umbral de tiempo de respuesta en un determinado post ya venció

def notification_umbral_limit(request):
	TEMPLATE_NAME = "base.html"
	connected_user = UserProfile.objects.get(user=request.user) #Usuario conectado a la base de datos
	umbral = connected_user.umbral
	if(connected_user.is_teacher == True):
		list_no_comment = []
		list_to_comment = []
		listapost = Post.objects.filter(thread_sectionteacher=connected_user, publish_date_lt=datetime.now() - timedelta(days=umbral))
		for x in listapost:
			print(type(x))
			if (not x.comment_set.filter(author=connected_user).exists()):
				list_no_comment.append(x)
		umbral = umbral-1
		listapost2= Post.objects.filter(thread_sectionteacher=connected_user, publish_date_lt=datetime.now() - timedelta(days=umbral))
		for x in listapost2:
			if (not x.comment_set.filter(author=connected_user).exists()):
				list_to_comment.append(x)

	return render(request,TEMPLATE_NAME,{"list_no_comment":list_no_comment},{"list_to_comment":list_to_comment})

#NO SE HACEN 2 USUARIOS, SE HACE UN USUARIO GENERAL UTILIZANDO EL REQUEST.USER PARA RECONOCER
#EL USUARIO QUE ESTA CONECTADO
#ESTA REGLA DEBE CUMPLIRSE PARA AMBOS, PARA THREAD FOLLOWER COMO PARA NOTIFICATION

#para thread, al momento de crear un post se debe levantar una notificacion
#UTILIZAR AJAX PARA CUANDO SE OMENTE AGREGAR UNA NOTIFICACION EN ESTADO TRUE


