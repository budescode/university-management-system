from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from .models import Faculty, Department
from django.contrib.auth.models import User

#this is the main administrator view
def administrator(request):
	return render(request, 'admin1/index.html')


#this view will give list of faculty
def faculty_view(request):
	domain = request.get_host()
	qs = Faculty.objects.all()
	context = {'qs':qs, 'domain':domain}
	return render(request, 'admin1/faculty.html', context)

#this view will give list of the department
def department_view(request):
	domain = request.get_host()
	qs = Department.objects.all()
	faculty  = Faculty.objects.all()
	context = {'qs':qs, 'domain':domain, 'faculty':faculty}
	return render(request, 'admin1/department.html', context)

#this view is to add faculty
def add_faculty_view(request):
	addfaculty = request.POST.get('addfaculty')
	qs = Faculty.objects.create(faculty=addfaculty)
	print(addfaculty, 'yeahh')

	return JsonResponse({'id':qs.id, 'addfaculty':addfaculty})

#this view is to edit faculty
def edit_faculty_view(request, id):
	editfaculty = request.POST.get('editfaculty')
	qs = Faculty.objects.get(id=int(id))
	qs.faculty  = editfaculty
	qs.save()
	#print('testttt', id, editfaculty)
	return JsonResponse({'id':id, 'editfaculty':editfaculty})

#this view is to delete faculty
def delete_faculty_view(request, id):
	qs = Faculty.objects.get(id=int(id))
	# qs.delete()
	print('yeahhh', qs)
	return JsonResponse({'id':id})



#this view is to add department
def add_department_view(request):
	adddepartment = request.POST.get('adddepartment')
	addfaculty = request.POST.get('addfaculty')
	faculty = Faculty.objects.get(faculty=addfaculty)
	#print(adddepartment, addfaculty, faculty)
	qs = Department.objects.create(faculty=faculty, department=adddepartment)

	return JsonResponse({'adddepartment':adddepartment, 'addfaculty':addfaculty, 'id':qs.id})


def edit_department_view(request, id):
	editfaculty = request.POST.get('editfaculty')
	editdepartment = request.POST.get('editdepartment')
	
	faculty = Faculty.objects.get(faculty=editfaculty)
	qs = Department.objects.get(id=id)
	qs.faculty  = faculty
	qs.department = editdepartment
	qs.save()
	#print('testttt', id, editfaculty)
	return JsonResponse({'id':id, 'editfaculty':editfaculty, 'editdepartment':editdepartment})


#this view is to delete faculty
def delete_department_view(request, id):
	qs = Department.objects.get(id=int(id))
	qs.delete()
	print('yeahhh', qs)
	return JsonResponse({'id':id})

def students(request):
	qs = User.objects.filter(is_staff = False)
	context = {'qs':qs}
	return render(request, 'admin1/students.html', context)
