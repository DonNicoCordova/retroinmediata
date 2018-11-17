# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from retro.models import CommentRanking, ThreadRanking, ThreadFollower, PostFollower
from django.db.models import Q
from retro_auth.models import UserProfile
from .models import Section, Thread, Comment, CommentArchive, Post
from .forms import ThreadForms, PostForms
from alertas.models import Alerta, AnswerReport
import re
from django.db.models import Q
from django.views.decorators.csrf import csrf_exempt

# Create your views here.


day_dict = {"Mo": "Lunes", "Tu": "Martes", "We": "Miercoles",
            "Th": "Jueves", "Fr": "Viernes", "Sa": "Sábado"}

module_dict = {"D1": "08:30 - 10:10", "D2": "10:20 - 12:00",
               "D3": "12:10 - 13:50", "D4": "14:00 - 15:40",
               "D5": "15:50 - 17:30", "D6": "17:40 - 19:20",
               "V1": "17:00 - 18:40", "V2": "18:50 - 20:30",
               "V3": "20:40 - 22:20"}


def coincidencia(nuevo_post,Thread):
    
    lista = []
    lista2= []
    aux=[]
    repetido = []
    
    #se traen los post y se pasan a mayuscula para poder comparar
    for x in Post.objects.filter(thread = Thread):
        lista.append(x.title.upper())
    
    # keywords_2 sera el post recibido
    keywords_2 = nuevo_post.upper()
    
    #se pasa el post a pequeñas listas
    key3 = keywords_2.split(" ")

    # agrega las preguntas a una lista
    for i in lista:
        lista2.append(i.split(" "))
        
    #compara las palabras del nuevo post con las preguntas de todos los post 
    # en vase a un porcentaje mayor a 65% de coincidencia
    # agregar filtro de preguntas de un hilo
    
    for palubria in lista2:
        repetido = []
        aux=[]
        for v in key3:
            aux.append(str(v))
            if len(palubria) > 1:
                for b in palubria:
                    if v == b:
                        repetido.append(b)

            elif len(palubria)==1 and palubria == aux:
                return([True,palubria])
                
        porcentaje1 = 100*len(repetido)/len(key3) #66.6%
        print(porcentaje1)

        if porcentaje1 > 65:
            # data para html para mostrar alerta de coincidencia
            return([True,palubria])
        
    return([False,""])


@login_required(login_url='/auth/login/')
def index(request):
    template_name = "index.html"
    return render(request, template_name, {'sections': Section.objects.filter(Q(teacher=request.user.userprofile) | Q(student__student=request.user.userprofile))})


@login_required(login_url='/auth/login/')
def section_details(request, pk):
    template_name = 'section_details.html'
    data = {}

    if Section.objects.filter(pk=pk).exists():
        section = Section.objects.get(pk=pk)
        data['threadform'] = ThreadForms()
        data['formvalid'] = True
        if request.POST:
            if request.POST['action'] == 'createThread':
                data['threadform'] = ThreadForms(request.POST)
                if data['threadform'].is_valid():
                    data['threadform'] = data['threadform'].save(commit=False)
                    data['threadform'].section = section
                    data['threadform'].save()
                    return HttpResponseRedirect(reverse('section_details', kwargs={'pk': pk}))
                else:
                    data['formvalid'] = False
            elif request.POST['action'] == 'followThread':
                follow = ThreadFollower.objects.filter(userprofile=request.user.userprofile, thread_id=request.POST['pk'])
                if follow:
                    follow[0].delete()
                else:
                    ThreadFollower.objects.create(userprofile=request.user.userprofile, thread_id=request.POST['pk'])
                return JsonResponse({})
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
        data['follow'] = ThreadFollower.objects.filter(thread__in=data['threadpage']).values_list('thread_id', flat=True)
    else:
        messages.error(request, 'No existe la sección.')
        return HttpResponseRedirect(reverse('index'))

    return render(request, template_name, data)


def thread_details(request, pk):
    template_name = "thread_details.html"
    data = {}
    if Thread.objects.filter(pk=pk).exists():
        thread = Thread.objects.get(pk=pk)
        data['postform'] = PostForms()
        data['formvalid'] = True
        data['postparecido']=0
        if request.POST:
            if request.POST['action'] == 'createPost':
                data['postform'] = PostForms(request.POST)
                if data['postform'].is_valid():
                    a = coincidencia(request.POST["title"],thread)
                    print(a)
                    if a[0] == True:
                        frase = ' '.join(a[1])
                        data['postparecido']=1
                        data['postfrase'] = frase
                    else:
                        data['postform'] = data['postform'].save(commit=False)
                        data['postform'].author = request.user.userprofile
                        data['postform'].thread = thread
                        data['postform'].save()
                        return HttpResponseRedirect(reverse('thread_details', kwargs={'pk': pk}))
                else:
                    if a[0] != True:
                        data['formvalid'] = False
            elif request.POST['action'] == 'followPost':
                follow = PostFollower.objects.filter(userprofile=request.user.userprofile, post_id=request.POST['pk'])
                if follow:
                    follow[0].delete()
                else:
                    PostFollower.objects.create(userprofile=request.user.userprofile, post_id=request.POST['pk'])
                return JsonResponse({})
        data['thread'] = thread
        page = request.GET.get('page')
        search = request.GET.get('search')
        if search:
            postlist = Post.objects.filter(Q(title__icontains=search),
                                           thread=thread).order_by('-publish_date')
            data['searchFilter'] = '&search=' + search
        else:
            postlist = Post.objects.filter(thread=thread).order_by('-publish_date')
        paginator = Paginator(postlist, 8)
        try:
            data['postlist'] = paginator.page(page)
        except PageNotAnInteger:
            data['postlist'] = paginator.page(1)
        except EmptyPage:
            data['postlist'] = paginator.page(paginator.num_pages)
        data['follow'] = PostFollower.objects.filter(post__in=data['postlist']).values_list('post_id', flat=True)
    else:
        messages.error(request, 'No existe el hilo.')
        return HttpResponseRedirect(reverse('index'))
    return render(request, template_name, data)


