

from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.


def index(request):
    return render(request,'shop/index.html')

def about(request):
    return HttpResponse("This is About Us")

def contact(request):
    return HttpResponse("This is contact")
def tracker(request):
    return HttpResponse("This is tracker")
def search(request):
    return HttpResponse("This is search")

def prodview(request):
    return HttpResponse("This is prodview")
def checkout(request):
    return HttpResponse("This is checkout")