from django.shortcuts import render,redirect


def home(request):
    return render(request,"index.html")

def main(request):
    return render(request,"index1.html")

def calender(request):
    return render(request,"calender.html")

def tasks(request):
    return render(request,"tasks.html")

def addtasks(request):
    return render(request,"add-tasks.html")

def login(request):
    return render(request,"login.html")

def register(request):
    return render(request,"register.html")

def forgot(request):
    return render(request,"forgot.html")

# views.py
 # Import the User model
