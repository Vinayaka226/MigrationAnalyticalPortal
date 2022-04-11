from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages

# Create your views here.
def register(request):
	if request.method == 'POST':
		first_name = request.POST['first_name']
		last_name = request.POST['last_name']
		username = request.POST['username']
		email = request.POST['email']
		password1 = request.POST['password1']
		password2 = request.POST['password2']
		is_active = True

		if(password1 == password2):
			if User.objects.filter(username=username).exists():
				messages.error(request,"UserName alredy taken")
				return redirect('Register')
			elif User.objects.filter(email=email).exists():
				messages.error(request,"Email already in use")
				return redirect('Register')
			else:
				user = User.objects.create_user(username=username, password=password1,email=email,first_name=first_name,
					last_name=last_name,is_active=is_active)
				user.save()
				supUsers = User.objects.filter(is_superuser=1)
				supUsers_fname = [item.first_name for item in supUsers]
				message = ",".join(supUsers_fname)
				#sample = ['Vinayaka1', 'Vinayaka2']
				#message = ",".join(sample)
				messages.success(request,message)
				return redirect('Register')
		else:
			messages.error(request, "Password Not Matching! Try again")
			return redirect('Register')
	else:
		return render(request, 'RegisterForm.html')

def login(request):
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']

		user = auth.authenticate(username=username,password=password)

		#print(user.is_superuser)
		#print(user.is_active)
		#print(user.is_staff)

		if user is not None and user.is_superuser and user.is_active and user.is_staff:
			auth.login(request,user)
			return redirect('/mainpage')
		elif user is not None and user.is_staff and user.is_active:
			auth.login(request,user)
			return redirect('/mainpage/')
		elif user is not None and user.is_active:
			auth.login(request,user)
			return redirect('/LLM/mainPage/')

		#if user is not None:
			#auth.login(request,user)
			
			#return redirect('/LLM/mainpage/')

		else:
			messages.info(request,'invalid creadentials')
			return redirect('Login')
	else :
		return render(request, 'login.html')

def logout(request):
	auth.logout(request)
	return redirect('Login')