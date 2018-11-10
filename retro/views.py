# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from retro_auth.models import UserProfile
from django.contrib import messages
from .models import Section,Subject,Comment,CommentArchive,Post
from retro_auth.models import UserProfile
from django.db.models import Q
from retro.forms import post_form, post_form_document
from django.contrib.auth.models import User
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


#@login_required(login_url='/auth/login/')
def index(request):
	data = {}
	profile = UserProfile.objects.get(user=request.user,user_type=request.Sections['type'])
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

#@login_required(login_url='/auth/login/')
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

def create_comment_archives(new_comment,File):
    try:
        archive = CommentArchive(comment=new_comment, document= File)
        archive.save()
    except:
        pass


def post(request):
    data={}
    post = Post.objects.get(pk=1)
    all_comment = Comment.objects.filter(post=post)

    lista_coment = []
    file = ""
    for i in all_comment:
        try:
            file = CommentArchive.objects.get(comment = i)
            lista_coment.append([i,file])
        except:
            lista_coment.append([i,""])
    us = UserProfile.objects.get(user = request.user)
    data['comm'] = lista_coment
    if request.method == "POST":
        data['form'] = post_form(request.POST)
        if data['form'].is_valid():
            new_comment = Comment(post=post,description=request.POST['description'],author=us)
            new_comment.save()
            create_comment_archives(new_comment,request.FILES['document'])
            return redirect('post')

    else:
        data['form'] = post_form()
        data['form_arch'] = post_form_document()

    template_name = 'Post.html'
    return render(request, template_name, data)
