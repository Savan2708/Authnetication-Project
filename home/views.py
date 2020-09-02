from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.sessions.models import Session
from .models import Profile


def home(request):
    if request.session.has_key('loggedin'):
        prof = Profile.objects
        return render(request, 'home/home.html', {'prof': prof})
    return redirect('login')


def user_crete(request):
    if request.method == 'POST':
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        if len(fname) < 2:
            messages.error(request, "Your first name to too Short")
            return redirect('signup')

        elif len(lname) < 2:
            messages.error(request, "Your last name to too Short")
            return redirect('signup')

        elif pass1 != pass2:
            messages.error(request, "Password do not match")
            return redirect('signup')

        elif len(pass1) < 8:
            messages.error(request, "Your Password to too Short")
            return redirect('signup')

        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()
        messages.success(request, "User Created")
        return redirect('login')
    else:
        return render(request, 'home/signup.html')


def user_login(request):
    if request.session.has_key('loggedin'):
        return redirect('home')
        
    if request.method == 'POST':
        loginusername = request.POST['loginusername']
        loginpass = request.POST['loginpass']

        user = authenticate(username=loginusername, password=loginpass)

        if user is not None:
            login(request, user)
            messages.success(request, "Loggedin")
            request.session['loggedin'] = True
            return redirect('home')
        else:
            messages.error(request, "invalid username or password")
            return redirect('login')

    return render(request, 'home/login.html')


@login_required(login_url='/login')
def user_logout(request):
    logout(request)
    messages.success(request, "Loggedout")
    return redirect('login')


@login_required(login_url='/login')
def user_edit(request):
    if request.method == 'POST':
        if request.FILES['img'] and request.POST['about'] and request.POST['phnum']:
            profile = Profile()
            profile.img = request.FILES['img']
            profile.about = request.POST['about']
            profile.phnum = request.POST['phnum']
            profile.save()
            return redirect('list')
        else:
            return render(request, "home/intro.html")

    else:
        return render(request, "home/intro.html")


def user_list(request):
    prof = Profile.objects
    return render(request, 'home/list.html', {'prof': prof})
