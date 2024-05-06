from django.shortcuts import render, redirect,HttpResponse,get_object_or_404
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .forms import CreateUserForm,CreateContactForm,LoginForm
from django.urls import reverse
from .email_utils import send_signup_email
def home(request):
    return render(request,'HOME.html')
def check_user_exists(username):
    try:
        user = Profile.objects.get(username=username)
        return user
    except Profile.DoesNotExist:
        return None
def register(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            user_email = user.email 
            send_signup_email(user_email)
            return redirect('sign_in')
    else:
        form = CreateUserForm()

    return render(request, 'register.html', {'form': form})

def sign_in(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        print("IM here")
        if form.is_valid():
            print("Valid")
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            # Check if the user exists
            user = check_user_exists(username)

            if user and user.password == password:  # Replace with secure password validation
                # User exists and password is correct, perform login operation
                # (e.g., set user in the session and redirect to dashboard)
                # ...
                return redirect('profile', user_id=user.id)
            else:
                print('Not valid')
    else:
        
        form = LoginForm()

    return render(request, 'sign_in.html', {'form': form})


def profile(request,user_id):
    user = Profile.objects.get(pk= user_id)
    contacts = UserContact.objects.filter(profile=user)

    return render(request, 'profile.html', {'user': user, 'contacts': contacts})

def update(request,contact_id,user_id):
    contact = get_object_or_404(UserContact, pk=contact_id)
    if request.method == 'POST':
        form = CreateContactForm(request.POST, instance=contact)
        if form.is_valid():
            form.save()
            return redirect('profile', user_id=user_id)
    else:
        form = CreateContactForm(instance=contact)

    return render(request, 'update.html', {'form': form, 'contact': contact, 'user_id': user_id})
def useradd(request,user_id):
    user = Profile.objects.get(pk=user_id)

    if request.method == 'POST':
        form = CreateContactForm(request.POST)
        if form.is_valid():
            contact = form.save(commit=False)
            contact.profile = user
            contact.save()
            return redirect('profile', user_id=user.id)
    else:
        form = CreateContactForm()

    return render(request, 'useradd.html', {'form': form})
def delete(request,user_id,contact_id):
    contact = get_object_or_404(UserContact, pk=contact_id)
    contact.delete()
    return redirect('profile', user_id=user_id)

