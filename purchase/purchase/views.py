from django.shortcuts import render, HttpResponse, redirect
from django.urls import reverse_lazy

def Home(request):
	return render(request, 'home.html', {})

def Admin(request):
	return render(request, 'admin.html', {})

def ScreenShots(request):
	return render(request, 'screenshots.html', {})