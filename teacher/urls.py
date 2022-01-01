from django.urls import path
from teacher.views import *
urlpatterns = [
    path('', hometeacher, name="HomeTeacher"),
    path('register/',TeacherSignUpView.as_view(), name='registerTeacher'),
    path('login/',LoginTeacher, name='loginTeacher'),
    path('logout/', logoutUser, name='logoutTeacher'),
    path('Posts/', poststeacher, name='PostsTeacher'),
    path('createpost/',createPost, name='createPostTeacher'),
    path('account/', TeacherAccount, name="TeacherAccount"),
    path('update_profile/', updateProfileTeacher, name="update_profileTeacher"),
    path('groups/<slug:slug>/', creategroup, name='GroupsTeacher'),
    path('postView/<slug:slug>/', post, name="teacherpost"),
    path('update_post/<slug:slug>/', updatePost, name="update_postTeacher"),
	path('delete_post/<slug:slug>/', deletePost, name="delete_postTeacher"),

]
