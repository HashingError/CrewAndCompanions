from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def wall(request):
    return render(request, 'wall.html')

def submissions(request):
    return render(request, 'submissions.html')

def resources(request):
    return render(request, 'home.html')