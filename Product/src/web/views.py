from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Project
# Create your views here.

def index(request):
    return render(request,"web/index.html")

def project_list(request):
    projects = Project.objects.all()
    context = {
        "project_list":projects,
        }
    return render(request,"web/project_list.html", context)

def project_detail(request, project_id):
    proj = get_object_or_404(Project, id=project_id)
    context = {
        'project': proj
    }
    return render(request, 'web/project_detail.html', context)
