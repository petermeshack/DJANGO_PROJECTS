from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'blog/blog.html')


def contact(request):
    return render(request, 'blog/contact.html',
                  {'content': ['If you would like to contact me, please email me.', 'www.petermeshack@gmail.com']})


