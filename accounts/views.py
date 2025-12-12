from django.shortcuts import render , redirect
from django.contrib.auth import authenticate, login

# Create your views here.
def login_views(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["Password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request , user)
            return redirect("/")
    if request.user.is_authenticated:
        msg = f"user is authenticated as {request.user.username}"
    else:
        msg = f"user is not authenticated"
    return render(request , "accounts/login.html" , {"msg":msg})
# def logout_views(request):
#     return render(request , "accounts/logout.html")
def signup_views(request):
    return render(request , "accounts/signup.html")