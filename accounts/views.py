from django.shortcuts import render, redirect
from django.contrib import messages, auth
# Create your views here.

# user model
from django.contrib.auth.models import User

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'username is taken')
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'email is taken')
                    return redirect('register')
                else:
                    user = User.objects.create_user(
                        username=username,
                        email=email,
                        password=password    
                    )
                    user.save()
                    messages.success(request, f'hey {username}, you are now registed')
                    return redirect('login')
        else:
            messages.error(request, 'password do not match')
            return redirect('register')
    else:
        return render(request, 'accounts/register.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(
            username=username,
            password=password
        )

        if user is not None:
            auth.login(request, user)
            messages.success(request, f'hey {username}, you are now logged in')
            return redirect('home')
        else:
            messages.error(request, 'invalid credentials')
            return redirect('login') 
    else:
        return render(request, 'accounts/login.html')

 
def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request, 'logged out')
        return redirect('login') 