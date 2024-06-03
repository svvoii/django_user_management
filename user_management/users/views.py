from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm


def login_user(request):
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			return redirect('home')
		else:
			messages.error(request, 'Invalid username or password')
			return redirect('users:login')
	else:
		return render(request, 'users/login.html', {})

def logout_user(request):
	# if requestmethod == 'POST':
	logout(request)
	messages.success(request, 'You have been logged out.')
	return redirect('home')

def register_user(request):
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password1')
			user = authenticate(username=username, password=password)
			login(request, user)
			messages.success(request, f'Registration successful. Account created for {username}')
			return redirect('home')
	else:
		form = UserCreationForm()
	return render(request, 'users/register.html', {'form': form})
