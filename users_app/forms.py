from django import forms
from django.db import connection
plug = connection.cursor()


class sign_in_form(forms.Form):
    email = forms.EmailField(max_length = 254, widget=forms.EmailInput(attrs={'class':'form-control'}))
    password = forms.CharField(widget = forms.PasswordInput(attrs={'class':'form-control'}), max_length = 50, min_length = 8)

class sign_up_form(forms.Form):
    name = forms.CharField(max_length = 20, widget=forms.TextInput(attrs={'class':'form-control'}))
    lastname = forms.CharField(max_length = 20, widget=forms.TextInput(attrs={'class':'form-control'}))
    email = forms.EmailField(max_length = 254, widget=forms.EmailInput(attrs={'class':'form-control'}))
    password = forms.CharField(widget = forms.PasswordInput(attrs={'class':'form-control'}), max_length = 50, min_length = 8)
    conform_password = forms.CharField(widget = forms.PasswordInput(attrs={'class':'form-control'}), max_length = 50, min_length = 8)

class edit_user_form(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}), max_length=20)
    lastname = forms.CharField(max_length = 20, widget=forms.TextInput(attrs={'class':'form-control'}))
    password = forms.CharField(widget = forms.PasswordInput(attrs={'class':'form-control'}), min_length = 8, max_length = 20)

class edit_password_form(forms.Form):
    old_password = forms.CharField(widget = forms.PasswordInput(attrs={'class':'form-control'}), min_length = 8, max_length = 20)
    new_password = forms.CharField(widget = forms.PasswordInput(attrs={'class':'form-control'}), min_length = 8, max_length = 20)
    conform_password = forms.CharField(widget = forms.PasswordInput(attrs={'class':'form-control'}), min_length = 8, max_length = 20)

class forgot_password_email_form(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}), max_length = 30)

class forgot_password_code_form(forms.Form):
    conformation_code = forms.CharField(max_length=6, widget=forms.TextInput(attrs={'class':'form-control'}))

class update_password_form(forms.Form):
    new_password = forms.CharField(widget = forms.PasswordInput(attrs={'class':'form-control'}), min_length = 8, max_length = 20)
    conform_password = forms.CharField(widget = forms.PasswordInput(attrs={'class':'form-control'}), min_length = 8, max_length = 20)

class user_info_form(forms.Form):
    new_password = forms.CharField(widget = forms.PasswordInput(attrs={'class':'form-control'}), min_length = 8, max_length = 20)
