from django.shortcuts import render, redirect
from web.models import Counselor
from .adapter import Adapter, CommandFactory
import datetime

adapter = Adapter()

def update_database_view(request):
    #check for authorization
    if not request.user.is_authenticated():
        return redirect('/admin/login/')
    else:
        counselors = Counselor.objects.all()
        context = {
            "counselors":counselors,
            "counselorerror": False
        }

        return render(request, 'database_manager/db_update_page.html',context)

#Used for choosing the action to perform based on request.POST queryDict
def update_database_post(request):
    #if information is being posted
    if request.method == "POST":
        #if a schedule was requested
        if request.POST["Action"] == "schedule":
            #convert queryDict to python Dict
            #if no counselors was selected return to page
            print request.POST
            for c in request.POST["Counselor"].iteritems():
                print c

            return redirect("http://google.com")

def update_all_counselors(request):
    adapter.update_all_now()
    return redirect("/admin/")

def update_specific_counselor(request):
    target = Counselor.objects.get(name=(request.POST["counselorname"]))
    adapter.update_now(target)
    return redirect("/admin/")

def find_new_counselors(request):
    cmdFactory = CommandFactory()
    cmd = cmdFactory.new_FindNewCounselorsCommand(datetime.datetime.now())
    cmd.execute()
    return redirect("/admin/")
