from django.shortcuts import render, reverse, redirect
from retro_auth.models  import *
from retro.models import *
from .models import ForoAudit
from auditorias.forms import edit_umbral, ForoAuditForm
from alertas.forms import AnswerReportUser
import datetime


def auditorias(request):
    data = {}
    if request.user.userprofile.is_dcareer:
        data['form'] = ForoAuditForm(request=request)
        if request.POST:
            data['form'] = ForoAuditForm(request.POST, request=request)
            if data['form'].is_valid():
                data['form'] = data['form'].save(commit=False)
                alert = AnswerReportUser.objects.get(report_id=request.POST['alert'])
                data['form'].director = request.user.userprofile
                data['form'].student = alert.student
                data['form'].teacher = alert.teacher
                data['form'].save()
                return redirect('auditorias')
            else:
                return render(request, "auditorias/auditorias.html", data)
        return render(request, "auditorias/auditorias.html", data)
    return redirect('index')


def historial_auditorias(request):
    data = {}
    data['auditoria'] = ForoAudit.objects.all()
    template_name = "auditorias/_auditorias.html"
    return render(request, template_name, data)


def buscar_auditorias(request):
    template_name = "auditorias/_auditorias2.html"
    data = {}
    data['auditorias'] = ForoAudit.objects.all()

    return render(request, template_name, data)


def edit_Umbral(request):
    data = {}
    data["umbral"] = UserProfile.objects.all()
    data["date"] = Post.objects.all()
    data["now"] = datetime.datetime.now()
    umbral = UserProfile.objects.get(user=request.user)
    # teacher=UserProfile.objects.all()
    if umbral.is_teacher == True:
        if request.method == 'GET':
            print ('holi')
            form = edit_umbral(instance=umbral)
        else:
            form = edit_umbral(request.POST,instance=umbral)
            if form.is_valid():
                form.save()
                return redirect('edit_Umbral')
        data['form'] = form
        return render(request, 'auditorias/edit_umbral.html', data)
    else:
        return redirect('auditorias')


def auditorias_aut(request):
    post = Post.objects.all()
    for x in post:
        comment = Comment.objects.all()
        return redirect('../edit_umbral.html')