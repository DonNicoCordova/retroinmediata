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
from .forms import ThreadForms, PostForms
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
        if request.POST:
            data['postform'] = PostForms(request.POST)
            if data['postform'].is_valid():
                data['postform'] = data['postform'].save(commit=False)
                data['postform'].author = request.user.userprofile
                data['postform'].thread = thread
                data['postform'].save()
                return HttpResponseRedirect(reverse('thread_details', kwargs={'pk': pk}))
            else:
                data['formvalid'] = False
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
    else:
        messages.error(request, 'No existe el hilo.')
        return HttpResponseRedirect(reverse('index'))
    return render(request, template_name, data)


def post_details(request, pk):
    template_name = "post_details.html"
    data = {}
    if Post.objects.filter(pk=pk).exists():
        post = Post.objects.get(pk=pk)
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
        if request.method == "POST":
            data['form'] = post_form(request.POST)
            if data['form'].is_valid():
                new_comment = Comment(post=post, description=request.POST['description'],
                                      author=request.user.userprofile)
                new_comment.save()
                if request.FILES:
                    create_comment_archives(new_comment, request.FILES['document'])
                return HttpResponseRedirect(reverse('post_details', kwargs={'pk': pk}))
            print(data['form'].errors)
        else:
            data['form'] = post_form()
            data['form_arch'] = post_form_document()
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


def post(request):
    data = {}
    post = Post.objects.get(pk=1)
    all_comment = Comment.objects.filter(post=post)

    lista_coment = []
    file = ""
    for i in all_comment:
        try:
            file = CommentArchive.objects.get(comment=i)
            lista_coment.append([i, file])
        except:
            lista_coment.append([i, ""])
    us = UserProfile.objects.get(user=request.user)
    data['comm'] = lista_coment
    if request.method == "POST":
        data['form'] = post_form(request.POST)
        if data['form'].is_valid():
            new_comment = Comment(post=post, description=request.POST['description'], author=us)
            new_comment.save()
            create_comment_archives(new_comment, request.FILES['document'])
            return HttpResponseRedirect(reverse('post'))

    else:
        data['form'] = post_form()
        data['form_arch'] = post_form_document()

    template_name = 'Post.html'
    return render(request, template_name, data)


def question(request):
    template_name = 'question.html'

    # For Testing
    user = request.user.userprofile
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

        listComments.append(tuple((i, round(rankingAvg, 1))))

    if request.POST:
        if request.POST['rtype']=='sort':
            sortedList = []
            if request.POST['order']=='Ascending':
                sortedList = sorted(listComments,key=lambda t: t[1])
            elif request.POST['order']=='Descending':
                sortedList = sorted(listComments,reverse=True, key=lambda t: t[1])
            dictAnswersSorted = {}

            for index,items in enumerate(sortedList, start=1):
                dictAnswersSorted[index] = {}
                dictAnswersSorted[index]["pk"] = items[0].pk
                dictAnswersSorted[index]["description"] = items[0].description
                dictAnswersSorted[index]["author"] = '%s %s' % (items[0].author.user.first_name, items[0].author.user.last_name)
                dictAnswersSorted[index]["publish_date"] = items[0].publish_date
                dictAnswersSorted[index]["rating"] = items[1]
                print(dictAnswersSorted[index])
            return JsonResponse(dictAnswersSorted)

        if request.POST['rtype']=='rate':
            if CommentRanking.objects.filter(userprofile=user.id, comment=request.POST["comment"]).exists():
                crank = CommentRanking.objects.get(userprofile=user.id, comment=request.POST["comment"])
                crank.rating = request.POST["rating"]
            else:
                comment = Comment.objects.get(pk=request.POST["comment"])
                crank = CommentRanking(userprofile=user, comment=comment, rating=request.POST["rating"])
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
                    dictRatings[i.pk] = round(rankingAvg, 1)
            return JsonResponse(dictRatings)
    return render(request, template_name, {"Comments": listComments, 'Postpk': questionPk})


def forum(request):
        template_name = 'forum.html'

        #For Testing
        user = request.user.userprofile
        sectionPk = 1

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

            listThreads.append(tuple((i,round(rankingAvg, 1))))

        if request.POST:
            if request.POST['rtype']=='sort':
                sortedList = []
                if request.POST['order']=='Ascending':
                    sortedList = sorted(listThreads,key=lambda t: t[1])
                elif request.POST['order']=='Descending':
                    sortedList = sorted(listThreads,reverse=True, key=lambda t: t[1])
                dictThreadsSorted = {}

                for index,items in enumerate(sortedList, start=1):
                    dictThreadsSorted[index] = {}
                    dictThreadsSorted[index]["pk"] = items[0].pk
                    dictThreadsSorted[index]["name"] = items[0].name
                    dictThreadsSorted[index]["publish_date"] = items[0].publish_date
                    dictThreadsSorted[index]["rating"] = items[1]
                return JsonResponse(dictThreadsSorted)

            if request.POST['rtype']=='rate':
                if ThreadRanking.objects.filter(userprofile=user.id,thread=request.POST["thread"]).exists():
                    trank = ThreadRanking.objects.get(userprofile=user.id,thread=request.POST["thread"])
                    trank.rating = request.POST["rating"]
                else:
                    thread = Thread.objects.get(pk=request.POST["thread"])
                    trank = ThreadRanking(userprofile=user,thread=thread,rating=request.POST["rating"])
                trank.save()
                allThreads = Thread.objects.filter(section=sectionPk)
                dictRatings = {}

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
                        dictRatings[i.pk] = round(rankingAvg, 1)
                return JsonResponse(dictRatings)
        return render(request, template_name, {"Threads":listThreads,"SectionNRC":sectionNRC})


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
