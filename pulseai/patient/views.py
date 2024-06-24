from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

# from django.contrib.auth.forms import UserCreationForm
# from patient.form import BlogForm, CustomUserCreationForm

def form_demo(request):
      # form = BlogForm()
      # form = UserCreationForm()
      # form = CustomUserCreationForm()
      # context = {
      #     'form' : form
      # }
      # return render(request, 'patient/form.html', context)
      pass

def signup(request):
      if request.method == "POST":
            fn = request.POST.get("f_name")
            ln = request.POST.get("l_name")
            un = request.POST.get("u_name")
            email = request.POST.get("email")
            pwd = request.POST.get("pass")

            if User.objects.filter(username=un).exists():
                  messages.error(request, "Username is already taken")
            elif User.objects.filter(email=email).exists():
                  messages.error(request, "Email is already taken")
            else:
                  user = User.objects.create_user(
                  first_name=fn, last_name=ln, username=un, email=email, password=pwd)
                  user.save()
                  messages.success(request, "Account Created Succesfully")

      return render(request, 'patient/signup.html')

def signin(request):
      if request.method == "POST":
            username = request.POST.get("u_name")
            password = request.POST.get("pass")

            user = authenticate(request, username=username, password=password)
            
            if user is None:
                  messages.error(request, "Invalid Username or Password")
            else:
                  login(request, user)
                  # return render(request, 'blog/index.html')
                  return redirect('home')

      return render(request, 'patient/signin.html')

def signout(request):
      logout(request)
      return redirect('home')
