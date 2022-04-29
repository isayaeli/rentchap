from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm


class loginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'User Name'}), label='Username')
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Password'}), label='Password')


class registerForm(UserCreationForm):
	username = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'User Name'}), required=True, label='Username')
	email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder':'Email'}),required=True, label='Email')
	first_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'First Name'}),required=True, label='First Name')
	last_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Last Name'}),required=True, label='Last Name')
	password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Password'}),required=True, label='Password')
	password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Confirm Password'}),required=True, label='Password')


	class Meta:
		model = User
		fields = ('username','email','first_name','last_name','password1','password2')

		def save(self, commit=True):
			user = super(registerForm, self).save(commit=False)
			user = self.cleaned_data['email']
			if commit:
				user.save()
			return user