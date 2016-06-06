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
        #if the client browser does not support datetime-local indexerror will be cast
        try:
            context = {
                "counselors":counselors,
                "counselorerror": False,
                "commandque": adapter.get_scheduled_updates_info()
                }
        except IndexError:
            return redirect("http://google.com")

        return render(request, 'database_manager/db_update_page.html',context)

#Used for choosing the action to perform based on request.POST queryDict
def update_database_post(request):
    def string_to_datetime(dtString):
         dtStringList = dtString.split("T")
         timeList = dtStringList[1].split(":")
         dateList = dtStringList[0].split("-")
         return datetime.datetime(year=int(dateList[0]), month = int(dateList[1]), day = int(dateList[2]), hour=int(timeList[0]), minute = int(timeList[1]))

    #if information is being posted
    if request.method == "POST":
        #if a schedule was requested
        if request.POST["Action"] == "schedule":
            try:
                executionTime = string_to_datetime(request.POST["Datetime"])
            except IndexError:
                return render(request, 'database_manager/browser_error.html')
            for c in request.POST.getlist("Counselor"):
                url = str(c)
                adapter.schedule_update(executionTime,url)
            return redirect("/update/database")

        #if a findnewcounselors command is being scheduled
        elif request.POST["Action"] == "schedule-findnewcmd":
            #if the client browser does not support datetime-local indexerror will be cast
            try:
                executionTime = string_to_datetime(request.POST["Datetime"])
            except IndexError:
                return render(request, 'database_manager/browser_error.html')
            adapter.find_new_counselors(executionTime)
            print executionTime
            print datetime.datetime.now()
            return redirect("/update/database")

        #if a sinle command is being removed
        elif request.POST["Action"] =="delete-cmd":
            commandId = int(request.POST["Id"])
            adapter.delete_scheduled_update(commandId)
            return redirect("/update/database")

        #if all commands is being removed
        elif request.POST["Action"] =="clear-que":
            adapter.clear_all_scheduled_updates()
            return redirect("/update/database")

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
