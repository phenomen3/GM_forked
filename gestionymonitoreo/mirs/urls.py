from django.urls import path
from . import views

urlpatterns = [
    path('', views.mirs_home, name='mirs_home'),
    # path('folios/', views.folios_home, name='folios_home'),
    # path('noticias/', views.noticias_home, name='noticias_home'),
    path('noticias/ingresar/', views.noticias_form, name='noticias_form'),
    path('noticias/buscar/', views.noticias_search, name='noticias_search'),
]