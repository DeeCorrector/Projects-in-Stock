from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Project
# Create your views here.
def project_list(request):
    return HttpResponse("<h1>You're on the project_list view</h1>")
