#Imports to render pages, redirect and give error404
from django.shortcuts import render, get_object_or_404, redirect

#
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.template.context_processors import csrf

#importing models
from web.models import Project, Counselor

#importing forms
from .forms import CreateProjectForm, EditCounselorInfoForm

#Overview of all the project
@login_required
def edit_hub(request):
    c = get_object_or_404(Counselor, account_id=request.user.id)
    context = {'counselor': c,}

    return render(request, "edit_info/edit_hub.html", context)

#Lets user create
@login_required
def create(request):
    #getting necessary data
    counselor = get_object_or_404(Counselor, account_id=request.user.id)
    #if the request contains POST info validate it, else no arguments
    form = CreateProjectForm(request.POST or None)


    #if a form is being submitted
    if form.is_valid():
      instance = form.save(commit=False)
      instance.save()
      counselor.projects.add(instance)
      context = {
        'counselor': counselor,
        'CreateForm': form,
        'prj': instance
        }
      return render(request, "edit_info/post_succes.html", context)

    #serves the form
    context = {
      'counselor': counselor,
      'CreateForm': form,
      }
    context.update(csrf(request))
    return render(request, "edit_info/create_project.html", context)

#View for editing already existing projects
@login_required
def edit_project(request, project_id):
    instance = get_object_or_404(Project, id=project_id)
    form = CreateProjectForm(request.POST or None, instance=instance)

    #if a form is being submitted
    if (form.is_valid()) & (request.method == "POST"):
      instance.save()
      context = {
        'prj': instance
        }
      return render(request, "edit_info/post_succes.html", context)

    #serves the form
    context = {
        "form": form,
      }
    context.update(csrf(request))
    return render(request, "edit_info/edit_project.html", context)

#view for deleting an already existing project_id
@login_required
def delete_project(request, project_id):
    instance = get_object_or_404(Project, id=project_id)
    instance.delete()
    return redirect('edit hub')

#View for editing already existing projects
@login_required
def edit_counselor(request, counselor_id):
    instance = get_object_or_404(Counselor, id=counselor_id)
    form = EditCounselorInfoForm(request.POST or None, instance=instance)

    #if a form is being submitted
    if (form.is_valid()) & (request.method == "POST"):
      instance.save()
      return redirect('edit hub')

    #serves the form
    context = {
        "counselor":instance,
        "form": form,
      }
    context.update(csrf(request))
    return render(request, "edit_info/edit_counselor.html", context)

# Login Views:
#Displays login screen
def login(request):
    if not request.user.is_authenticated():
        context = {"bad_login": False}
        #security stuff
        context.update(csrf(request))
        return render(request, 'edit_info/login.html', context)
    else:
        return redirect('edit hub')

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

        #On succesful login redirect to edithub
        return redirect('edit hub')
    else:
        #if user cant be authenticated render invalid login
        return render(request, 'edit_info/login.html', {"bad_login": True})

#logs user out
def logout(request):
    auth.logout(request)
    #after logout redirect to index
    return redirect('index')
