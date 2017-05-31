from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegistrationForm(forms.ModelForm):
    username=forms.CharField(max_length=50,required=True, help_text='')
    first_name = forms.CharField(max_length=30, required=False, help_text='')
    last_name = forms.CharField(max_length=30, required=False, help_text='')
    email = forms.EmailField(max_length=254, help_text='Enter a valid email address only.')
    password=forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password', )


class LoginForm(forms.ModelForm):
	# password1=forms.CharField(widget=forms.PasswordInput)
    username=forms.CharField(max_length=50,required=True,help_text='')
    password=forms.CharField(widget=forms.PasswordInput, required=True)
    class Meta:
		model=User
		fields=('username','password')