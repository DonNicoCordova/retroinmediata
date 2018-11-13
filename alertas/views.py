from django.shortcuts import render
from alertas.forms import *
from retro_auth.models  import *
from retro.models import *

# Create your views here.
def alerta(request):
    data = {}
    data["request"] = request
    if request.method == "POST":
        data['form'] = AlertaForm(request.POST, request.FILES)

        if data['form'].is_valid():
            # aca el formulario valido
            data['form'].save()

            return render(request, "alertas/alertas.html")

    else:
        data['form'] = AlertaForm()