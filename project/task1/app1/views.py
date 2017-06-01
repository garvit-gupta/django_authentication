# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect

# Create your views here.
from django.http import HttpResponse
from django.contrib.auth import authenticate,login
from django.views.generic import View
from .forms import UserForm


def index(request):
    return HttpResponse("Hello. You're at the homepage.")

def login(request):
	return render(request,'app1/login.html')

def register(request):
	return HttpResponse("Register Page")

def dashboard(request,user_id):
	return HttpResponse("User ID: %s" % user_id)

class UserFormView(View):
	form_class=UserForm
	template_name='app1/login.html'

	def get(self,request):
		form=self.form_class(None)
		return render(request,self.template_name,{'form':form})

	def post(self,request):
		form=self.form_class(request.POST)

		if form.is_valid():
			user=form.save(commit=False)
			username=form.cleaned_data['username']
			password=form.cleaned_data['password']
			user.ser_password(password)
			user.save

			user=authenticate(username=username,password=password)

			if user is not None:

				if user.is_active:

					login(request,user)
					return redirect('app1:index')
		return render(request,self.template_name,{'form':form})
