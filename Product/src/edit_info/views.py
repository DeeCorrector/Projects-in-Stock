from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import auth
from django.template.context_processors import csrf
from web.models import Project, Counselor

# Create your views here.

def edit_hub(request, counselor_id):
    c = get_object_or_404(Counselor, id=counselor_id)
    context = {
             'counselor': c,
    }
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
        return redirect('logged_in')
    else:
        #if user cant be authenticated redirect to invalid login
        return redirect('invalid_login')

#logs user out
def logout(request):
    auth.logout(request)
    return render(request, 'edit_info/logged_out.html', {})

#for testing, displays a succesful login screen
def logged_in(request):
    return render(request, 'edit_info/logged_in.html', {"username": request.user.username})

#displays the login screen with an error
def invalid_login(request):
    return render(request, 'edit_info/login.html', {"bad_login": True})
