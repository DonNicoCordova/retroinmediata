from django.shortcuts import render
from retro_auth.models  import *
from retro.models import *
import datetime


# Create your views here.

#def auditorias(request):
#    # mydate = datetime.datetime.now()
#    return render(request, "auditorias/auditorias.html", {"umbral":UserProfile.objects.all(), "date":Post.objects.all(), "now": datetime.datetime.now()})
def porcentaje(lista1,keywords_2):
    print(len(lista1),len(keywords_2))
    porcentaje1 = 100*len(lista1)/len(keywords_2) #66.6%
    print(porcentaje1)

    if porcentaje1 > 65:
        print("Similar")
    else:
        print("No similares")

def auditorias(request):
    lista = []
    lista2= []
    repetido = []

    for x in Post.objects.all():
        lista.append(x.title.upper())

    keywords_2 = "buena los cabros".upper()

    key3 = keywords_2.split(" ")

    for i in lista:
        lista2.append(i.split(" "))

        
    #volver la lista repetidos a cero
    #agregar el else cuando es una sola palabra
    #mandar las weas a porcentaje antes de volver la lista a cero
    for palubria in lista2:
        print(len(palubria))
        for v in key3:
            if len(palubria) > 1:
                for b in palubria:
                    if v == b:
                        repetido.append(b)
                        
    print("-------**")
    print(repetido)

#    for m in key3:
#        print(m)
#        if z == m:
#            repetido.append(z)

#    print (contador)
#    print('\n')



    #keywords_2 = ['buena los cabros']
#    print(keywords_2)
#    print(lista1)


    return render(request, "auditorias/auditorias.html", {"umbral":UserProfile.objects.all(), "date":Post.objects.all(),"parametros_rep":repetido})


    
"""
def auditorias(request):
            
    return render(request, "auditorias/auditorias.html", {"date":Post.objects.all()})
"""
"""
def repetido(request):
    lista = []
    unico = []
    repetido= []
    contador = 0
    for x in Post.objects.all():
        lista.append(x.title)
        for z in lista:
            if z not in unico:
                unico.append(z)
            else:
                if z not in repetido:
                    repetido.append(z)
                    contador += 1
                    #return render(request, "auditorias/auditorias.html", {"otro":Post.objects.all()})
            
    print (contador)
    print (repetido)
    return render(request, "auditorias/prueba.html", {"parametros":contador})
"""

