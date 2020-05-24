import os
from django.shortcuts import render, HttpResponse
from .models import Book
from django.http import JsonResponse

import sqlite3
 
pwd = os.path.dirname(__file__)

def index (request):
    books = Book.objects.all()
    return render(request, 'home/index.html', {'books': books, 'n' : range(1,30)})

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
    
    torah       = sql ("torah.bblx", libro, capitulo, verso)
    oso         = sql ("Biblia del Oso.bbli", libro, capitulo, verso)
    jerusalem   = sql ("Biblia Corona de Jerusaln.bbli", libro, capitulo, verso)

    data = {
        'success': 'true',
        'torah':torah,
        'oso'  :oso,
        'jerusalem':jerusalem,
    }
    return JsonResponse(data)