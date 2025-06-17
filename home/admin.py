from django.contrib import admin
from .models import Book, Bible

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['num', 'name', 'hebreo', 'fonetica']
    list_editable = ['name', 'hebreo', 'fonetica']
    search_fields = ['name', 'hebreo']
    ordering = ['num']
    list_per_page = 25

@admin.register(Bible)
class BibleAdmin(admin.ModelAdmin):
    list_display = ['name', 'label', 'description', 'file', 'visible', 'activo', 'file_exists']
    list_editable = ['label', 'description', 'visible', 'activo']
    list_filter = ['visible', 'activo']
    search_fields = ['name', 'label', 'description']
    readonly_fields = ['file_exists']
    
    def file_exists(self, obj):
        """Indica si el archivo bíblico existe"""
        return obj.is_file_exists()
    file_exists.boolean = True
    file_exists.short_description = 'Archivo existe'