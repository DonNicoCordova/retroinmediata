# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib import messages
from retro_auth.models import UserProfile
from retro.models import Section,Subject
import datetime
import ast
import json
import os
import requests

def auth_login(request):
    logout(request)
    username = password = ''
    if request.POST:
        request.session["h"] = 0
        username = request.POST["username"]
        password = request.POST["password"]
        post_data = {
            'username': username,
            'password': request.POST["password"]
        }
        response = requests.post(
            os.getenv("AUTH_URL")+str("/rest-auth/login/"), data=post_data)
        content = response.content.decode('utf-8')
        content = json.loads(content)
        if "key" in content:
            post_data = {'username': username}
            header = {"Content-Type": 'application/json',
                        "Authorization": "Token " + content["key"]}
            response_1 = requests.get(
                os.getenv("AUTH_URL")+'/rest-auth/user/', headers=header, data=post_data)
            content_1 = json.loads(response_1.content.decode("utf-8"))
            request.session["name"] = content_1["first_name"] + \
                " " + content_1["last_name"]
            request.session["token"] = content["key"]
            header = {"Content-Type": 'application/x-www-form-urlencoded',
                        'Authorization': "Token " + content["key"]}
            post_data = {'user_pk': content_1['pk'],
                            'period': datetime.date.today().year}
            response_2 = requests.post(
                os.getenv("AUTH_URL")+'/get/get_user_info/', headers=header, data=post_data)
            content_2 = json.loads(response_2.content.decode("utf-8"))
            content_2 = content_2['user_info']
            request.session["user_pk"] = content_1['pk']
            request.session["username"] = username
            request.session["rut"] = content_2['user_rut']
            request.session["type"] = content_2['user_type']
            if content_1['first_name'][0] == " ":
                first = content_1['first_name'][1:].split(" ")
            else:
                first = content_1['first_name'].split(" ")

            if content_1["last_name"][0] == " ":
                last = content_1["last_name"][1:].split(" ")
            else:
                last = content_1["last_name"].split(" ")

            full_name = ""
            for name in first:
                full_name += name.capitalize()+" "

            for name in last:
                full_name += name.capitalize()+" "

            if not User.objects.filter(username=username).exists():
                n_usuario = User.objects.create_user(
                    username=username,
                    password=password
                )
                n_usuario.save()
                n_usuario.first_name = content_1['first_name']
                n_usuario.last_name = content_1['last_name']
                n_usuario.save()

                if request.session["type"] == "AL":
                    try:
                        profile = UserProfile.objects.get(
                            rut = content_2['user_rut']
                        )
                        profile.api_pk = content_1["pk"]
                        profile.user = n_usuario
                        profile.save()

                    except UserProfile.DoesNotExist:
                        profile = UserProfile.objects.create(
                            api_pk = content_1['pk'],
                            user=n_usuario,
                            name=full_name,
                            user_type="AL",
                            carreer=content_2["carreer_pk"],
                            rut=content_2['user_rut'],
                        )
                        profile.save()
                    

                else:
                    try:
                        profile = UserProfile.objects.get(
                            rut = content_2['user_rut']
                        )
                        profile.api_pk = content_1["pk"]
                        profile.user = n_usuario
                        profile.save()

                    except UserProfile.DoesNotExist:
                        profile = UserProfile.objects.create(
                            api_pk = content_1['pk'],
                            user=n_usuario,
                            name=full_name,
                            user_type="DO",
                            carreer=content_2["carreer_pk"],
                            rut=content_2['user_rut'],
                        )
                        profile.save()
                    
                login(request, n_usuario)
                
                post_data = {'user_pk': profile.api_pk,'user_type':profile.user_type,'period':201820}
                header = {"Content-Type": 'application/x-www-form-urlencoded',
                            "Authorization": "Token " + request.session["token"]}
                response_subjects = requests.post(os.getenv("AUTH_URL")+'/get/get_current_sections/', headers=header, data=post_data)
                content_subjects = json.loads(response_subjects.content.decode("utf-8"))

                for teacher in content_subjects["teachers"]:
                    if UserProfile.objects.filter(rut=teacher['rut']).exists():
                        teacher_profile = UserProfile.objects.get(rut=teacher['rut'],user_type="DO")
                    else:
                        teacher_profile = UserProfile.objects.create(
                            name = teacher['name'],
                            rut = teacher['rut'],
                            user_type = "DO",
                            user = None,
                        )
                        teacher_profile.save()

                for course in content_subjects['courses']:
                    if Section.objects.filter(api_pk=course['pk']).exists():
                        section = Section.objects.get(api_pk=course['pk'])
                        if not section.students.filter(pk=profile.pk).exists():
                            section.students.add(profile)
                            section.save()
                        else:
                            pass
                    else:
                        try:
                            subject = Subject.objects.get(api_pk=course['subject_pk'])
                        
                        except Subject.DoesNotExist:
                            subject = Subject.objects.create(
                                api_pk = course['subject_pk'],
                                name = course['subject'],
                                subject_code = course['subject_code']
                            )
                            subject.save()

                        teacher = UserProfile.objects.get(name=course['teacher'])
                        section_type = "AY" if len(course['schedule'].split("/")) == 1 else "CA"
                        section = Section.objects.create(
                            section_type = section_type,
                            api_pk = course['pk'],
                            teacher = teacher,
                            subject = subject,
                            schedule = course["schedule"],
                            nrc = course['nrc'],
                        )
                        section.save()
                    

                    section.students.add(profile)
                    section.save()

                for tutory in content_subjects['tutories']:
                    if Section.objects.filter(api_pk=tutory['pk']).exists():
                        section = Section.objects.get(api_pk=tutory['pk'])
                        if not section.students.filter(pk=profile.pk).exists():
                            section.students.add(profile)
                            section.save()
                        else:
                            pass
                    else:
                        try:
                            subject = Subject.objects.get(api_pk=tutory['subject_pk'])
                        
                        except Subject.DoesNotExist:
                            subject = Subject.objects.create(
                                api_pk = tutory['subject_pk'],
                                name = tutory['subject'],
                                subject_code = tutory['subject_code']
                            )
                            subject.save()

                        teacher = UserProfile.objects.get(name=tutory['teacher'])
                        section = Section.objects.create(
                            section_type = "AY",
                            api_pk = tutory['pk'],
                            teacher = teacher,
                            subject = subject,
                            schedule = tutory['schedule'],
                            nrc = tutory['nrc'],
                        )
                        section.save()
                    
                    
                    section.students.add(profile)
                    section.save()



                return HttpResponseRedirect(reverse('index'))
            else:
                user = authenticate(
                    username=username,
                    password=password
                )
                login(request, user)
                profile = UserProfile.objects.get(user=user)
                post_data = {'user_pk': profile.api_pk,'user_type':profile.user_type,'period':201820}
                print(post_data)
                header = {"Content-Type": 'application/x-www-form-urlencoded',
                            "Authorization": "Token " + request.session["token"]}
                response_subjects = requests.post(os.getenv("AUTH_URL")+'/get/get_current_sections/', headers=header, data=post_data)
                content_subjects = json.loads(response_subjects.content.decode("utf-8"))
                print ("Estos son los cursos: ", content_subjects)

                for teacher in content_subjects["teachers"]:
                    if UserProfile.objects.filter(rut=teacher['rut']).exists():
                        teacher_profile = UserProfile.objects.get(rut=teacher['rut'],user_type="DO")
                    else:
                        teacher_profile = UserProfile.objects.create(
                            name = teacher['name'],
                            rut = teacher['rut'],
                            user_type = "DO",
                            user = None,
                        )
                        teacher_profile.save()

                for course in content_subjects['courses']:
                    if Section.objects.filter(api_pk=course['pk']).exists():
                        section = Section.objects.get(api_pk=course['pk'])
                        if not section.students.filter(pk=profile.pk).exists():
                            section.students.add(profile)
                            section.save()
                        else:
                            pass
                    else:
                        try:
                            subject = Subject.objects.get(api_pk=course['subject_pk'])
                        
                        except Subject.DoesNotExist:
                            subject = Subject.objects.create(
                                api_pk = course['subject_pk'],
                                name = course['subject'],
                                subject_code = course['subject_code']
                            )
                            subject.save()

                        teacher = UserProfile.objects.get(name=course['teacher'])
                        section_type = "AY" if len(course['schedule'].split("/")) == 1 else "CA"
                        section = Section.objects.create(
                            section_type = section_type,
                            api_pk = course['pk'],
                            teacher = teacher,
                            subject = subject,
                            schedule = course["schedule"],
                            nrc = course['nrc'],
                        )
                        section.save()
                    

                    section.students.add(profile)
                    section.save()

                for tutory in content_subjects['tutories']:
                    if Section.objects.filter(api_pk=tutory['pk']).exists():
                        section = Section.objects.get(api_pk=tutory['pk'])
                        if not section.students.filter(pk=profile.pk).exists():
                            section.students.add(profile)
                            section.save()
                        else:
                            pass
                    else:
                        try:
                            subject = Subject.objects.get(api_pk=tutory['subject_pk'])
                        
                        except Subject.DoesNotExist:
                            subject = Subject.objects.create(
                                api_pk = tutory['subject_pk'],
                                name = tutory['subject'],
                                subject_code = tutory['subject_code']
                            )
                            subject.save()

                        teacher = UserProfile.objects.get(name=tutory['teacher'])
                        section = Section.objects.create(
                            section_type = "AY",
                            api_pk = tutory['pk'],
                            teacher = teacher,
                            subject = subject,
                            schedule = tutory['schedule'],
                            nrc = tutory['nrc'],
                        )
                        section.save()
                    
                    
                    section.students.add(profile)
                    section.save()

                return HttpResponseRedirect(reverse('index'))
        else:
            messages.error(request, 'Usuario y contraseña invalidos. Intentelo nuevamente.')
    data = {}
    template_name = "login.html"
    return render(request, template_name, data)


def auth_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))
