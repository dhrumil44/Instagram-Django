from django import forms
from django.contrib.auth.models import User 
from .models import Picture

# class UserForm(forms.ModelForm):
# 	class Meta:
# 		model = User
# 		fields = [
# 			"name"
# 		]

class PictureForm(forms.ModelForm):
	class Meta:
		model = Picture
		fields = [
			"user",
			"image"
		]

		widgets = {'user': forms.HiddenInput()}

class UserRegForm(forms.ModelForm):
	password = forms.CharField(widget = forms.PasswordInput())
	class Meta:
		model = User
		fields = [
			"username",
			"email",
			"password"
		]

class LoginForm(forms.ModelForm):
	password = forms.CharField(widget = forms.PasswordInput())
	class Meta:
		model = User
		fields = [
			"username",
			"password"
		]