from django.forms import ModelForm
from django import forms
from django.contrib.auth.forms import PasswordChangeForm
# from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from blog.models import Blog
from patient.models import HeartVital

class BlogForm(ModelForm):
	class Meta:
		model = Blog
		# fields = '__all__'
		fields = ['title','content']

class HeartVitalForm(ModelForm):
	class Meta:
		model = HeartVital
		exclude = ['user', 'heart_disease', 'prediction_probability']

class EmailChangeForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ['email']

class CustomPasswordChangeForm(PasswordChangeForm):
	class Meta:
		model = User
		fields = ['old_password', 'new_password1', 'new_password2']

