from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from.models import *


# Create your views here.
def index(request):
    return render(request, 'capsule/index.html')

def journal(request):
    return render(request, 'capsule/journal.html', {
        'entries': JournalEntry.objects.all()
    })

def add_entry(request):
    if request.method == 'POST':
        return HttpResponseRedirect(reverse('capsule:journal'))
    else:
        return render(request, 'capsule/add_entry.html')

def view_entry(request, entry_id):
    return render(request, 'capsule/view_entry.html', {
        'entry': JournalEntry.objects.get(pk=entry_id)
    })

def goals(request):
    return render(request, 'capsule/goals.html')

def notes(request):
    return render(request, 'capsule/notes.html')