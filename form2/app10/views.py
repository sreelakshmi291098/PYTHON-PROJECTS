from django.shortcuts import render

# Create your views here.

from app10.forms import Register

# Create your views here.
def index(request):
    return render(request,'index.html')

def form(request):
    form=Register()

    if request.method=='POST':
        form=Register(request.POST)
        if form.is_valid():
            print("form validation success.print in console")  
            print("Name"+form.cleaned_data['Name']) 
            print("Email"+form.cleaned_data['Email']) 
            print("Text"+form.cleaned_data['Text'])
            print("Password"+form.cleaned_data['Password'])
    return render(request,'form.html',{'form':form})
    
