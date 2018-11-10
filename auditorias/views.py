from django.shortcuts import render
from retro_auth.models import *
from retro.models import *

# Create your views here.

def auditorias(request):
    lista = []
    unico = []
    repetido= []
    con = []
    nel = []
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

    keywords = "buena los cabros".split(" ") 
    keywords_2 = "buena los cabros".split(" ")
    print(keywords)
    print(keywords_2)
    if keywords == keywords_2:
        print("vahj")
    else: 
        print("novahj")

    for i in keywords:
        for z in keywords_2:
            if i == z:
                con.append(i)
            else:
                nel.append(z)
            
    print(con)
    
    """if len(keywords) == len(con):
        print("Preguntas similares")
    else:
        print("diferentes")"""
    
    porcentaje1 = 100*len(con)/len(keywords)
    porcentaje2 = 100*len(con)/len(keywords)

    if porcentaje1 > 65:
        print("Similar")
    else:
        print("No similares")
    

    

    
        
    return render(request, "auditorias/auditorias.html", {"umbral":UserProfile.objects.all(), "date":Post.objects.all(), "parametros":contador,
                    "parametros_rep":repetido})


    
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



