from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Profile
from .forms import ProfileForm
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, 'home.html')  # Ensure you have a home.html template

def register(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already taken")
            return redirect('register')
        else:
            user = User.objects.create_user(username=username, password=password)
            user.save()
            Profile.objects.create(user=user)  # Creating profile upon registration
            messages.success(request, "Registration successful!")
            return redirect('login')
    return render(request, 'register.html')

def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('profile', username=user.username)  # Redirect to the user's profile after login
        else:
            messages.error(request, "Invalid credentials")
            return redirect('login')
    return render(request, 'login.html')

def logout_user(request):
    logout(request)
    messages.success(request, "Logged out successfully")
    return redirect('login')

from django.http import HttpResponseForbidden

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from django.contrib import messages
from .models import Profile
from .forms import ProfileForm
import json

@login_required
def edit_profile(request, username):
    # Ensure that the logged-in user is editing their own profile
    if request.user.username != username:
        return HttpResponseForbidden("You are not allowed to edit this profile.")

    # Fetch or create the profile for the logged-in user
    profile, created = Profile.objects.get_or_create(user=request.user)

    if request.method == "POST":
        form = ProfileForm(request.POST, request.FILES, instance=profile)

        if form.is_valid():
            # Custom validation for social_links field to ensure valid JSON
            social_links = form.cleaned_data.get('social_links')
            try:
                if social_links:  # If social_links is not empty, validate JSON
                    json.loads(social_links)  # Try to parse the JSON
            except (TypeError, json.JSONDecodeError):
                form.add_error('social_links', 'Invalid JSON format for social links.')

            if form.errors:
                return render(request, 'edit_profile.html', {'form': form})

            # Save the profile if all validation passes
            form.save()
            messages.success(request, "Profile updated successfully!")
            return redirect('profile', username=request.user.username)
    else:
        form = ProfileForm(instance=profile)

    return render(request, 'edit_profile.html', {'form': form})

def logout_user(request):
    logout(request)
    messages.success(request, "Logged out successfully")
    return redirect('home')


def view_profile(request, username):
    user = get_object_or_404(User, username=username)
    profile, created = Profile.objects.get_or_create(user=user)
    return render(request, 'view_profile.html', {
        'profile': profile,
        'room_background': profile.room_background
    })
