from django.shortcuts import render
from . import forms
# Create your views here.
def index(request):
	return render(request,'basicApp/index.html')

def form_name_view(request):
	form=forms.FormName()
	return render(request,'basicApp/form_page.html',{'form':form})