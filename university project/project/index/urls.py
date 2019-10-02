from django.urls import path, include
from django.conf.urls import url
from . import views

app_name = 'index'


urlpatterns = [
    path('', views.index, name='index'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('blog/', views.blog, name='blog'),
    
    

]
