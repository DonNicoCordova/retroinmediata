from django.shortcuts import render
from retro_auth.models  import *
from retro.models import *
import datetime


# Create your views here.

#def auditorias(request):
#    # mydate = datetime.datetime.now()
#    return render(request, "auditorias/auditorias.html", {"umbral":UserProfile.objects.all(), "date":Post.objects.all(), "now": datetime.datetime.now()})

def auditorias(request):
    lista = []
    lista2= []
    vacio = []
    aux=[]
    repetido = []

    for x in Post.objects.all():
        lista.append(x.title.upper())

    keywords_2 = "buena los cabros".upper()

    key3 = keywords_2.split(" ")

    for i in lista:
        lista2.append(i.split(" "))

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
                print("ya hay un tema parecido: ",palubria)
                
        porcentaje1 = 100*len(repetido)/len(key3) #66.6%
        print(porcentaje1)

        if porcentaje1 > 65:
            print("Similar a",palubria)
        else:
            print("No similares")

        
    return render(request, "auditorias/auditorias.html",{"umbral":UserProfile.objects.all(),"date":Post.objects.all()})

#   "parametros_rep":repetido})