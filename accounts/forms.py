# from django import forms
# from django.contrib.auth.models import User

# class UserRegisterForm(forms.ModelForm):
#     password = forms.CharField(widget=forms.PasswordInput)

#     class Meta:
#         model = User
#         fields = ['username', 'email', 'password']

# My working codes

# from django import forms
# from django.contrib.auth.models import User
# from .models import UserProfile

# class SignUpForm(forms.ModelForm):
#     class Meta:
#         model = User
#         fields = ['username', 'password', 'email']

#     password = forms.CharField(widget=forms.PasswordInput())

# class ProfileForm(forms.ModelForm):
#     class Meta:
#         model = UserProfile
#         fields = ['skills', 'location']

from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
	email = forms.EmailField()
	phone_no = forms.CharField(max_length = 20)
	first_name = forms.CharField(max_length = 20)
	last_name = forms.CharField(max_length = 20)
	class Meta:
		model = User
		fields = ['username', 'email', 'phone_no', 'password1', 'password2']

