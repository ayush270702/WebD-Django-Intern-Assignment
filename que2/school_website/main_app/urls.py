from django.urls import path

from .views import *

urlpatterns = [
 
    # Defining various url using path with first argument as route, second argument as view which need to be called , and optional argument name
    
    path('home/', home, name='home'),   
    path('register', register, name='register'),    
    path('stud_register/', stud_registration, name='stud_register'), 
    path('teach_register/', teach_registration, name='teach_register'), 
    path('stud_profile/<int:pk>/', stud_prof, name='stud_profile'),
    path('teach_profile/<int:pk>/', teach_prof , name='teach_profile'),
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
    
]
