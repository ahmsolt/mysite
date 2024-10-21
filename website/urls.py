from website.views import *
from django.urls import path 

app_name = 'website'

urlpatterns = [
    path('', index_view,name='index'),
    path('about',about_view,name='about'),
    path('contact',contact_view,name='contact')
    
]