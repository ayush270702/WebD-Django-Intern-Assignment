from django.shortcuts import render, redirect
from django.contrib import auth
from .forms import * 
from datetime import date
# Create your views here.

# Creating View for home page
def home(request):
    return render(request, 'main_app/home.html')   # we will render home.html upon request


# creating view which will return page that asks for student or teacher
def register(request):
    return render(request, 'main_app/register.html')  # we will render register.html upon request


# creating view for student registration
def stud_registration(request):
    if request.method == 'POST':    # checking if request is post request
        form = Stud_form(request.POST)   # declaring stud_form
        if form.is_valid():              # checking if data in form is valid
            user = form.save()           # saving form or creating model in user model
        
        #getting data from form and storing in variables
        standard = form.cleaned_data.get('standard')
        section = form.cleaned_data.get('section')
        roll_no = form.cleaned_data.get('roll_no')
        gender = form.cleaned_data.get('gender')
        dob = form.cleaned_data.get('dob')
        
        today = date.today()    # use to get current date
        age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))     # calculating age with help of date of birth and current date
        
        Student.objects.create(student=user, section=section, roll_no=roll_no, gender=gender, standard=standard, age=age, dob=dob)  # creating object of student and saving all fields      
        return render(request, 'main_app/home.html')    # we will render home.html upon request
    
    else:                        # checking if request is get
        form = Stud_form()       # using stud_form to get  form 
        return render(request, 'main_app/signup.html', {'form': form})  # we will render signup.html upon request and we are sending form as context
    
    
# Creating View for teacher registration    
def teach_registration(request):
    if request.method == 'POST':         # checking if request is post request
        form = Teach_form(request.POST)  # declaring teach_form
        if form.is_valid():              # checking if data in form is valid
            user = form.save()           # saving form or creating model in user model
        
        #getting data from form and storing in variables
        subject = form.cleaned_data.get('subject')
        mobile_number = form.cleaned_data.get('mobile_number')
        section = form.cleaned_data.get('section')
        gender = form.cleaned_data.get('gender')
        dob = form.cleaned_data.get('dob')
        
        today = date.today()            # use to get current date
        age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day)) # calculating age with help of date of birth and current date
        
        
        Teacher.objects.create(teacher=user, section=section, gender=gender, subject=subject, mobile_number=mobile_number, age=age, dob=dob)      # creating object of teacher and saving all fields  
        return render(request, 'main_app/home.html')    # we will render home.html upon request
    
    else:                       # Checking if request is get
        form = Teach_form()     # Using teach_form to get form
        return render(request, 'main_app/signup.html', {'form': form})    # we will render signup.html upon request and we are sending form in context
    


# creating view for student profile    
def stud_prof(request,pk):       # getting request with primary key
    student = Student.objects.get(pk=pk)    #getting particular student with help of pk
    return render(request, 'main_app/stud_profile.html', {'student': student})    # we will render stud_profile.html upon request and passing student object as context


# creating view for teacher profile
def teach_prof(request,pk):  # getting request with primary key
    teacher = Teacher.objects.get(pk=pk)    #getting particular teacher with help of pk
    return render(request, 'main_app/teach_profile.html', {'teacher': teacher})     # we will render teach_profile.html upon request and passing teacher object as context


def login(request):
    if request.method == 'POST':        # Checking if request is post
        
        # Getting username and password
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)  # Validating username and password

        if user is not None:  # if username and password are correct
            if Student.objects.filter(student=user).exists():   # if any student with student=user exists
                auth.login(request, user)     # login user
                return redirect(f"/school/stud_profile/{Student.objects.filter(student=user)[0].id}/")     #redirecting to student profile page and passing id of first user in queryset
            
            elif Teacher.objects.filter(teacher=user).exists():    # if any student with student=user exists
                auth.login(request, user)   # login user
                return redirect(f"/school/teach_profile/{Teacher.objects.filter(teacher=user)[0].id}/")     #redirecting to teacher profile page and passing id of first user in queryset
             
        else:    # If username and password are incorrect
            context = {'error': True}   
            return render(request, 'main_app/login.html',context)   # Rendering login.html as passing context with error as true
    return render(request, 'main_app/login.html')      # if request is get we will render login.html



# creating view to logout
def logout(request):
    auth.logout(request)    # logging out current user
    return redirect("/school/home")    # redirecting to home page