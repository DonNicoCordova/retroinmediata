# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from retro_auth.models import UserProfile
from django.contrib import messages
from .models import Section,Subject
from django.db.models import Q
import requests
import json
import os
# Create your views here.


day_dict = {"Mo":"Lunes", "Tu":"Martes", "We":"Miercoles",
            "Th":"Jueves", "Fr":"Viernes", "Sa":"Sábado"}

module_dict = {"D1":"08:30 - 10:10", "D2":"10:20 - 12:00",
               "D3":"12:10 - 13:50", "D4":"14:00 - 15:40",
               "D5":"15:50 - 17:30", "D6":"17:40 - 19:20",
               "V1":"17:00 - 18:40", "V2":"18:50 - 20:30",
               "V3":"20:40 - 22:20"}


# @login_required(login_url='/auth/login/')
def index(request):
	data = {}
	profile = UserProfile.objects.get(user=request.user,user_type=request.session['type'])
	if request.session['type'] == "AL":
		sections = Section.objects.filter(Q(students=profile))
	else:
		sections = Section.objects.filter(Q(teacher=profile))

	data['sections'] = []
	for section in sections:
		if section.schedule != "Sin Horario":
			schedules = section.schedule.split("/")
			output = []
			for schedule in schedules:
				day = schedule.split(";")[0][:2]
				day = day_dict[day]
				time = schedule.split(";")[0][2:]
				time = module_dict[time]
				classroom = schedule.split(";")[1]
				output.append([day,time,classroom])

			data['sections'].append([section,output])
		else:
			data['sections'].append([section,section.schedule])

	template_name = "index.html"
	return render(request, template_name, data)

@login_required(login_url='/auth/login/')
def section_details(request,pk):
	template_name = 'section_details.html'
	data = {}

	if Section.objects.filter(pk=pk).exists():
		section = Section.objects.get(pk=pk)
		if section.schedule != "Sin Horario":
			schedules = section.schedule.split("/")
			output = []
			for schedule in schedules:
				day = schedule.split(";")[0][:2]
				day = day_dict[day]
				time = schedule.split(";")[0][2:]
				time = module_dict[time]
				classroom = schedule.split(";")[1]
				output.append([day,time,classroom])

			data['section'] = [section,output]
		else:
			data['section'] = [section,section.schedule]

	else:
		messages.error(request, 'No existe la sección.')
		return HttpResponseRedirect(reverse('index'))


	return render(request, template_name, data)

def edit_Post(request,pk_Post):
        post = Post.objects.get(pk=pk_Post)
        if request.method == 'GET':
            form = PostForm(instance=post)
        else:
            form = PostForm(request.POST,instance=post)
            if form.is_valid():
                form.save()
                #redirect que no se cual es
            return redirect('../')
            #redirect que no se cual es tampoco en los ''
        return render(request,'',{'form':form})
    else:
        return redirect('index')

def edit_Comment(request,pk_Comment):
        comment = Comment.objects.get(pk=pk_Comment)
        if request.method == 'GET':
            form = CommentForm(instance=comment)
        else:
            form = CommentForm(request.POST,instance=comment)
            if form.is_valid():
                form.save()
                #redirect que no se cual es
            return redirect('../')
            #redirect que no se cual es tampoco en los ''
        return render(request,'',{'form':form})
    else:
        # no se si redirecciona a index
        return redirect('index')
