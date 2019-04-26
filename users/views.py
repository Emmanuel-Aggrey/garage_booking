from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegistrationForm, UserUpdateForm
from mysite.models import Servicings
from django.contrib.auth.models import User
from django.views.generic import CreateView



def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account succesfully created. Please Login')
            return redirect('login')
    else:
        form = UserRegistrationForm()

    return render(request, 'users/register.html', {'form':form})


@login_required
def dashboard(request):
    user = request.user
    user_bookings = Servicings.objects.filter(service_user=request.user).order_by('-service_booked')
    context = {
        'dash_active': True,
        'user': user,
        'services': user_bookings
    }
    return render(request, 'users/dashboard.html', context)



@login_required
def profile(request):
    if request.method == 'POST':
        user_update_form = UserUpdateForm(request.POST, instance=request.user)
        if user_update_form.is_valid():
            user_update_form.save()
            messages.success(request, f'Profile Updated...')
            return redirect('dashboard')
    else:
        user_update_form = UserUpdateForm(instance=request.user)

    context = {
        'dash_active': True,
        'title': 'Profile',
        'user_update_form': user_update_form 
    }
    return render(request, 'users/profile.html', context)

