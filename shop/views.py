from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
#urls.py is not present in the shop
#so we need to create the urls.py file in the shops
# def index(request):
#     return HttpResponse("welcome to the ecommerce website aamir")
def index(request):
    return render(request,'shop/index.html')
def about(request):
    return HttpResponse("we are at about section")
def contact(request):
    return HttpResponse("we are at contact section")
def tracker(request):
    return HttpResponse("we are at tracker section")
def search(request):
    return HttpResponse("we are at search section"),
def product(request):
    return HttpResponse("we are at product view section")
def checkout(request):
    return HttpResponse("we are at checkout section")