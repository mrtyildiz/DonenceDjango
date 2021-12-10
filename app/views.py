from django.contrib.auth import forms
from django.db.models import query
from django.db.models.query import RawQuerySet
from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage
import mimetypes

from .models import footer
from .models import teacher
from .models import ebeveyn
from .models import Course
from .models import Galery
from .models import Blogs
from .models import Future
def index(request):
    if request.method == 'POST':
        user = auth.authenticate(username=request.POST['ebeveynName'],password=request.POST['Password'])
        if user is not None:
            return redirect('/')
        else:
            auth.login(request, user)
            return render(request, 'deneme.html')
            

    if request.method == 'POST':
        Parent = ebeveyn(ebeveynName=request.POST['ebeveynName'],studentName=request.POST['studentName'],Email=request.POST['Email'],Password=request.POST['Password'])
        Parent.save()
        redirect('/')
        

    else:
        foot = footer.objects.all()
        teac = teacher.objects.all()
        cour = Course.objects.all()
        Gal = Galery.objects.all()
        Blo = Blogs.objects.all()
        Futures = Future.objects.all()
        context = { 'foot' : foot, 'teac' : teac, 'cour' : cour, 'Gal' : Gal, 'Blo' : Blo, 'Futures' : Futures}
        return render(request, 'index.html', context)

def about(request):
    if request.method == 'POST':
        Parent = ebeveyn(ebeveynName=request.POST['ebeveynName'],studentName=request.POST['studentName'],Email=request.POST['Email'],Password=request.POST['Password'])
        Parent.save()
        return redirect('/about')
    else:
        foot = footer.objects.all()
        Futures = Future.objects.all()
        context = { 'foot' : foot, 'Futures' : Futures }
        return render(request, 'about.html', context)

def Teacher(request):
    if request.method == 'POST':
        Parent = ebeveyn(ebeveynName=request.POST['ebeveynName'],studentName=request.POST['studentName'],Email=request.POST['Email'],Password=request.POST['Password'])
        Parent.save()
        return redirect('/Teacher')
    else:
        foot = footer.objects.all()
        teac = teacher.objects.all()
        context = { 'foot' : foot, 'teac' : teac}
        return render(request, 'teacher.html', context)

def Courses(request):
    if request.method == 'POST':
        Parent = ebeveyn(ebeveynName=request.POST['ebeveynName'],studentName=request.POST['studentName'],Email=request.POST['Email'],Password=request.POST['Password'])
        Parent.save()
        return redirect('/Courses')
    else:
        foot = footer.objects.all()
        cour = Course.objects.all()
        context = { 'foot' : foot, 'cour' : cour }
        return render(request, 'courses.html', context)
def Pricing(request):
    if request.method == 'POST':
        Parent = ebeveyn(ebeveynName=request.POST['ebeveynName'],studentName=request.POST['studentName'],Email=request.POST['Email'],Password=request.POST['Password'])
        Parent.save()
        return redirect('/Pricing')
    else:
        foot = footer.objects.all()
        context = { 'foot' : foot }
        return render(request, 'pricing.html', context)

def Blog(request):
    if request.method == 'POST':
        Parent = ebeveyn(ebeveynName=request.POST['ebeveynName'],studentName=request.POST['studentName'],Email=request.POST['Email'],Password=request.POST['Password'])
        Parent.save()
        return redirect('/Blog')
    else:
        foot = footer.objects.all()
        Blo = Blogs.objects.all()
        context = { 'foot' : foot, 'Blo' : Blo }
        return render(request, 'blog.html', context)

def Contact(request):
    pass
def deneme(request):
    user = auth.authenticate(username=request.POST['username'],password=request.POST['password'])
    if user is not None:
        auth.login(request, user)
        return render(request, 'deneme.html')
    else:
        return render(request, 'index.html')
    
