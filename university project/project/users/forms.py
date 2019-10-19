from .models import CustomUser
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth.hashers import make_password,is_password_usable,check_password

class CustomUserForm(forms.ModelForm):
	class Meta:
		model  = CustomUser
		exclude = ['user', 'admitted', 'password']


class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput( 
        attrs={'class':'form-control', 'placeholder':'Enter username'}))
    password = forms.CharField(widget=forms.PasswordInput( 
        attrs={'class':'form-control', 'placeholder':'Enter Password'}))
    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")
        if username and password :
            user = authenticate(username=username, password=password)
            if not user:
                raise forms.ValidationError("Invalid Log in details. Try Again....")
            if not user.is_active:
                raise forms.ValidationError("This User is no longer active.")
            return super(LoginForm, self).clean(*args, **kwargs)