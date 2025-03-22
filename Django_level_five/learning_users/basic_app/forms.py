from django import forms
from django.contrib.auth.models import User
from basic_app.models import UserProfileInfo

class UserForm(forms.ModelForm):
	password=forms.CharField(widget=forms.PasswordInput())

	class Meta():
		model=UserForm
		field=('username','email','password')

class UserProfileInfo(forms.ModelForm):
	class Meta():
		model=UserProfileInfo
		field=('profile_site','profile_pic')