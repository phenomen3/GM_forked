from django.shortcuts import render, redirect
from .forms import NoticiaForm
from .models import Noticia
from django.db.models import Q

from django.contrib.auth.decorators import login_required

#@login_required


def mirs_home(request):
    return render(request, 'mirs_home.html')

@login_required
def noticias_form(request):
    if request.method == 'POST':
        form = NoticiaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('mirs_home')
    else:
        form = NoticiaForm()
    
    context = {'form': form}
    return render(request, 'mirs/noticias_form.html', context)

def noticias_search(request):
    query = request.GET.get('q')
    resultados = []
    
    if query:
        resultados = Noticia.objects.filter(
            Q(titulo__icontains=query) | Q(contenido__icontains=query)
        ).order_by('-fecha')[:10]
    
    context = {'resultados': resultados}
    return render(request, 'mirs/noticias_form.html', context)