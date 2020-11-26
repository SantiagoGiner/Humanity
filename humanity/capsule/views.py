from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.core.exceptions import ObjectDoesNotExist

from .forms import *
from .models import *

# Create your views here.

# Render the home page
@login_required
def index(request):
    return render(request, 'capsule/index.html')


# Add an entry to the user's journal
@login_required
def add_entry(request):
    # Route was reached via POST, as by submitting a form
    if request.method == 'POST':
        form = AddJournalEntry(request.POST)
        # Validate the user's input in the form and add a journal entry to their journal
        if form.is_valid():
            new_entry = JournalEntry(user_id=request.user.id, entry=form.cleaned_data['entry'])
            new_entry.save()
            messages.success(request, 'Journal entry added!')
            return HttpResponseRedirect(reverse('capsule:journal'))
        # If an error occured, redirect them to add entry again
        messages.warning(request, 'Invalid input')
        return HttpResponseRedirect(reverse('capsule:add_entry'))

    # Else, user reached via GET, as by clicking a link
    return render(request, 'capsule/add_entry.html', {
        'form': AddJournalEntry()
    })

@login_required
def change_goal(request, goal_id, action):
    try:
        goal = Goal.objects.get(id=goal_id)
        old_priority = goal.priority
        if action == 'complete':
            goal.priority = 'completed'
            goal.save()
            messages.success(request, f'{old_priority.capitalize()} goal completed!')
        elif action == 'delete':
            goal.delete()
            messages.success(request, 'Goal deleted')
        else:
            messages.warning(request, 'That action on a goal is not permitted')
            return HttpResponseRedirect(reverse(f'capsule:view_goal', args=[old_priority]))
        return HttpResponseRedirect(reverse(f'capsule:view_goal', args=[old_priority]))
    except ObjectDoesNotExist:
        messages.success(request, 'That goal does not exist')
        return HttpResponseRedirect(reverse('capsule:goals'))

# Render the template for user's goals
@login_required
def goals(request):
    return render(request, 'capsule/goals.html')

@login_required
def journal(request):
    return render(request, 'capsule/journal.html', {
        'entries': JournalEntry.objects.filter(user_id=request.user.id)
    })

# Log the user in
def login_view(request):
    # Route was reached via POST, as by submitting a form
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        # Validate that the user input a correct username and password
        user = authenticate(request, username=username, password=password)
        # If so, log the user in
        if user is not None:
            login(request, user)
            messages.success(request, f'Logged in as {request.user.username}!')
            return HttpResponseRedirect(reverse('capsule:index'))
        # Else, redirect them to the login page again, informing them of the error
        else:
            messages.warning(request, 'Invalid credentials')
            return render(request, 'capsule/login.html', {
                'form': AuthenticationForm()
            })

    # Else, user reached via GET, as by clicking a link
    return render(request, 'capsule/login.html', {
        'form': AuthenticationForm()
    })

# Log the user out
def logout_view(request):
    logout(request)
    messages.success(request, 'Logged out!')
    return HttpResponseRedirect(reverse('capsule:login'))


# Render template for user's notes
@login_required
def notes(request):
    return render(request, 'capsule/notes.html')

# Create a new account for the user
def register(request):
    # Route was reached via POST, as by submitting a form
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        # Validate the user's input
        if form.is_valid():
            # Add the user to the users table
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            # Log the user in
            new_user = authenticate(request, username=username, password=password)
            login(request, new_user)
            messages.success(request, 'Registered!')
            return HttpResponseRedirect(reverse('capsule:index'))
        # If an error occured, redirect them to register again
        messages.warning(request, 'Invalid credentials. Verify that you meet all the requirements in each field')
        return HttpResponseRedirect(reverse('capsule:register'))

    # Else, user reached via GET, as by clicking a link
    return render(request, 'capsule/register.html', {
        'form': UserRegistrationForm()
    })

# View a journal entry
@login_required
def view_entry(request, entry_id):
    # Render a template with the selected entry
    return render(request, 'capsule/view_entry.html', {
        'entry': JournalEntry.objects.get(pk=entry_id)
    })

@login_required
def view_goal(request, priority):
    if request.method == 'POST':
        form = AddGoal(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            description = form.cleaned_data['description']
            new_goal = Goal(user_id=request.user.id, title=title, description=description, priority=priority)
            new_goal.save()
            messages.success(request, f'{priority.capitalize()} goal added!')
            return HttpResponseRedirect(reverse('capsule:view_goal', args=[priority]))
        messages.warning(request, 'Invalid input')
        return HttpResponseRedirect(reverse('capsule:view_goal', args=[priority]))
    if priority in ['daily', 'weekly', 'monthly', 'long-term', 'completed']:
        return render(request, 'capsule/view_goal.html', {
            'goals': Goal.objects.filter(user_id=request.user.id, priority=priority),
            'priority': priority,
            'form': AddGoal()
        })
    messages.warning(request, 'That is not a valid type of goals')
    return HttpResponseRedirect(reverse('capsule:goals'))