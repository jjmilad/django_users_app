from django.shortcuts import render
from django.db import connection
from django.http import HttpResponseRedirect
from django.urls import reverse
import datetime
import random
from .forms import sign_in_form, sign_up_form, edit_user_form, edit_password_form, forgot_password_code_form, update_password_form, forgot_password_email_form
plug = connection.cursor()
from django.conf import settings
import bcrypt
import json
import requests
from .models import users
import re


#signed_in_page
def sign_in_page(request):
    data = {}
    form = sign_in_form(request.POST)
    if form.is_valid() and request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        redirect = str(request.session.get('redirect'))
        result = users.objects.get(email=email)
        if result:
            db_password = result.password
            print(db_password)
            if bcrypt.checkpw(password.encode('utf-8'), "$2b$12$BTGwYDRqItR5bzjhAOH3mOlgs/M78JZIMPU44C4KpTwiZPgjZtV.W".encode('utf-8')):
                request.session['user'] = result.id
                if redirect == 'None':
                    redirect = 'account'
                elif redirect:
                    del(request.session['redirect'])
                return HttpResponseRedirect(redirect+'?success=sign_in')
        return HttpResponseRedirect(reverse('sign_in')+'?error=unkown')
    data['sign_in_form'] = form
    return render(request, 'users_app/sign_in.html', data)

#sign_up_page
def sign_up_page(request):
    data = {}
    form = sign_up_form(request.POST)
    if request.method == 'POST' and form.is_valid():
        name = request.POST.get('name')
        lastname = request.POST.get('lastname')
        email = request.POST.get('email')
        input_password = request.POST.get('password')
        conform_password = request.POST.get('conform_password')
        if input_password != conform_password:
            return HttpResponseRedirect(reverse('sign_up')+'?conform_password=false')
        salt = bcrypt.gensalt()
        hashed = bcrypt.hashpw(input_password.encode('utf-8'), bcrypt.gensalt())
        password = hashed
        date = datetime.datetime.now()
        new_user = users.objects.create(name=str(name), lastname=lastname, email=email, password=password, date_joined=date)
        new_user.save()
        return HttpResponseRedirect(reverse('sign_in')+'?success=true')
    data['sign_up_form'] = form
    return render(request, 'users_app/sign_up.html', data)


#account_page
def account_page(request):
    data = {}
    user = request.session.get('user')
    if not user:
        return HttpResponseRedirect(reverse('sign_in'))
    return render(request, 'users_app/account.html', data)

#log_our_user_page
def log_out_user_page(request):
    if request.session.get('user'):
        del(request.session['user'])
        return HttpResponseRedirect(reverse('sign_in'))

def forgot_password_page(request):
    print('hi')
