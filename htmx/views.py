import time

from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html', {})

def element1(request):
    time.sleep(2)
    return render(request, 'p1.html', {})

def element2(request):
    time.sleep(5)
    return render(request, 'p2.html', {})