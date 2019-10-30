from django.shortcuts import render, redirect
from .forms import CustomUserForm, LoginForm
import string
import random
from django.contrib.auth.models import User
from .models import CustomUser
from django.contrib.auth import authenticate, login, get_user_model, logout
from django.contrib.auth.decorators import login_required

# Create your views here.
def register(request):
	if request.method == 'POST':
		form = CustomUserForm(request.POST or None. request.FILES or None)
		if form.is_valid():
			username = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(12))
			password = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(12))
			email = form.cleaned_data['email']
			user = User.objects.create_user(username=username, password=password, email=email)
			data = form.save(commit=False)
			data.user = user
			data.password = password
			data.save()
			print(data)
			context = {'username':username, 'password':password}
			return render(request, 'users/register_success.html', context)

			# print('yeah', generate)
	else:
		form = CustomUserForm()
	context = {'form':form}
	return render(request, 'users/register.html', context)


def login_view(request):
	if request.method == 'POST':
		form = LoginForm(request.POST or None)
		if form.is_valid():
			username  = form.cleaned_data.get("username")
			password  = form.cleaned_data.get("password")
			user = authenticate(username=username, password=password)
			if user is not None:
			 	if user.is_active:
			 		login(request, user)
			 		return redirect('users:profile')
			 	else:
			 		return HttpResponse('Disabled account')
			else:
				return HttpResponse('Invalid login')
	else:
		form = LoginForm()
	context = {"form": form}
	return render(request, "users/login.html", context)


@login_required(login_url='/users/login/')
def profile(request):
	qs = CustomUser.objects.get(user = request.user)
	context = {'qs':qs}
	return render(request, 'student/index.html', context)


def logout_view(request):
	logout(request)
	return render(request, "users/logout.html", {})