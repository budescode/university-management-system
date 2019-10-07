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
	path('faculty/', views.faculty_view, name='faculty'),
	path('department/', views.department_view, name='department'),
	path('add-faculty/', views.add_faculty_view, name='add_faculty'),
	path('add-department/', views.add_department_view, name='add_department'),
	path('edit-faculty/<slug:id>/', views.edit_faculty_view, name='edit_faculty'),	
	path('delete-faculty/<slug:id>/', views.delete_faculty_view, name='delete_faculty'),
	path('delete-department/<slug:id>/', views.delete_department_view, name='delete_department'),
	path('edit-department/<slug:id>/', views.edit_department_view, name='edit_department'),
	

	
	
	







]







