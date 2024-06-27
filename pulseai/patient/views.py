from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from datetime import datetime, timedelta
import re # For Mobile Number


# from django.contrib.auth.forms import UserCreationForm
# from patient.form import BlogForm, CustomUserCreationForm

from patient.models import HeartVital, Appointment, Visit, Patient
from patient.form import HeartVitalForm
from patient.predict import predict_heart_disease

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

            if not fn or not ln or not un or not email or not pwd:
                  messages.error(request, "All fields are required.")
            # Validate email format
            elif not re.match(r"[^@]+@[^@]+\.[^@]+", email):
                  messages.error(request, "Invalid email format.")
            # Validate username is alphanumeric and between 3 and 30 characters
            elif not re.match(r"^[a-zA-Z0-9]{3,30}$", un):
                  messages.error(request, "Username must be alphanumeric and between 3 and 30 characters.")
            # Validate password strength (minimum 8 characters, at least one letter and one number)
            elif len(pwd) < 8 or not re.search(r"[A-Za-z]", pwd) or not re.search(r"[0-9]", pwd):
                  messages.error(request, "Password must be at least 8 characters long and contain both letters and numbers.")
            # Check if username already exists
            elif User.objects.filter(username=un).exists():
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

            # Validate that no fields are empty
            if not username or not password:
                  messages.error(request, "Both username and password are required.")
            # Validate username format
            elif not re.match(r"^[a-zA-Z0-9]{3,30}$", username):
                  messages.error(request, "Invalid username format.")
            else:
                  user = authenticate(request, username=username, password=password)
                  
                  if user is None:
                        messages.error(request, "Invalid Username or Password")
                  else:
                        login(request, user)
                        return redirect('home')
      return render(request, 'patient/signin.html')

def signout(request):
      logout(request)
      return redirect('home')

@login_required(login_url='signin')
def take_a_test(request):
      context = {}
      today = timezone.now().date()
      # today = datetime.today()
      is_exists = HeartVital.objects.filter(user=request.user, created_at__date=today).count()
      if( is_exists > 0):
            context["error"] = True

      form = HeartVitalForm()
      if request.method == "POST":
            form = HeartVitalForm(request.POST)
            # print(form.data)
            patient = form.save(commit=False)
            # Prediction
            patient_data = {}
            for k, v in form.data.items():
                  patient_data[k] = v
            patient_data.pop('csrfmiddlewaretoken')
            #print(patient_data)
            prediction = predict_heart_disease(patient_data)
            #print(prediction)
            context['prediction'] = prediction

            #save to database
            patient.user = request.user
            patient.heart_disease = prediction.get('class')
            patient.prediction_probability = prediction.get('probability')
            patient.save()

      context['form'] = form
      return render(request, 'patient/take_a_test.html', context)


login_required(login_url='signin')
def appointment(request):
      if request.method == "POST":
            mobile = request.POST.get('mobile')
            date = request.POST.get("date")
            note = request.POST.get("note")
            
            selected_date = datetime.strptime(date, "%Y-%m-%d").date()
            current_date = datetime.now().date()
            max_date = current_date + timedelta(days=7)
            
            if not re.fullmatch(r'\d{10}', mobile):
                  messages.error(request, "Mobile number must be exactly 10 digits.")
            elif selected_date < current_date:
                  messages.error(request, "You cannot choose a past date for the appointment.")
            elif selected_date > max_date:
                  messages.error(request, "You can only book an appointment within the next 7 days.")
            elif Appointment.objects.filter(user=request.user, date=date).exists():
                  messages.error(request, f"Appointment for {date} is already done")
            elif Appointment.objects.filter(date=date).count() >= 20:
                  messages.error(request, f"All the slots of {date} is already booked")
            else:
                  appointment = Appointment(user=request.user, mobile=mobile, date=date, note=note)
                  appointment.save()
                  messages.success(request, "Appointment Booked")
      
      appointments = Appointment.objects.filter(user=request.user).order_by("-date")
      context = {
            'appointments': appointments
      }
      return render(request, 'patient/appointment.html', context)

def update_appointment(request, aid):
      if request.method == "POST":
            mobile = request.POST.get('mobile')
            date = request.POST.get("date")
            note = request.POST.get("note")
            
            selected_date = datetime.strptime(date, "%Y-%m-%d").date()
            current_date = datetime.now().date()
            max_date = current_date + timedelta(days=7)
            
            if not re.fullmatch(r'\d{10}', mobile):
                  messages.error(request, "Mobile number must be exactly 10 digits.")
            elif selected_date < current_date:
                  messages.error(request, "You cannot choose a past date for the appointment.")
            elif selected_date > max_date:
                  messages.error(request, "You can only book an appointment within the next 7 days.")
            elif Appointment.objects.filter(user=request.user, date=date).exclude(id=aid).exists():
                  messages.error(request, f"Appointment for {date} is already done")
            else:
                  appointment = Appointment(id=aid, user=request.user, mobile=mobile, date=date, note=note)
                  appointment.save()
                  messages.success(request, "Appointment Updated")
                  return redirect('appointment')
            
      app = Appointment.objects.get(id=aid)
      context = {
            'appointment': app
      }
      return render(request, 'patient/appointment_update.html', context)

def delete_appointment(request, aid):
      app = Appointment.objects.filter(id=aid).delete()
      if app:
            messages.success(request, "Appointment Deleted")
      else :
            messages.error(request, "Something Went Woring")

      return redirect('appointment')

def profile(request):
      heart_vitals = HeartVital.objects.filter(user=request.user)
      visits = {}
      if Patient.objects.filter(patient=request.user).exists():
            patient = Patient.objects.get(patient=request.user)
            visits = Visit.objects.filter(patient=patient)

      context = {
            'heart_vitals': heart_vitals,
            'visits': visits
      }
      return render(request, 'patient/profile.html', context)