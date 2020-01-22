from django.http  import HttpResponse
from django.shortcuts import render
from .models import CarMake
# Create your views here.
def home_project(request):
    
    return render(request, 'index.html')
def car(request):
    return render(request, 'navbar.html')



def search_results(request):
    if 'order' in request.GET and request.GET["order"]:
        search_term = request.GET.get("order")
        searched_articles = Article.search_by_title(search_term)
        message = f"{search_term}"
        
        return render(request, 'search.html',{"message":message,"order": searched_orders})


    