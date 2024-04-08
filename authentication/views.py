from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from .forms import LoginAuthenticationForm

# Create your views here.
def sign_in(request):
    if request.method == "POST":
        user = authenticate(request, username = request.POST["username"], password = request.POST["password"])

        if not user:
            return render(request, "login.html",{
                "form": LoginAuthenticationForm(),
                "error": "Username or password incorrect"
            })
        else:
            login(request, user)
            return redirect("/excel")
    else:
        if request.user.is_authenticated:
            return redirect("/excel")
            
        return render(request, "login.html",{
            "form": LoginAuthenticationForm()
        })

def terminate_session(request):
    logout(request)
    return redirect("/auth")