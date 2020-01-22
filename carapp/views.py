from django.http  import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_project(request):
    return render(request, 'index.html')
def car(request):
    return render(request, 'navbar.html')



    