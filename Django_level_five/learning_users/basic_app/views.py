from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'basic_app/index.html')

def base(request):
    return render(request, 'basic_app/base.html')



def registration(request):
	return render(request,"basic_app/registration.html")

def login(request):
	return render(request,"basic_app/login.html")