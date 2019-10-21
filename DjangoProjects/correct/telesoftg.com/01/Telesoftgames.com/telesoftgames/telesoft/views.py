from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'telesoft/home.html')


def hardware(request):
    return render(request, 'telesoft/telesofthardwares.html')


def software(request):
    return render(request, 'telesoft/telesoftsoftwares.html')


def blog(request):
    return render(request, 'blog/blog.html')

