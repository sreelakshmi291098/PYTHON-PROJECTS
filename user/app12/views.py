from django.shortcuts import render

# Create your views here.
from app12.forms import Newuserform

def index(request):
    return render(request,'index.html')

def users(request):
    form=Newuserform()
    if request.method=='POST':
        form=Newuserform(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print('ERROR FROM INVALID')
    return render(request,'user.html',{'form':form})
