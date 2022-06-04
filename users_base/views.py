from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .models import User
from .forms import UserForm, ProfileUpdateForm
from django.contrib.auth.forms import AuthenticationForm


def register(request):   

    form_user = UserForm(request.POST or None)

    if form_user.is_valid() :
        user = form_user.save()
       
        
        if "profile_pic" in request.FILES:
            user.profile_pic = request.FILES["profile_pic"]

        user.save()
        login(request, user)
        messages.success(request, "Register successful.")

        return redirect("home")

    context = {
        "form_user": form_user,
    }

    return render (request, "users_base/register.html", context)

def user_login(request):
    form = AuthenticationForm(request, data=request.POST)

    if form.is_valid():
        #? Eğer AuthenticationForm'u kullanmasaydık aşağıdaki kodları yazmak gerikirdi
        #* username = form.cleaned_data("username")
        #* password = form.cleaned_data("password")
        #* user = authenticate(username_username, password=password)

        user = form.get_user()
        if user : 
            messages.success(request, "Login successful.")
            login(request, user)
            return redirect("home")

    return render(request, "users_base/user_login.html", {"form" : form})

def user_logout(request):
    messages.success(request, "You logged out!")
    logout(request)
    return redirect("home")


def user_profile(request,id):
    user = User.objects.get(id=id)
    form = ProfileUpdateForm(instance = user)
    
    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST, request.FILES, instance=user)
        # print("USER" : instance)
        if form.is_valid():           
            form.save()
            login(request, user)
            messages.success(request, "Profile updated.")
            return redirect("home")

    context = {
        "form" : form,
    }
    return render(request, "users_base/user_profile.html", context)

