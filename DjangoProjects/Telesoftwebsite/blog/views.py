from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'peterblog\home.html')

def contact(request):
    return render(request, 'peterblog\contact.html')

def blog(request):
    return render(request, 'peterblog\ blog.html')