def post_details(request, pk):
    template_name = "post_details.html"
    data = {}
    if Post.objects.filter(pk=pk).exists():
        post = Post.objects.get(pk=pk)
        if request.POST:
            if request.POST['action'] == 'report_teacher':
                alert = AnswerReport.objects.create(description='El alumno ' + request.user.first_name + ' ' + request.user.last_name + ' ha reportado que el profesor <b>'
                                                                + post.thread.section.teacher.user.first_name + ' ' + post.thread.section.teacher.user.last_name +
                                                                '</b> no ha contestado la pregunta: <b>' + post.title + '</b>')
                alert.createReport(request.user.userprofile, post.thread.section.teacher, post.thread.section.careersubjectsection.career.director)
        all_comment = Comment.objects.filter(post=post)
        listComments = []
        for i in all_comment:
            rankingSum = 0
            rankingAvg = 0.0
            numRatings = 0
            rankings = CommentRanking.objects.filter(comment=i)

            for j in rankings:
                rankingSum += j.rating
                numRatings += 1

            if (numRatings != 0):
                rankingAvg = rankingSum / numRatings

            try:
                file = CommentArchive.objects.get(comment=i)
                listComments.append(tuple((i, rankingAvg, file)))
            except:
                listComments.append(tuple((i, rankingAvg, "")))
        data['Comments'] = listComments
        data['post'] = post
    else:
        messages.error(request, 'No existe la pregunta.')
        return HttpResponseRedirect(reverse('index'))
    return render(request, template_name, data)


def create_comment_archives(new_comment, File):
    try:
        archive = CommentArchive(comment=new_comment, document=File)
        archive.save()
    except CommentArchive.DoesNotExist:
        pass

@csrf_exempt
def comment_post(request):
    if request.method == "POST":
        cleanr = re.compile('<.*?>')
        cleantext = re.sub(cleanr, '', request.POST['content'])
        if request.POST.get('content', False) and cleantext != "":
            post = Post.objects.get(pk=request.POST['Postpk'])
            author = UserProfile.objects.get(user=request.user)
            n_comment = Comment.objects.create(
                post=post,
                description=request.POST["content"],
                author=author,
                status=0,
            )
            n_comment.save()
            n_file = CommentArchive.objects.create(
                comment=n_comment,
                document=request.FILES['document'] if request.FILES.get('document', False) else None,
            )
            n_file.save()
            data = {
                'message': "ok"
            }
            Alerta.objects.create(post_id=request.POST['Postpk'], student_question=post.author, student_answerd=request.user.userprofile)
            return JsonResponse(data)
        else:
            data = {'message': 'fail'}
            return JsonResponse(data)
    else:
        return HttpResponseRedirect(reverse('index'))


@csrf_exempt
def delete_post(request):
    data = {}
    data['post'] = Post.objects.all()
    post_id = request.POST["pk"]
    comment = Comment.objects.filter(post=post_id).delete()
    Post.objects.get(pk=post_id).delete()
    return JsonResponse({'message': 'ok'})


@csrf_exempt
def delete_comment(request):
    data = {}
    comment_id = request.POST["pk"]
    comment = Comment.objects.get(pk=comment_id).delete()
    return JsonResponse({'message': 'ok'})

def delete_imag(request):
    data = {}
    print("holi")
    archive = CommentArchive.objects.get(pk=request.POST["pk"]).delete()
    return JsonResponse({'message': 'ok'})


@csrf_exempt
def frequent_questions_student(request):
	data={}
	template_name = "frequent_questions_student.html"
	return render(request, template_name,data)

@csrf_exempt
def frequent_questions_teacher(request):
	data={}
	template_name = "frequent_questions_teacher.html"
	return render(request, template_name,data)


def update_comment(request):
    data = {}
    comment_id = request.POST["pk"]
    comment = Comment.objects.get(pk=comment_id)
    comment.description = request.POST["comment"]
    comment.save()
    data["text"] = comment.description
    data["message"] = "ok"
    return JsonResponse(data)

def update_post(request):
    data = {}
    print(request.POST)
    post_id = request.POST["pk"]
    post = Post.objects.get(pk=post_id)
    post.title = request.POST['title']
    post.save()
    post.description = request.POST["comment"]
    post.save()
    data["text"] = post.description
    data["title"] = post.title
    data["message"] = "ok"
    return JsonResponse(data)
