from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import logout , authenticate, login



# Create your views here.
# pass word for test user is  888888888888888888888888              qazwsxedcrfvtgb!@#

def index(request):

    if request.user.is_anonymous:
        return redirect("/login")




    return render(request, 'index.html')


def loginUser(request):
    if request.method== "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        # check if user has correct credentials
        user = authenticate(username=username , password=password)
        if user is not None:
            login(request,user)
            redirect("/")
         # A backend authenticated the credentials
        else:
            return render(request, 'login.html')
        # No backend authenticated the credentials




    return render(request, 'login.html')


def logout(request):
    return render(request, 'index.html')





def logoutUser(request):
    logout(request)
    return redirect("/login")
    # Redirect to a success page.