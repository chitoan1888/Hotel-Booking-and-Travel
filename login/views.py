from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.urls import reverse_lazy
from django.contrib import messages
from .models import Register_tables

# Create your views here.

from .forms import (
    RegistrationForm, 
    EditProfile,
    PasswordChangingForm
)

# from django import template

# register = template.Library()

from django.template.loader import render_to_string


# def index (request):
#     return render(request, 'pages/home.html')

def login_user (request):
    form = RegistrationForm()
    if request.method == 'POST':
        username = request.POST.get('username')
        password2 = request.POST.get('password2')

        user=authenticate(request, username=username, password=password2)
        if user is not None:
            login(request, user)
            return redirect('/profile/')
        else:
            messages.info(request, 'Username or Password is incorrect')
    context = {}
    return render(request, 'login.html', context)

def register (request):
    # if request.user.is_authenticed:
    #     return redirect('trangchu')
    # else:
        form = RegistrationForm()
        if request.method == 'POST':
            form = RegistrationForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account was created for ' + user)
                return redirect('/login')

        context = {'form': form}
        return render(request, 'register.html', context)

def logout_user(request):
    logout(request)
    return redirect('login')

def profile (request):
    args = {'user': request.user}
    return render(request, 'profile.html')

def edit_profile(request):
    if request.method == 'POST':
        form = EditProfile(request.POST)
        form = EditProfile(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            return redirect('/change_success/')
    else:
        form = EditProfile(instance=request.user)
        # args={'form': form}
    return render(request, 'profile.html', {'form': form})



# def change_password(request):
#     if request.method == 'POST':
#         form = PasswordChangeForm(data=request.POST, user=request.user)

#         if form.is_valid():
#             form.save()
#             update_session_auth_hash(request, form.user)
#             return redirect('/homeme/')

#     else:
#         form = PasswordChangeForm(user=request.user)
#         return render(request, 'pages/change_password.html', {'form': form})
#     # return render(request, 'pages/change_password.html', {'form': form})

class PasswordsChangeView(PasswordChangeView):
    from_class = PasswordChangingForm
    # from_class = PasswordChangeForm
    success_url = reverse_lazy('change_success')

def change_success(request):
    return render(request, 'change_success.html', {})

def trangchu (request):
    return render(request, 'trang_chu.html')

