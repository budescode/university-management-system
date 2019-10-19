from django.db import models
from django.contrib.auth.models import User
from administrator.models import Course, Faculty, Department

# Create your models here.

class CustomUser(models.Model):
    MALE = 'male'
    FEMALE = 'female'

    GENDER_CHOICES = (
        ('', 'Choose your gender'),
        (MALE, 'Male'),
        (FEMALE, 'Female')
    )
    MODE_CHOICES = (
        ('', 'Mode Of Enter'),
        ('UTME', 'UTME'),
        ('D.E', 'D.E'),
        
    )
    
    user = models.ForeignKey(User, on_delete  = models.CASCADE, related_name='student')
    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100)
    other_names = models.CharField(max_length=100)
    email = models.EmailField()
    gender = models.CharField(choices=GENDER_CHOICES, max_length=6)
    date_of_birth = models.DateField(default="1970-01-01")

    state_of_origin = models.CharField(max_length=100)
    lga_of_origin = models.CharField(max_length=100)
    nationality = models.CharField(max_length=15)

    faculty = models.ForeignKey(Faculty, on_delete  = models.CASCADE, default=1)
    dept = models.ForeignKey(Department, on_delete  = models.CASCADE, default=1)
    jamb_reg_no = models.CharField(max_length=15)
    mode_of_entry = models.CharField(max_length=15, choices=MODE_CHOICES)
    course_of_study = models.ForeignKey(Course, on_delete=models.CASCADE)
    password = models.TextField()

    # passport = models.ImageField(upload_to="users/applicants/passports")
    admitted  = models.BooleanField(default=False)

    def __str__(self):
    	return self.first_name +  '  '  + self.middle_name + " " + self.other_names
