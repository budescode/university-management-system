from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField 


class Faculty(models.Model):
	faculty = models.CharField(max_length=100)

	def __str__ (self):
		return self.faculty

class Department(models.Model):
	faculty = models.ForeignKey(Faculty, on_delete = models.CASCADE)
	department = models.CharField(max_length=100)

	def __str__ (self):
		return self.department


class Course(models.Model):
	department = models.ForeignKey(Department, on_delete = models.CASCADE)
	course = models.CharField(max_length=100)

	def __str__(self):
		return self.course