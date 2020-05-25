from django.contrib import admin
from django.urls import path
from home import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name="index"),
    path('ajax/test/', views.ajax, name="ajax"),
    path('ajax/capitulos/', views.capitulos, name="capitulos"),
    path('ajax/versiculos/', views.versiculos, name="versiculos"),
    path('admin/', admin.site.urls),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
