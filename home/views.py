import os
from django.shortcuts import render, HttpResponse
from .models import Book, Bible
from django.http import JsonResponse

import sqlite3
 
pwd = os.path.dirname(__file__)

def index (request):
    books           = Book.objects.all()
    bibles          = Bible.objects.all()
    bibles_active   = Bible.objects.filter(activo=1)
    colors = ['#145cc9', '#1ac914', '#dc3545']
    
    return render(request, 'home/index.html', {'books': books, 'n' : range(1,30), 'bibles':bibles, 'bibles_active':bibles_active})

def sql (traduccion, libro, capitulo, verso):
    
    bible = pwd+'/bibles/'+traduccion
    con = sqlite3.connect(bible)
    
    cursorObj = con.cursor()
    texto = cursorObj.execute('select Scripture from Bible WHERE Book = '+libro+' AND Chapter = '+capitulo+' AND Verse = '+verso)
    
    return texto.fetchall()[0][0]

def capitulos(request):
    libro   = request.POST['libro']
    bible   = pwd+'/bibles/Biblia del Oso.bbli'
    con     = sqlite3.connect(bible)
    cursorObj = con.cursor()
    capitulos = ''

    max = int( cursorObj.execute('SELECT MAX(DISTINCT Chapter) FROM Bible WHERE Book = '+libro).fetchall()[0][0] )
    
    for i in range(1,(max+1)):
        capitulos+= '<option value="'+str(i)+'">'+str(i)+'</option>'
    
    data = {'success': 'true', 'capitulos': capitulos}

    return JsonResponse(data)

def versiculos(request):
    libro       = request.POST['libro']
    capitulo    = request.POST['capitulo']
    bible   = pwd+'/bibles/Biblia del Oso.bbli'
    con     = sqlite3.connect(bible)
    cursorObj = con.cursor()
    versiculos = ''

    max = int( cursorObj.execute('SELECT MAX(DISTINCT Verse) FROM Bible WHERE Book = '+libro+' AND Chapter = '+capitulo).fetchall()[0][0] )
    
    for i in range(1,(max+1)):
        versiculos+= '<option value="'+str(i)+'">'+str(i)+'</option>'
    
    data = {'success': 'true', 'versiculos': versiculos}

    return JsonResponse(data)





def ajax (request):
    libro       = request.POST['libro']
    capitulo    = request.POST['capitulo']
    verso       = request.POST['versiculo']
    
    args_dict   = { r'\u':'&#', '?':';', r'{\f2':'', r'{\f1':'' }
                        
    bibles_active   = Bible.objects.filter(activo=1)
    bibles = {}
        
    if int(libro) > 39:
        griego      = sql ("Griego - Sahidica.bblx", libro, capitulo, verso) 
        
        for key in args_dict.keys():
            griego = griego.replace(key, str(args_dict[key]))
        
        interlineal = griego
    else:
        hebreo      = sql ("HOT-ALEPPO.bblx", libro, capitulo, verso)
        for key in args_dict.keys():
            hebreo = hebreo.replace(key, str(args_dict[key]))
        
        interlineal = hebreo

    data = {'success': 'true', 'interlineal': interlineal}

    for bible in bibles_active:
        data["bible"+str(bible.id)] = sql (bible.file, libro, capitulo, verso)
       
    return JsonResponse(data)