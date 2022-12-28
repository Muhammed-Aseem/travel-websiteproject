from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user=auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'invalid credentials')
            return redirect("login.html")


    return render(request,'login.html')
def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        first_name = request.POST['firstname']
        last_name = request.POST['lastname']
        email = request.POST['email']
        password = request.POST['password']
        passwordc = request.POST['password1']
        if password==passwordc:
            if User.objects.filter(username=username).exists():
                print("taken")
                messages.info(request,"username  taken")
                return  redirect("register")
            elif User.objects.filter(email=email).exists():
                messages.info(request,"email taken")
                return  redirect("register")
            else:
                user=User.objects.create_user(username=username,password=password,last_name=last_name,email=email,first_name=first_name)

                user.save();
                return redirect("login")
            print("user created")
        else:
            messages.info(request,"password not matched")
            return redirect("register")
        return redirect("/")
    return render(request,"register.html")

def logout(request):
    auth.logout(request)
    return redirect('/')
