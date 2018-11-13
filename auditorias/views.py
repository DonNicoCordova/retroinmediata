from django.shortcuts import render
from django.shortcuts import redirect
from retro_auth.models  import *
from retro.models import *
from auditorias.forms import edit_umbral
import datetime

# Create your views here.

def auditorias(request):
    # mydate = datetime.datetime.now()
    user = UserProfile.objects.get(user=request.user)
    return render(request, "auditorias/auditorias.html", {"umbral":UserProfile.objects.all(), "date":Post.objects.all(), "now": datetime.datetime.now(), "My_umbral": user})

def edit_Umbral(request):
    data = {}
    data["umbral"] = UserProfile.objects.all()
    data["date"] = Post.objects.all()
    data["now"] = datetime.datetime.now()
    umbral = UserProfile.objects.get(user=request.user)
    teacher=UserProfile.objects.all()
    if umbral.usertype_set.all()[0].teacher:
        if request.method == 'GET':
            form = edit_umbral(instance=umbral)
        else:
            form = edit_umbral(request.POST,instance=umbral)
            if form.is_valid():
                form.save()
                return redirect('auditorias')
            return render(request, 'auditorias/edit_umbral.html', data)
        data['form'] = form
        return render(request, 'auditorias/edit_umbral.html', data)
    else:
        return redirect('auditorias')   
def is_teacher(request):
    userprofile=UserProfile.objects.all()
    # print(UserType.objects.filter(teacher="True"))
    print('-------------Userprofile-----------')
    print(userprofile)
    print('-------------Userprofile-----------')
    cant_usuarios=len(userprofile)
    print ('-----------CANTIDAD USUARIO------------')
    print(cant_usuarios)
    print ('-----------CANTIDAD USUARIO------------')
    teacher = UserProfile.objects.get(pk=1)
    # print ('-------------------UserProfile 1------------')
    # print (teacher)
    # print ('-------------------UserProfile 1------------')
    # teacher2 = UserProfile.objects.get(pk=3)
    # print ('-------------------UserProfile 2------------')
    # print (teacher2)
    # print ('-------------------UserProfile 2------------')
    # teacher3 = UserProfile.objects.get(pk=4)
    # print ('-------------------UserProfile 3------------')
    # print (teacher3)
    # print ('-------------------UserProfile 3------------')
    # print ('-----------TEACHER------------')
    # print(teacher)
    # print ('-----------TEACHER------------')
    # contador = 1
    # while contador <= cant_usuarios:
    #     teacher = UserProfile.objects.get(pk=contador)
        # if teacher.usertype_set.all()[0].teacher:
        #     print('-------------------TEACHER UMBRAL---------------')
        #     print(teacher.umbral)
        #     print('-------------------TEACHER UMBRAL---------------')
        #     print('-------------------CONTADOR IF---------------')
        #     print(contador)
        #     print('-------------------CONTADOR IF---------------')
        #     contador = contador + 1
        # else:
        #     return redirect('auditorias')
        # if contador <=2:
        #     teacher = UserProfile.objects.get(pk=contador)
        #     print('---------UMBRAL TEACHER------------')
        #     print(teacher.umbral)
        #     print('----------UMBRAL TEACHER-----------')
        #     contador = contador +1
        #     return redirect('is_teacher')
        # else:
        #     return redirect('auditorias')

def auditorias_aut(request):
    post = Post.objects.all()
    print ('--------------POST-------------')
    print (post)


    