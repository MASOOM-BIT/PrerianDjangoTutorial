from django.shortcuts import render
from . import forms
# Create your views here.
def index(request):
	return render(request,'basicApp/index.html')

def form_name_view(request):
	form=forms.FormName()

	if request.method=='POST':
		form=forms.FormName(request.POST)

		if form.is_valid():
			print("VALIDATION SUCESS")
			print("NAME :"+form.cleaned_data['name'])
			print("Email:"+form.cleaned_data['email'])
			print("Verifiy_Email:"+form.cleaned_data['verify_email'])
			print("TEXT :"+form.cleaned_data['text'])

	return render(request,'basicApp/form_page.html',{'form':form})