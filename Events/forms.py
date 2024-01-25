from django import forms 
   
# import GeeksModel from models.py 
from .models import RegisteredUser
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from django.contrib.auth.models import User
   
# create a ModelForm 
class UserRegisterForm(ModelForm):
    

    class Meta: 
        model = RegisteredUser
        fields = ['name', 'email', 'phone_number']

class UserSignUpForm(forms.ModelForm):
	username = forms.CharField(widget=forms.widgets.TextInput(attrs = {"placeholder" : "Full name","class" : "input-fields"}),
	 max_length=30, required=True, label = "Full Name")
	email = forms.CharField(widget=forms.EmailInput(attrs = {"placeholder" : "Email","class" : "input-fields"}), max_length=100, required=True,label= "Email")
	password = forms.CharField(widget=forms.PasswordInput(attrs = {"placeholder" : "password","class" : "input-fields"}), label = "Password.")
	

	class Meta:

		model = User
		fields = ('username', 'email', 'password')
            
class UsersLoginForm(forms.ModelForm):
	username = forms.CharField(widget=forms.widgets.TextInput(attrs = {"placeholder" : "Full name","class" : "input-fields"}),
	 max_length=30, required=True, label = "Full Name")
	password = forms.CharField(widget=forms.PasswordInput(attrs = {"placeholder" : "password","class" : "input-fields"}), label = "Password.")

	class Meta:
		model = User
		fields = ('username', 'password')