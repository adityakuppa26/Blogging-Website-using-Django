from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login
from django.views import generic
from django.views.generic import View
from .forms import UserForm
# Create your views here.
def index(request):
	return render(request,'personal/home.html')
def contact(request):
	return render(request,'personal/basic.html',{'content':['contact me at ','adityakuppa@gmail.com']})

