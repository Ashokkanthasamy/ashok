from django.shortcuts import render, redirect, get_object_or_404
from .models import Person
from .forms import PersonForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from .forms import SignUpForm, SignInForm
from django.contrib import messages

def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Account created successfully! Welcome to Titan.')
            return redirect('signin')  # redirect to home after signup
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

def logout_view(request):
    logout(request)
    messages.info(request, 'You have been logged out.')
    return redirect('signin')

def signin_view(request):
    if request.method == 'POST':
        form = SignInForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, 'Welcome back, {user.username}!')
            return redirect('home')  # redirect to home after login
    else:
        form = SignInForm()
    return render(request, 'signin.html', {'form': form})


@login_required(login_url='signin')
# Home page
def home_view(request):
    return render(request, 'home.html')

@login_required(login_url='signin')
# Analytics page
def analytics_view(request):
    return render(request, 'analytics.html')

@login_required(login_url='signin')
# Settings page
def settings_view(request):
    return render(request, 'settings.html')

@login_required(login_url='signin')
# Profile page
def profile_view(request):
    return render(request, 'profile.html')

@login_required(login_url='signin')
def dashboard(request):
    data = Person.objects.all()
    return render(request, 'dashboard1.html', {'data': data})

def person_create(request):
    if request.method == "POST":
        form = PersonForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Person added successfully!')
        else:
            messages.error(request, 'Error adding person. Please check the form.')
    return redirect('dashboard')

def person_update(request, pk):
    person = get_object_or_404(Person, pk=pk)
    if request.method == "POST":
        form = PersonForm(request.POST, instance=person)
        if form.is_valid():
            form.save()
            messages.success(request, 'Person updated successfully!')
        else:
            messages.error(request, 'Error updating person. Please check the form.')
    return redirect('dashboard')

def person_delete(request, pk):
    person = get_object_or_404(Person, pk=pk)
    if request.method == "POST":
        person.delete()
        messages.success(request, 'Person deleted successfully!')
    return redirect('dashboard')