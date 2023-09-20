from django.shortcuts import render , redirect
from .models import Registration

# Create your views here.
def index(request):
    return render(request,"index.html",{})

def about(request):
    return render(request,"about.html",{})

def courses(request):
    return render(request,"courses.html",{})

def join_us(request):
    if request.method=="POST":
        name=request.POST['name']
        email=request.POST['email']
        type=request.POST['user-type']
        subject=request.POST['subject']
        message=request.POST.get('message')

        Registration.objects.create(name=name,email=email,type=type,subject=subject,message=message)
        print("Registration Successfull")
        return redirect("/join-us")

    return render(request,"join-us.html",{})

def teachers(request):
    return render(request,"teachers.html",{})

def blog(request):
    return render(request,"blog.html",{})

def contact(request):
    return render(request,"contact.html",{})

def single(request):
    return render(request,"single.html",{})
