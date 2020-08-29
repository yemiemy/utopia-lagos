from django.shortcuts import render
from django.contrib import messages
from .models import Contact, New
from blog.models import Post
from datetime import datetime
# Create your views here.

def index(request):
    posts = Post.objects.all().order_by('-id')[:2]
    return render(request, 'pages/index.html', {'posts':posts})

def citylab(request):
    return render(request, 'pages/citylabs.html')

def portfolio(request):
    return render(request, 'pages/portfolio.html')

# News view
def news(request):
    news = New.objects.all()
    return render(request, 'pages/news.html', {'news':news})

# Lagos Urban Innovation Challenge
def luic(request):
    return render(request, 'pages/luic.html')

# MegaCity Fund
def mcf(request):
    return render(request, 'pages/mcf.html')

def about(request):
    return render(request, 'pages/about.html')


# function to receive the contact form from the front-end
def contact(request):
    try:
        if request.method == 'POST':
            name = request.POST['name']
            email = request.POST['email']
            subject = request.POST['subject']
            message = request.POST['message']
            date_stamp = datetime.now()
            
            contact_me = Contact.objects.create(
                name=name, 
                email=email, 
                subject=subject, 
                message=message, 
                date_stamp=date_stamp
                )
            contact_me.save()
            messages.success(
                request, 
                'Your message has been successfully sent! Thanks for reaching out.'
                )
        return render(request, 'pages/contact.html')
    
    except Exception as e:
        return render(request, 'pages/error.html', {'e':e})


def error_404(request, exception):
    return render(request, 'pages/error_404.html', status=404)

def error_500(request):
    data = {}
    return render(request, 'pages/error_500.html', data)

def error_403(request, exception):
    return render(request, 'pages/error_403.html', status=403)