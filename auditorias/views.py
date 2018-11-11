from django.shortcuts import render
from retro_auth.models import *
from retro.models import *

# Create your views here.

def auditorias(request):
    lista = []
    unico = []
    repetido= []
    lista1 = []
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
                

    print (contador)
    print (repetido)
    print('\n')
    print(lista)

    keywords_2 = "buena los cabros".split(" ")
    #keywords_2 = ['buena los cabros']
    print(keywords_2)

    for i in lista:
        print(i)
        for m in keywords_2:
            if i == m:
                lista1.append(i)
    
    print(lista1)
    
    porcentaje1 = 100*len(lista1)/len(keywords_2) #66.6%
    print(porcentaje1)

    if porcentaje1 > 65:
        print("Similar")
    else:
        print("No similares")
    


    return render(request, "auditorias/auditorias.html", {"umbral":UserProfile.objects.all(), "date":Post.objects.all(), "parametros":contador,
                    "parametros_rep":repetido, "parametros_rep2":porcentaje1})


    
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



