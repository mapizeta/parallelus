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
    cursorObj.execute('SELECT Scripture FROM Bible WHERE Book = ? AND Chapter = ? AND Verse = ?', 
                     (libro, capitulo, verso))
    result = cursorObj.fetchall()
    con.close()
    
    return result[0][0] if result else ""

def capitulos(request):
    libro   = request.POST.get('libro')
    if not libro:
        return JsonResponse({'success': 'false', 'error': 'Libro requerido'})
        
    bible   = pwd+'/bibles/Biblia del Oso.bbli'
    con     = sqlite3.connect(bible)
    cursorObj = con.cursor()
    capitulos = '<option value="">Capítulo</option>'

    cursorObj.execute('SELECT MAX(DISTINCT Chapter) FROM Bible WHERE Book = ?', (libro,))
    max_chapter = cursorObj.fetchall()[0][0]
    con.close()
    
    if max_chapter:
        for i in range(1, int(max_chapter) + 1):
            capitulos += f'<option value="{i}">{i}</option>'
    
    data = {'success': 'true', 'capitulos': capitulos}
    return JsonResponse(data)

def versiculos(request):
    libro       = request.POST.get('libro')
    capitulo    = request.POST.get('capitulo')
    
    if not libro or not capitulo:
        return JsonResponse({'success': 'false', 'error': 'Libro y capítulo requeridos'})
        
    bible   = pwd+'/bibles/Biblia del Oso.bbli'
    con     = sqlite3.connect(bible)
    cursorObj = con.cursor()
    versiculos = '<option value="">Selecciona Verso</option>'

    cursorObj.execute('SELECT MAX(DISTINCT Verse) FROM Bible WHERE Book = ? AND Chapter = ?', 
                     (libro, capitulo))
    max_verse = cursorObj.fetchall()[0][0]
    con.close()
    
    if max_verse:
        for i in range(1, int(max_verse) + 1):
            versiculos += f'<option value="{i}">{i}</option>'
    
    data = {'success': 'true', 'versiculos': versiculos}
    return JsonResponse(data)

def ajax (request):
    libro       = request.POST.get('libro')
    capitulo    = request.POST.get('capitulo')
    verso       = request.POST.get('versiculo')
    
    if not all([libro, capitulo, verso]):
        return JsonResponse({'success': 'false', 'error': 'Todos los campos son requeridos'})
    
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
        try:
            data["bible"+str(bible.id)] = sql (bible.file, libro, capitulo, verso)
        except Exception as e:
            data["bible"+str(bible.id)] = f"Error: {str(e)}"
       
    return JsonResponse(data)