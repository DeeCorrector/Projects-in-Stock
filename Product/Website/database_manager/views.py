from django.shortcuts import render, redirect
from web.models import Counselor
from .adapter import Adapter, FindNewCounselorsCommand
import datetime

adapter = Adapter()

def update_database_view(request):
    if not request.user.is_authenticated():
        return redirect('/admin/login/')
    else:
        counselors = Counselor.objects.all()
        context = {
            "counselors":counselors
        }
        return render(request, 'database_manager/db_update_page.html',context)

def update_all_counselors(request):
    adapter.update_all_now()
    return redirect("/admin/")

def update_specific_counselor(request):
    target = Counselor.objects.get(name=(request.POST["counselorname"]))
    adapter.update_now(target)
    return redirect("/admin/")

def find_new_counselors(request):
    test = FindNewCounselorsCommand(datetime.datetime.now())
    test.execute()
    return redirect("/admin/")
