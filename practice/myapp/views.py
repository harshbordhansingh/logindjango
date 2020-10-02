from django.shortcuts import render, HttpResponse
from datetime import datetime
from myapp.models import Contact
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request, 'index.html')

def about(request):
    return HttpResponse("This is my aboutpage.")

def services(request):
    return HttpResponse("This is my servicespage.")

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        description = request.POST.get('description')
        contact = Contact(name=name, email=email, description=description, date=datetime.today())
        contact.save()
        messages.success(request, 'Profile details updated.')
    return render(request, 'contact.html')