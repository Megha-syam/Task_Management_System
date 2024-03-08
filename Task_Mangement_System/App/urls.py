from django.urls import path,include
from .views import *

urlpatterns=[
	path('home',home,name='home'),
    path('',main,name="main"),
    path('calender',calender,name = "calender"),
    path('tasks',tasks,name="tasks"),
    path('addtasks',addtasks,name="add-tasks"),
    path('login',login,name="login"),
    path('register.html',register,name="register"), 
    path('forgot',forgot,name="forgot"),

]