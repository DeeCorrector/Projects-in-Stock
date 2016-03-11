from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.template.context_processors import csrf
from web.models import Project, Counselor

@login_required
def edit_hub(request, counselor_id):
    c = get_object_or_404(Counselor, id=counselor_id)
    context = {'counselor': c, 'username': request.user.username,}
    print(c.name)
    return render(request, "edit_info/edit_hub.html", context)

# Login Views:
#Displays login screen
def login(request):
    context = {"bad_login": False}
    context.update(csrf(request))
    return render(request, 'edit_info/login.html', context)

#authenticates login request
def auth_login(request):
    #gets user login input from the post request
    username = request.POST['username']
    password = request.POST['password']
    #authenticates user, if not authenticated returns None
    user = auth.authenticate(username=username, password=password)
    if user is not None:
        #login user
        auth.login(request, user)
        #redirect to logged_in url.

        #Fetch real counselor id here!
        c_id = 2
        return redirect('edit hub', counselor_id=c_id)
    else:
        #if user cant be authenticated redirect to invalid login
        return render(request, 'edit_info/login.html', {"bad_login": True})

#logs user out
def logout(request):
    auth.logout(request)
    return redirect('index')
