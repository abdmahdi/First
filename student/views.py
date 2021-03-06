from django.shortcuts import redirect, render
from django.contrib.auth.models import Group, User,auth
from django.contrib.auth import login
from django.views.generic import *
from student.forms import *
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy
from django.contrib.auth import logout, login, authenticate
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from student.decorators import *
from teacher.models import PostTeacher
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from student.filters import *
from school.models import *

@student_required
def homestudent(request):
    return render(request, 'student/HomeStudent.html')
    

# Create your views here.
@student_required
def posts(request):
	posts = PostTeacher.objects.filter(active=True)
	myFilter = PostFilter(request.GET, queryset=posts)
	posts = myFilter.qs

	page = request.GET.get('page')

	paginator = Paginator(posts, 6)

	try:
		posts = paginator.page(page)
	except PageNotAnInteger:
		posts = paginator.page(1)
	except EmptyPage:
		posts = paginator.page(paginator.num_pages)

	context = {'posts':posts, 'myFilter':myFilter}
	return render(request, 'student/posts.html', context)

@student_required
def postschool(request):
	posts = PostSchool.objects.filter(active=True)
	myFilter = PostFilterSchool(request.GET, queryset=posts)
	posts = myFilter.qs

	page = request.GET.get('page')

	paginator = Paginator(posts, 5)

	try:
		posts = paginator.page(page)
	except PageNotAnInteger:
		posts = paginator.page(1)
	except EmptyPage:
		posts = paginator.page(paginator.num_pages)

	context = {'postschool':posts, 'myFilter':myFilter}
	return render(request, 'student/postschool.html', context)

   
       
    
    

# @student_required
# def post(request, slug):
# 	post = PostTeacher.objects.get(slug=slug)
#     group = Groupe.objects.get(postteacher = post)
# 	context = {'post':post, 'group':group}
# 	return render(request, 'student/post.html', context)

    
@student_required
def post(request,slug):
    post = PostTeacher.objects.get(slug=slug)
    groups = Groupe.objects.filter(postteacher = post)
  
    context = {'post':post, 'groups':groups}
    return render(request, 'student/post.html', context)



@student_required
def postsch(request,slug):
    post = PostSchool.objects.get(slug=slug)
    groups = GroupeSchool.objects.filter(postschool = post)
    context = {'postschool':post, 'groups':groups, }
    return render(request, 'student/postsch.html', context)
              
class StudentSignUpView(CreateView):
    model = User
    form_class = UserSignUp
    template_name = 'student/register.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'student'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('loginStudent')
    


def active(request):
        request.user.is_active=True
        
def loginPage(request):
    
	if request.user.is_authenticated and request.user.is_student==True:
		return redirect('HomeStudent')
	if request.method == 'POST':
		email = request.POST.get('email')
		password =request.POST.get('password')
		try:
			user = User.objects.get(email=email, is_student=True)
			user = authenticate(request, username=user.username, password=password)
		except:
			messages.error(request, 'User with this email does not exists')
			return redirect('loginStudent')
                                    
		if user is not None and user.is_student==True:
			login(request, user)
			return redirect('HomeStudent')
		else:
			messages.error(request, 'Email OR password is incorrect')


	context = {}
	return render(request, 'student/login.html', context)




def logoutUser(request):
	logout(request)
	return redirect('loginStudent')    

@student_required
def StudentAccount(request):
    profile = request.user.student
    subs =  SubscripeTeacher.objects.filter(student =profile)
    context = {'subs':subs, 'profile':profile}
    return render(request, 'student/account.html',context)


@student_required
def updateProfile(request):
	user = request.user
	profile = user.student
	form = ProfileForm(instance=profile)
	if request.method == 'POST':
		user_form = UserForm(request.POST, instance=user)
		if user_form.is_valid():
			user_form.save()

		form = ProfileForm(request.POST, request.FILES, instance=profile)
		if form.is_valid():
			form.save()
			return redirect('StudentAccount')


	context = {'form':form}
	return render(request, 'student/profile_form.html', context)



@student_required 
def subscripeTeach(request,slug):
    form = SubTeacher()
    if request.method =='POST':
        form = SubTeacher(request.POST , request.FILES )  
        if form.is_valid():
              
            obj = form.save(commit = False)
            student = request.user.student
            group = Groupe.objects.get(slug =slug)
            slugteacher=group.postteacher.slug
            post=  PostTeacher.objects.get(slug = slugteacher)
            if SubscripeTeacher.objects.filter(student = student, postteacher = post).exists():
                 messages.error(request, "User already subscripe")
                 return redirect('Posts')
            else:    
                 obj.group = Groupe.objects.get(slug=slug)
                 obj.student = student
                 obj.postteacher = PostTeacher.objects.get(slug=slugteacher)
                 place = obj.group.nombredeplace -1
                 group = Groupe.objects.filter(slug =slug)
                 group.update(slug =slug,nombredeplace = place)
                 
                 obj.save()
                 form = SubTeacher()
                 messages.success(request, "Successfully created")
                 return redirect('Posts')
          
  
    return render(request, 'student/subTeacher.html', {'form':form})  



