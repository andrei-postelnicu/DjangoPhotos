from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import *
from django.contrib import messages
from .models import Photo

@login_required(login_url='login')
def homePage(request):
    photos = Photo.objects.filter(user=request.user).order_by('-date')
    context = {'photos': photos} 
    return render(request, 'myapp/home.html', context)

@login_required(login_url='login')
def addPhoto(request):
    if request.method == 'POST':
        form = AddPhotoForm(request.POST, request.FILES)
        if form.is_valid():
            photo_instance = form.save(commit=False)
            photo_instance.user = request.user
            photo_instance.save()
            return redirect('home')
    else:
        form = AddPhotoForm()
    
    context = {'form': form}
    return render(request, 'myapp/add_photo.html', context)

@login_required(login_url='login')
def viewPhoto(request, photo_id):
    context = {} 
    photo = get_object_or_404(Photo, id=photo_id)
    if request.user == photo.user:
        context = {'photo': photo} 
    else:
        messages.error(request, 'Error: This is not your photo.')

    return render(request, 'myapp/view_photo.html', context)

@login_required(login_url='login')
def deletePhoto(request, photo_id):
    photo = get_object_or_404(Photo, id=photo_id)
    if request.user == photo.user:
        if request.method == 'POST':
            photo.delete()
            return redirect('home') 
    else:
        messages.error(request, 'Error: This is not your photo.')
    
    return render(request, 'myapp/delete_photo.html')

@login_required(login_url='login')
def settingsPage(request):
    return render(request, 'myapp/settings.html')

@login_required(login_url='login')
def deleteAccount(request):
    if request.method == 'POST':
        current_user = request.user
        current_user.delete()
        messages.success(request, 'The user ' + request.user.username + ' has been deleted.')
        return redirect('login')

    return render(request, 'myapp/delete_account.html')

def registerPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'An account has been created for ' + user + '.')
                return redirect('login')
            
        context = {'form': form}
        return render(request, 'myapp/signup.html', context)

def loginPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.error(request, 'Error: The credentials are incorrect.')
            
        context = {}
        return render(request, 'myapp/login.html', context)

def logoutUser(request):
    logout(request)
    return redirect('login')