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
    #def replace_values_in_string(text, args_dict):
    #for key in args_dict.keys():
    #    text = text.replace(key, str(args_dict[key]))
    #return text

    return render(request, 'home/index.html', {'books': books, 'n' : range(1,30), 'bibles':bibles, 'bibles_active':bibles_active})

def sql (traduccion, libro, capitulo, verso):
    
    bible = pwd+'/bibles/'+traduccion
    con = sqlite3.connect(bible)
    
    cursorObj = con.cursor()
    texto = cursorObj.execute('select Scripture from Bible WHERE Book = '+libro+' AND Chapter = '+capitulo+' AND Verse = '+verso)
    
    return texto.fetchall()[0][0]


def ajax (request):
    libro       = request.POST['libro']
    capitulo    = request.POST['capitulo']
    verso       = request.POST['verso']
    
    hebreo      = sql ("HOT-ALEPPO.bblx", libro, capitulo, verso)

    args_dict   = { r'\u':'&#', '?':';', r'{\f2':'' }
    
    for key in args_dict.keys():
        hebreo = hebreo.replace(key, str(args_dict[key]))

    bibles_active   = Bible.objects.filter(activo=1)
    bibles = {}
    
    data = {'success': 'true', 'hebreo': hebreo}

    for bible in bibles_active:
        data["bible"+str(bible.id)] = sql (bible.file, libro, capitulo, verso)
       
    return JsonResponse(data)