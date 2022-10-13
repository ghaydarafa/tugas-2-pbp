import datetime
from todolist.models import Task
from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponseNotFound
from django.urls import reverse
from .forms import CreateTaskForm
from django.core import serializers
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@login_required(login_url='/todolist/login/')
def show_todolist(request):
    # data = Task.objects.filter(user = request.user)
    username = request.user
    context = {
        # 'data_task': data,
        'username': username,
    }
    return render(request, "todolist.html", context)

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Akun telah berhasil dibuat!')
            return redirect('todolist:login')
    
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user) # melakukan login terlebih dahulu
            response = HttpResponseRedirect(reverse("todolist:show_todolist")) # membuat response
            response.set_cookie('last_login', str(datetime.datetime.now())) # membuat cookie last_login dan menambahkannya ke dalam response
            return response
        else:
            messages.info(request, 'Username atau Password salah!')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('todolist:login'))
    response.delete_cookie('last_login')
    return response

def create_task(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = CreateTaskForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            title = form.cleaned_data['title']
            description = form.cleaned_data['description']
            task = Task(user=request.user, title=title, description=description)
            task.save()
            return HttpResponseRedirect('/todolist')
            
    # if a GET (or any other method) we'll create a blank form
    else:
        form = CreateTaskForm()

    return render(request, 'createtask.html', {'form': form})

def delete_task(request, id):
    task = Task.objects.get(id=id)
    task.delete()
    return HttpResponseRedirect('/todolist')

def check_task(request, i):
    task = Task.objects.get(id=i)
    if task.is_finished == True:
        task.is_finished = False
    else:
        task.is_finished = True
    task.save()
    return HttpResponseRedirect('/todolist')

@login_required(login_url='/todolist/login/')
def show_json(request):
    data = Task.objects.filter(user = request.user)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def add_task(request):
    if request.method == 'POST':
        title = request.POST.get("title")
        description = request.POST.get("description")
        user = request.user

        new_task = Task(user=user,title=title, description=description)
        new_task.save()

        return HttpResponse(b"CREATED", status=201)

    return HttpResponseNotFound()

@csrf_exempt
def delete_ajax(request, i):
    if request.method == "DELETE":
        task = Task.objects.get(id=i)
        task.delete()
    return HttpResponse(b"DELETE")