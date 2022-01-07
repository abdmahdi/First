from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'Home/Home.html')

def error_404(request, exception):
    return render(request, 'Home/404.html')

def error_500(request, exception):
    return render(request, 'Home/500.html')
def check():
    pass