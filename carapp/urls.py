from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^$',views.home_project,name='home_project'),
    url(r'^car/',views.car,name='car'),
    url(r'^search/', views.search_results, name='search_results')
    
]