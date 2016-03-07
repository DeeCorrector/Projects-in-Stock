from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Project
# Create your views here.
def project_list(request):
    projects = Project.objects.all()
    context = {
        "project_list":projects,
        }

    return render(request,"web/project_list.html",context)
