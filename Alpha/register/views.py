from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import logout, authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth.decorators import login_required

# Create your views here.
def signup(request):

	if request.method == 'POST':
		u_name = request.POST.get('username')
		email = request.POST.get('email')
		pass1 = request.POST.get('password1')
		pass2 = request.POST.get('password2')

		if pass1 != pass2: 
			return HttpResponse("Your password does not match")

		else:
			new_user = User.objects.create_user(u_name,email,pass1)
			new_user.save()
			return redirect('home')



	return render(request, 'register/signup.html', {'title':'Sign Up'})

def login(request):

	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')

		user = authenticate(request, username = username, password = password)

		if user is not None:
			auth_login(request,user)
			return redirect('home')

		else:
			return HttpResponse("Your login credentials are wrong!!!")

	return render(request, 'register/login.html', {'title' : 'Login'})

@login_required
def profile(request):
	return render(request, 'register/profile.html',{'title':'profile'})
