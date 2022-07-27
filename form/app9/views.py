from django.shortcuts import render
from app9.forms import Register

# Create your views here.
def index(request):
    form=Register()

    if request.method=='POST':
        form=Register(request.POST)
        if form.is_valid():
            print("form validation success.print in console")  
            print("Name"+form.cleaned_data['Name']) 
            print("Email"+form.cleaned_data['Email']) 
            print("Text"+form.cleaned_data['Text'])  
    return render(request,'index.html',{'form':form})