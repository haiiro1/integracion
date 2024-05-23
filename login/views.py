from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm, CustomAuthenticationForm
from django.contrib.admin.views.decorators import staff_member_required
from .models import CustomUser


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(' crud/login.html')
    else:
        form = CustomUserCreationForm()
    return render(request, 'crud/signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('app/inicio.html')
    else:
        form = CustomAuthenticationForm()
    return render(request, 'crud/login.html', {'form': form})

@staff_member_required
def register_staff(request):
    if request.method == 'POST':
        form = StaffUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_staff = True
            user.save()
            return redirect('crud/login.html')
    else:
        form = StaffUserCreationForm()
    return render(request, 'crud/register_staff.html', {'form': form})