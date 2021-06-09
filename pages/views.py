from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
# Create your views here.

from .models import Contact, InquiryModal

def home(request):
    # EXPRIMENTING USER MODELS AND FUNCTIONS
    # print(request.user.is_authenticated)
    # print(request.user.is_anonymous)
    # print(request.user.is_staff)
    # print(request.user.is_active)
    # print(request.user.is_superuser)
    # print(request.user.date_joined)
    # print(request.user.last_login)
    # print(request.user.user_permissions)


    return render(request, 'pages/home.html')

def about(request):
    return render(request, 'pages/about.html')

def services(request): 
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']

        inquiry = InquiryModal(
            name=name,
            email=email,
            phone=phone,
            message=message
        )
        inquiry.save()
        messages.success(request, f'hey {request.user}, you will receive a email shortly')
        try:
            send_mail(
                'SHELD, messages',
                'we will get back to you as soon as possible.',
                'publishfirsttest@gmail.com',
                [email],
                fail_silently=False
            )
        except:
            pass
        return redirect(services)
    else:
        return render(request, 'pages/services.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']

        contact = Contact(
            name=name,
            email=email,
            message=message
        )
        contact.save()
        messages.success(request, 'message sended, you will receive a email shortly')
        try:
            send_mail(
                'THANK YOU FOR MESSAGING US',
                'we will get back to you as soon as possible.',
                'publishfirsttest@gmail.com',
                [email],
                fail_silently=False
            )
        except:
            pass

        return redirect(home)
    else:
        return render(request, 'pages/contact.html')
