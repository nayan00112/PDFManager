from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
# Create your views here.
def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username = username, password = password)
        if user is not None:
            auth.login(request, user)
            return redirect('Home')
        else:
            messages.info(request, 'User does not exist')
            return redirect('signin')
    else:
        return render(request, 'Accounts/login.html')
def signup(request):
    if request.method == 'POST':
        name = request.POST['name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:
            if User.objects.filter(username = username).exists():
                messages.info(request, 'Username is allrady taken')
                return render(request, 'accounts/signup.html')
            elif User.objects.filter(email = email).exists():
                messages.info(request, 'Email is allrady taken')
                return render(request, 'accounts/signup.html')
            else:
                user = User.objects.create_user(first_name = name, username = username, email = email, password = password1)
                user.save() 
                messages.info(request, 'User Created. Now go to Signin')
                return render(request, 'accounts/signup.html')
        else:
            messages.info(request, '''Password dosen't metch''')
            return render(request, 'accounts/signup.html')
    else:
        return render(request, 'accounts/signup.html')
def logout(request):
    auth.logout(request)
    return redirect('/')