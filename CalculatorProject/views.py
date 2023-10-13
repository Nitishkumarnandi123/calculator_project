from django.http import HttpResponse
from django.shortcuts import render


def homepage(request):
    return HttpResponse("welcome to home page")


#def index(request):
#    return HttpResponse("wel come to<br> index page")
def index1(request):
    return render(request,'index1.html')
