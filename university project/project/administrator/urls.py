from django.conf.urls import url, include
from django.contrib.auth import views as auth_views
# from django.contrib.auth.views import login, logout
from django.views.generic.base import TemplateView
from django.contrib.auth import views
from . import views
from django.contrib.auth import views as auth_views



from django.contrib.auth.views import PasswordResetView

from django.urls import path


app_name = "administrator"
urlpatterns = [
	path('', views.administrator, name='administrator'),







]







