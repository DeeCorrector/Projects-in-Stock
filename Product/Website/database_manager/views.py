from django.shortcuts import render, redirect

from web.models import Counselor
from .adapter import Adapter, FindNewCounselorsCommand

adapter = Adapter()

def update_database_view(request):
    if not request.user.is_authenticated():
        return redirect('/admin/login/')
    else:
        c = Counselor.objects.all()
        return render(request, 'database_manager/db_update_page.html',{"counselors":c})

def update_all_counselors(request):
    adapter.update_all_now()
    return redirect("/admin/")

def update_specific_counselor(request):
    target = Counselor.objects.get(name=(request.POST["counselorname"]))
    adapter.update_now(target)
    return redirect("/admin/")

def find_new_counselors(request):
    import datetime
    test = FindNewCounselorsCommand(datetime.datetime.now())
    test.execute()
    return redirect("/admin/")
