from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse


# Create your views here.
def index(request):
    return render(request, 'capsule/index.html')

def journal(request):
    return render(request, 'capsule/journal.html')

def add_entry(request):
    if request.method == 'POST':
        return HttpResponseRedirect(reverse('capsule:journal'))
    else:
        return render(request, 'capsule/add_entry.html')

def goals(request):
    return render(request, 'capsule/goals.html')

def notes(request):
    return render(request, 'capsule/notes.html')