from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .forms import SignupForm  
from django.contrib.auth import login, logout, authenticate;
from random import* 
from django.core.mail import send_mail
from .models import Profile

	
def uhome(request):
	if request.user.is_authenticated:
		return render(request,"uhome.html")
	else:
		return redirect("ulogin")

def ulogin(request):
    if request.method == "POST":
        un = request.POST.get("username")
        pw = request.POST.get("password")
        
        user = authenticate(request, username=un, password=pw)
        
        if user is not None:
            
            login(request, user)
            return redirect("uhome")  
        else:
            msg = "Invalid username or password"
            return render(request, "ulogin.html", {"msg": msg})
    else:
        
        return render(request, "ulogin.html")


def usignup(request):
    if request.user.is_authenticated:
        return redirect("uhome")
    
    if request.method == "POST":
        form = SignupForm(request.POST, request.FILES)
        if form.is_valid():
            data = form.cleaned_data
            pw = data['password']
            cpw = data['confirm_password']

            if pw != cpw:
                msg = "Passwords do not match"
                return render(request, "usignup.html", {"form": form, "msg": msg})

            if User.objects.filter(username=data['username']).exists():
                msg = "Username already taken"
                return render(request, "usignup.html", {"form": form, "msg": msg})

            usr = User.objects.create_user(
                username=data['username'],
                email=data['email'],
                password=pw,
                first_name=data['first_name'],
                last_name=data['last_name']
            )

            Profile.objects.create(
                user=usr,
                profile_picture=data.get('profile_picture'),
                address_line1=data.get('address_line1'),
                city=data.get('city'),
                state=data.get('state'),
                pincode=data.get('pincode'),
                user_type=data.get('user_type')
            )

            
            
            subject = "Welcome!"
            text = "Thank you for signing up!"
            from_email = "sai.tester24jan24@gmail.com"
            to_email = [data['email']]
            send_mail(subject, text, from_email, to_email)

            
            return redirect("ulogin")  
        else:
            return render(request, "usignup.html", {"form": form})
    else:
        form = SignupForm()
        return render(request, "usignup.html", {"form": form})


def uhome(request):
    if request.user.is_authenticated:
        profile = Profile.objects.filter(user=request.user).first()
        return render(request, "uhome.html", {"user": request.user, "profile": profile})
    else:
        return redirect("ulogin")


def ulogout(request):
	logout(request)
	return redirect("ulogin")	
