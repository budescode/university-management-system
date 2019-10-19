from django.urls import path, include
from django.conf.urls import url
from . import views

app_name = 'users'


urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('profile/', views.profile, name='profile'),
    path('logout/', views.logout_view, name='logout'),
    
    
    

    
    

]
