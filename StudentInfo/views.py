from django.shortcuts import render


# from django.http import request
# Create your views here.
def index(request):
    hh = "Hello World!"
    return render(request, 'index.html', hh)
