# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from retro.models import CommentRanking, ThreadRanking
from django.db.models import Q
from retro_auth.models import UserProfile
from retro.forms import post_form, post_form_document
from .models import Section, Thread, Comment, CommentArchive, Post
from .forms import ThreadForms
import re
from django.views.decorators.csrf import csrf_exempt
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
    # profile = UserProfile.objects.get(user=request.user,user_type=request.Sections['type'])
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
            return HttpResponseRedirect(reverse('post'))

    else:
        data['form'] = post_form()
        data['form_arch'] = post_form_document()

    template_name = 'Post.html'
    return render(request, template_name, data)

def question(request):
	template_name = 'question.html'

	#For Testing
	user = UserProfile.objects.get(rut="111111111")
	questionPk = 1

	comments = Comment.objects.filter(post=questionPk)

	listComments = []
	for i in comments:
		rankingSum = 0
		rankingAvg = 0.0
		numRatings = 0
		rankings = CommentRanking.objects.filter(comment=i)

		for j in rankings:
			rankingSum += j.rating
			numRatings += 1

		if (numRatings != 0):
			rankingAvg = rankingSum / numRatings

		listComments.append(tuple((i,rankingAvg)))

	if request.POST:
		if CommentRanking.objects.filter(userprofile=user.id,comment=request.POST["comment"]).exists():
			crank = CommentRanking.objects.get(userprofile=user.id,comment=request.POST["comment"])
			crank.rating = request.POST["rating"]
		else:
			comment = Comment.objects.get(pk=request.POST["comment"])
			crank = CommentRanking(userprofile=user,comment=comment,rating=request.POST["rating"])

		crank.save()
		comments = Comment.objects.filter(post=questionPk)
		dictRatings = {}

		for i in comments:
			rankingSum = 0
			rankingAvg = 0.0
			numRatings = 0
			rankings = CommentRanking.objects.filter(comment=i)

			for j in rankings:
				rankingSum += j.rating
				numRatings += 1
			if (numRatings != 0):
				rankingAvg = rankingSum / numRatings
				dictRatings[i.pk] = rankingAvg
		#print (request.POST["rating"])
		return JsonResponse(dictRatings)
	return render(request, template_name, {"Comments":listComments,'Postpk':questionPk})

def forum(request):
	template_name = 'forum.html'

	#For Testing
	user = UserProfile.objects.get(rut="111111111")
	sectionPk = 1
	questionPk = 1
	allThreads = Thread.objects.filter(section=sectionPk)
	section = Section.objects.get(pk=allThreads[0].section.id)
	sectionNRC = section.nrc

	listThreads = []
	for i in allThreads:
		rankingSum = 0
		rankingAvg = 0.0
		numRatings = 0
		rankings = ThreadRanking.objects.filter(thread=i)

		for j in rankings:
			rankingSum += j.rating
			numRatings += 1

		if (numRatings != 0):
			rankingAvg = rankingSum / numRatings

		listThreads.append(tuple((i,rankingAvg)))

	if request.POST:
		if ThreadRanking.objects.filter(userprofile=user.id,thread=request.POST["thread"]).exists():
			trank = ThreadRanking.objects.get(userprofile=user.id,thread=request.POST["thread"])
			trank.rating = request.POST["rating"]
		else:
			thread = Comment.objects.get(pk=request.POST["thread"])
			trank = ThreadRanking(userprofile=user,thread=thread,rating=request.POST["rating"])
		trank.save()
		allThreads = Comment.objects.filter(post=questionPk)
		dictRatings = {}

		for i in allThreads:
			rankingSum = 0
			rankingAvg = 0.0
			numRatings = 0
			rankings = CommentRanking.objects.filter(comment=i)

			for j in rankings:
				rankingSum += j.rating
				numRatings += 1
			if (numRatings != 0):
				rankingAvg = rankingSum / numRatings
				dictRatings[i.pk] = rankingAvg
		#print (request.POST["rating"])
		return JsonResponse(dictRatings)
	return render(request, template_name, {"Threads":listThreads,"SectionNRC":sectionNRC})

@csrf_exempt
def comment_post(request):
	if request.method == "POST":
		print("Entre al POST")
		cleanr = re.compile('<.*?>')
		cleantext = re.sub(cleanr, '', request.POST['content'])
		if request.POST.get('content',False) and cleantext != "":
			print("Entre al if")
			post = Post.objects.get(pk=1)
			author = UserProfile.objects.get(user=request.user)
			n_comment = Comment.objects.create(
				post=post,
				description=request.POST["content"],
				author=author,
				status=0,
			)
			n_comment.save()
			print("Comment creado")
			n_file = CommentArchive.objects.create(
				comment=n_comment,
				document=request.FILES['saved_file'] if request.FILES.get('saved_file',False) else None,
			)
			n_file.save()
			print("File creado")
			data = {
				'message':"ok"
			}
			return JsonResponse(data)
		else:
			print("Entre al else")
			data = {'message' : 'fail'}
			return JsonResponse(data)
	else:
		return HttpResponseRedirect(reverse('index'))

@login_required(login_url='/auth/login/')
def delete_post(request, post_id):
    data = {}
    template_name = 'section_details.html'
    data['post'] = Post.objects.all()
    comment = Comment.objects.filter(post = post_id).delete()
    Post.objects.get(pk=post_id).delete()
    return HttpResponseRedirect(reverse('section_details'))
#ESTA FUNCION NO SABÍA COMO FILTRAR LOS COMENTARIOS DEL POST QUE SE ESTA BORRANDO, NECESITO PROBARLO PARA SABER SI FUNCIONA
