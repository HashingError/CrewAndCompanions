from django.shortcuts import render, redirect
from .models import Letter
from django.views.generic import FormView
from .forms import LetterForm

# Create your views here.
def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')


def wall(request):
    qs = Letter.objects.exclude(publish=False)
    return render(request, 'wall.html', {'qs': qs})


def resources(request):
    return render(request, 'home.html')


def submissions(request):
    if request.method == 'POST':
        form = LetterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('wall')
    else:
        form = LetterForm()
    return render(request, 'letter_form.html', {'form': form})