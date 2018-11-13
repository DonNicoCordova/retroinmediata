from django.shortcuts import render
from retro_auth.models import *
from retro.models import *


def auditorias(request):
    lista = []
    lista2= []
    repetido = []

    for x in Post.objects.all():
        lista.append(x.title.upper())

    keywords_2 = "buena los cabros".upper()

    key3 = keywords_2.split(" ")
    print("----------------------------")
    print(lista)
    print(key3)
    print("----------------------------")

    for i in lista:
        lista2.append(i.split(" "))
    print("----------------------------")
    print(lista2)
    print("----------------------------")

    print("****************************")
    print(lista2[8])

    for c in key3:
        for v in lista2[8]:
            if c == v:
                repetido.append(c)
    print("-------****")
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