from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from web.models import Project, Counselor

# Create your views here.

def edit_hub(request, counselor_id):
    c = get_object_or_404(Counselor, id=counselor_id)
    context = {
            "counselor" : c,
    }
    return render(request, "edit_info/edit_hub.html", context)
