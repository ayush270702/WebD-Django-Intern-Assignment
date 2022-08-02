from dataclasses import fields
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import *


# Modifying UserCreationForm for student registration 
class Stud_form(UserCreationForm):
    
    # Defining feields in form
    email = forms.EmailField(max_length=225)
    first_name = forms.CharField(max_length=225)
    last_name = forms.CharField(max_length=225)
    roll_no = forms.IntegerField()
    standard = forms.IntegerField()
    username = forms.CharField(max_length=255)
    
    dob = forms.DateField()
    
    gender=forms.CharField(label='Gender', widget=forms.RadioSelect(choices=[("Male","Male"), ("Female","Female")]))
    section=forms.CharField(label='section', widget=forms.RadioSelect(choices=[('A','A'), ('B','B'), ('C','C')]))      
    
    
    class Meta:
        model =  User  
        fields = ['first_name', 'last_name', 'email','roll_no', 'standard', 'username','gender', 'section', 'dob']     # Defining fields to be shown in form 
    
    
    
  
    
# Modifying UserCreationForm for teacher registration   
class Teach_form(UserCreationForm):
    # Defining feields in form
    email = forms.EmailField(max_length=225)
    first_name = forms.CharField(max_length=225)
    last_name = forms.CharField(max_length=225)
    subject = forms.CharField(max_length=225)
    mobile_number = forms.CharField(max_length=12)
    username = forms.CharField(max_length=255)
    dob = forms.DateField()
    
    section=forms.CharField(label='section', widget=forms.RadioSelect(choices=[('A','A'), ('B','B'), ('C','C')])) 
    gender=forms.CharField(label='Gender', widget=forms.RadioSelect(choices=[("Male","Male"), ("Female","Female")]))
    
    class Meta:
        model = User
        fields = ['first_name','last_name', 'email', 'subject', 'mobile_number', 'gender', 'section', 'username','dob']  # Defining fields to be shown in form 
    
    