from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse 




def administrator(request):
	return render(request, 'administrator/index.html')
