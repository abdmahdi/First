from django.urls import path
from student.views import *
urlpatterns = [
    #Home Student
    path('', homestudent, name="HomeStudent"),
    #POsts :: Post
    path('posts/', posts, name="Posts"),
    path('postshool/', postschool, name="Postshool"),
    path('post/<slug:slug>/', post, name="postTeacher"),
    path('postschool/<slug:slug>/', postsch, name="post"),
    path('Subscripe/<slug:slug>/', subscripeTeach, name="SubscripeTeacher"),
    path('Subscrips/',studentsubteach, name = "StudentSubscripe"),
    
    # Sign UP Student
    path('register/',StudentSignUpView.as_view(), name="registerStudent"),
    # profile student
    path('account/', StudentAccount, name="StudentAccount"),
    path('update_profile/', updateProfile, name="update_profileStudent"),
    
    
    #login/// logout
    path('login/', loginPage, name='loginStudent'),
    path('logout/', logoutUser, name='logoutStudent'),
   


    
]

