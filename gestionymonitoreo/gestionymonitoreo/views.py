from django.shortcuts import render

def project_home(request):
    return render(request, 'project_home.html')