from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages

from ..models.location import Location
from ..forms import VolunteerSignupForm, CompanySignupForm
from ..models.volunteer import Volunteer
from ..models.company import Company
from django.contrib.auth.forms import AuthenticationForm

def signup_selection_view(request):
    return render(request, 'pages/auth_selection.html')

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f"Welcome, {username}!")
                return redirect('/')  # Redirect to your home page
            else:
                messages.error(request, "Invalid username or password")
        else:
            messages.error(request, "Invalid username or password")
    else:
        form = AuthenticationForm()
    return render(request, 'pages/login.html', {'form': form})

def volunteer_signup_view(request):
    if request.method == 'POST':
        user_form = VolunteerSignupForm(request.POST, request.FILES)
        if user_form.is_valid():
            user = user_form.save(commit=False)
            user.save()
            volunteer = Volunteer.objects.create(
                user=user,
                name=user_form.cleaned_data.get('name'),
                surname=user_form.cleaned_data.get('surname'),
                sex=user_form.cleaned_data.get('sex'),
                birthday=user_form.cleaned_data.get('birthday'),
                description=user_form.cleaned_data.get('description'),
                phone_number=user_form.cleaned_data.get('phone_number'),
                avatar=user_form.cleaned_data.get('avatar'),
            )
            # Save skills
            volunteer.skills.set(user_form.cleaned_data.get('skills'))
            user = authenticate(username=user_form.cleaned_data.get('username'), password=user_form.cleaned_data.get('password1'))
            if user is not None:
                login(request, user)
                messages.success(request, "Volunteer account created successfully.")
                return redirect('/')
            else:
                messages.error(request, "Authentication failed.")
    else:
        user_form = VolunteerSignupForm()
    return render(request, 'pages/volunteer_signup.html', {'user_form': user_form})

def company_signup_view(request):
    if request.method == 'POST':
        user_form = CompanySignupForm(request.POST, request.FILES)
        if user_form.is_valid():
            user = user_form.save(commit=False)
            user.save()
            location = Location.objects.create(
                country=user_form.cleaned_data.get('country'),
                city=user_form.cleaned_data.get('city'),
                address=user_form.cleaned_data.get('address')
            )
            Company.objects.create(
                user=user,
                name=user_form.cleaned_data.get('name'),
                phone_number=user_form.cleaned_data.get('phone_number'),
                description=user_form.cleaned_data.get('description'),
                mission=user_form.cleaned_data.get('mission'),
                location=location,
                avatar=user_form.cleaned_data.get('avatar')
            )
            user = authenticate(username=user_form.cleaned_data.get('username'), password=user_form.cleaned_data.get('password1'))
            if user is not None:
                login(request, user)
                messages.success(request, "Company account created successfully.")
                return redirect('/')
            else:
                messages.error(request, "Authentication failed.")
    else:
        user_form = CompanySignupForm()
    return render(request, 'pages/company_signup.html', {'user_form': user_form})

def logout_view(request):
    logout(request)
    return redirect('wfutureAPI:login')  # Redirect to login page after logout