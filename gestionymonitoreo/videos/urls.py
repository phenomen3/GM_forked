from django.urls import path
from . import views

app_name = 'videos'
urlpatterns = [
    path('', views.index, name='index'),
    path('agregar_video/', views.agregar_video, name='agregar_video'),
    path('agregar_folio/<int:video_id>/', views.agregar_folio, name='agregar_folio'),
    path('buscar/', views.buscar, name='buscar'),
    path('buscar_resultados/', views.buscar_resultados, name='buscar_resultados'),
]