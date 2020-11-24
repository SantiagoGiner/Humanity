from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from .forms import *
from .models import *

# Create your views here.
@login_required(login_url='capsule:login')
def index(request):
    return render(request, 'capsule/index.html')

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            new_user = authenticate(request, username=username, password=password)
            login(request, new_user)
            messages.success(request, 'Registered!')
            return HttpResponseRedirect(reverse('capsule:index'))
        messages.warning(request, 'Invalid credentials. Verify that you meet all the requirements in each field')
        return HttpResponseRedirect(reverse('capsule:register'))
    return render(request, 'capsule/register.html', {
        'form': UserRegistrationForm()
    })

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, f'Logged in as {request.user.username}!')
            return HttpResponseRedirect(reverse('capsule:index'))
        else:
            messages.warning(request, 'Invalid credentials')
            return render(request, 'capsule/login.html', {
                'form': AuthenticationForm()
            })
    return render(request, 'capsule/login.html', {
        'form': AuthenticationForm()
    })

def logout_view(request):
    logout(request)
    messages.success(request, 'Logged out!')
    return HttpResponseRedirect(reverse('capsule:login'))

@login_required(login_url='capsule:login')
def journal(request):
    return render(request, 'capsule/journal.html', {
        'entries': JournalEntry.objects.filter(user_id=request.user.id)
    })

@login_required(login_url='capsule:login')
def add_entry(request):
    if request.method == 'POST':
        form = AddJournalEntry(request.POST)
        if form.is_valid():
            new_entry = JournalEntry(user_id=request.user.id, entry=form.cleaned_data['entry'])
            new_entry.save()
            messages.success(request, 'Journal entry added!')
            return HttpResponseRedirect(reverse('capsule:journal'))
        messages.warning(request, 'Invalid input')
        return HttpResponseRedirect(reverse('capsule:add_entry'))
    return render(request, 'capsule/add_entry.html', {
        'form': AddJournalEntry()
    })

@login_required(login_url='capsule:login')
def view_entry(request, entry_id):
    return render(request, 'capsule/view_entry.html', {
        'entry': JournalEntry.objects.get(pk=entry_id)
    })

@login_required(login_url='capsule:login')
def goals(request):
    return render(request, 'capsule/goals.html')

@login_required(login_url='capsule:login')
def notes(request):
    return render(request, 'capsule/notes.html')