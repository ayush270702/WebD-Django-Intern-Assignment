from ast import In
from django.db import models
from django.contrib.auth.models import User
from django.forms import CharField, IntegerField    
from django.core.validators import MaxValueValidator, MinValueValidator              


# Creating student model
class Student(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)                              #  Connecting Student model to User model using foreign key
    
    standard = models.IntegerField(validators=[MinValueValidator(5),MaxValueValidator(10)])  # std. of student with min value of 5 and max value of 10
                                      
    section = models.CharField(max_length=2, choices=[('A', 'A'), ('B', 'B'), ('C', 'C')])   # Defining choices for student section
    
    roll_no = models.IntegerField(null=True)                                                 # Roll number of student
    
    gender = models.CharField(max_length=6, choices= [("Male","Male"), ("Female","female")], null=True)  # Gender of student
    
    dob = models.DateField(null=True)    # Date of birth
    
    age = models.IntegerField(null=True) # age of student
    
    # Defining str function to return student's first name in admin panel
    def __str__(self):
        return self.student.first_name
    
    
    
# Creating Teacher model    
class Teacher(models.Model):
    teacher  = models.ForeignKey(User, on_delete=models.CASCADE)        #  Connecting Teacher model to User model using foreign key
    
    subject = models.CharField(max_length=50, null=True)                # subject taught by teacher
    
                   
    section = models.CharField(max_length=2, choices=[('A', 'A'), ('B', 'B'), ('C', 'C')])   # To wich section teacher teaches
    
    mobile_number = models.CharField(max_length=12, null=True)          # mobile number of teacher
    
    gender = models.CharField(max_length=6, choices= [("Male","Male"), ("Female","female")], null=True)   # gender of teacher
    
    dob = models.DateField(null=True)    # Date of birth
    
    age = models.IntegerField(null=True) # age of teacher
    
    # Defining str function to return teacher's first name in admin panel
    def __str__(self):
        return self.teacher.first_name