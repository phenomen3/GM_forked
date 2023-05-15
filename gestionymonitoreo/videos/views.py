from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
from .forms import VideoForm, FolioForm
from .models import Video, Folio
def index(request):
    return render(request, 'videos/index.html')

def buscar(request):
    if request.method == 'POST':
        query = request.POST.get('query')
        results = []
        if query:
            videos = Video.objects.filter(nombre__icontains=query)
            folios = Folio.objects.filter(delito__icontains=query)
            results.extend(list(videos))
            results.extend(list(folios))
        return render(request, 'videos/buscar_resultados.html', {'results': results})
    return render(request, 'videos/buscar.html')

def agregar_video(request):
    if request.method == 'POST':
        video_form = VideoForm(request.POST)
        if video_form.is_valid():
            video_form.save()
            return redirect('videos:buscar')
    else:
        video_form = VideoForm()
    return render(request, 'videos/agregar_video.html', {'video_form': video_form})



def agregar_folio(request, video_id):
    video = get_object_or_404(Video, pk=video_id)
    if request.method == 'POST':
        form = FolioForm(request.POST)
        if form.is_valid():
            folio = form.save(commit=False)
            folio.video = video
            folio.save()
            if request.POST.get("submit") == 'guardar':
                return redirect('videos:index')
            else:
                return redirect('videos:agregar_folio', video_id=video_id)
    else:
        form = FolioForm()
    return render(request, 'videos/agregar_folio.html', {'form': form, 'video': video})



def buscar_resultados(request):
    query = request.GET.get('q')
    resultados_video = Video.objects.filter(Q(nombre__icontains=query) | Q(url__icontains=query))
    resultados_folio = Folio.objects.filter(Q(delito__nombre__icontains=query) | Q(c2__nombre__icontains=query) | Q(c2__direccion__icontains=query) | Q(colonia__nombre__icontains=query))
    context = {
        'resultados_video': resultados_video,
        'resultados_folio': resultados_folio,
        'query': query,
    }
    return render(request, 'videos/buscar_resultados.html', context)
