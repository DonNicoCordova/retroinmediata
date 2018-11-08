# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required
from retro_auth.models import UserProfile
from django.contrib import messages
from .models import Section, Subject, Thread
from .forms import ThreadForms
from django.db.models import Q
import requests
import json
import os

# Create your views here.


day_dict = {"Mo": "Lunes", "Tu": "Martes", "We": "Miercoles",
            "Th": "Jueves", "Fr": "Viernes", "Sa": "Sábado"}

module_dict = {"D1": "08:30 - 10:10", "D2": "10:20 - 12:00",
               "D3": "12:10 - 13:50", "D4": "14:00 - 15:40",
               "D5": "15:50 - 17:30", "D6": "17:40 - 19:20",
               "V1": "17:00 - 18:40", "V2": "18:50 - 20:30",
               "V3": "20:40 - 22:20"}


@login_required(login_url='/auth/login/')
def index(request):
    # data = {}
    # profile = UserProfile.objects.get(user=request.user,user_type=request.session['type'])
    # if request.session['type'] == "AL":
    # 	sections = Section.objects.filter(Q(students=profile))
    # else:
    # 	sections = Section.objects.filter(Q(teacher=profile))
    #
    # data['sections'] = []
    # for section in sections:
    # 	if section.schedule != "Sin Horario":
    # 		schedules = section.schedule.split("/")
    # 		output = []
    # 		for schedule in schedules:
    # 			day = schedule.split(";")[0][:2]
    # 			day = day_dict[day]
    # 			time = schedule.split(";")[0][2:]
    # 			time = module_dict[time]
    # 			classroom = schedule.split(";")[1]
    # 			output.append([day,time,classroom])
    #
    # 		data['sections'].append([section,output])
    # 	else:
    # 		data['sections'].append([section,section.schedule])

    template_name = "index.html"
    return render(request, template_name, {})


@login_required(login_url='/auth/login/')
def section_details(request, pk):
    template_name = 'section_details.html'
    data = {}

    if Section.objects.filter(pk=pk).exists():
        section = Section.objects.get(pk=pk)
        data['threadform'] = ThreadForms()
        data['formvalid'] = True
        if request.POST:
            data['threadform'] = ThreadForms(request.POST)
            if data['threadform'].is_valid():
                data['threadform'] = data['threadform'].save(commit=False)
                data['threadform'].section = section
                data['threadform'].save()
                return HttpResponseRedirect(reverse('section_details', kwargs={'pk': pk}))
            else:
                data['formvalid'] = False
        data['section'] = section
        page = request.GET.get('page')
        search = request.GET.get('search')
        if search:
            threadlist = Thread.objects.filter(Q(name__icontains=search),
                                               section=section).order_by('-publish_date')
            data['searchFilter'] = '&search=' + search
        else:
            threadlist = Thread.objects.filter(section=section).order_by('-publish_date')
        paginator = Paginator(threadlist, 8)
        try:
            data['threadpage'] = paginator.page(page)
        except PageNotAnInteger:
            data['threadpage'] = paginator.page(1)
        except EmptyPage:
            data['threadpage'] = paginator.page(paginator.num_pages)
    # if section.schedule != "Sin Horario":
    # 	schedules = section.schedule.split("/")
    # 	output = []
    # 	for schedule in schedules:
    # 		day = schedule.split(";")[0][:2]
    # 		day = day_dict[day]
    # 		time = schedule.split(";")[0][2:]
    # 		time = module_dict[time]
    # 		classroom = schedule.split(";")[1]
    # 		output.append([day,time,classroom])
    #
    # 	data['section'] = [section,output]
    # else:
    # 	data['section'] = [section,section.schedule]

    else:
        messages.error(request, 'No existe la sección.')
        return HttpResponseRedirect(reverse('index'))

    return render(request, template_name, data)
