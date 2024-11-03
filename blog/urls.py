from blog.views import *
from django.urls import path 

app_name = 'blog'

urlpatterns = [
    path('', blog_view,name='index'),
    path('<int:pid>',blog_single,name='single'),
    path('category/<str:cat_name>' ,blog_category,name='category'),
    path('test',test,name='test'), 
   
]