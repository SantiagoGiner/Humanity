from datetime import date

from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.core.exceptions import ObjectDoesNotExist

from .forms import *
from .models import *


STATUS_CHOICES = ['i', 'c', 's']


# Render the home page
@login_required
def index(request):
    return render(request, 'capsule/index.html')


# Add a book to the user's library
@login_required
@csrf_exempt
def add_book(request):
    # User reached via POST, as by submitting a form to add a book
    if request.method == 'POST':
        try:
            # If book is already in Book table, then user already owns it
            if Book.objects.get(user_id=request.user.pk, title=request.POST['title']):
                messages.warning(request, f'{request.POST["title"]} is already in your library')
                # Redirect the user to add another
                return HttpResponseRedirect(reverse('capsule:add_book'))
        # If book is not in user's library, then add it
        except Book.DoesNotExist:
            Book(user_id=request.user.pk, title=request.POST['title'], authors=request.POST['author'],
                 cover_photo=request.POST['cover']).save()
            messages.success(request, f'{request.POST["title"]} was added to your library!')
            return HttpResponseRedirect(reverse('capsule:library'))
    # Else, user reached via GET: render a template to search for new books
    return render(request, 'capsule/add_book.html')


# Mark a goal as completed or delete it entirely
@login_required
def change_goal(request, goal_id, action):
    try:
        # Get information from the goal passed to the function
        goal = Goal.objects.get(pk=goal_id)
        old_priority = goal.priority
        if action == 'complete':
            # Change the priority of the goal to completed
            goal.priority = 'completed'
            goal.save()
            messages.success(request, f'{old_priority.capitalize()} goal completed!')
        elif action == 'delete':
            # Delete the goal from the database
            goal.delete()
            messages.success(request, 'Goal deleted')
        else:
            # Check for unavailable action on goal
            messages.warning(request, 'That action on a goal is not permitted')
            return HttpResponseRedirect(reverse(f'capsule:view_goal', args=[old_priority]))
        # Redirect the user to the goals page they were in
        return HttpResponseRedirect(reverse(f'capsule:view_goal', args=[old_priority]))
    # If goal no longer exists, inform the user and redirect them to main goals page
    except ObjectDoesNotExist:
        messages.success(request, 'That goal does not exist')
        return HttpResponseRedirect(reverse('capsule:goals'))


# Method for updating/deleting a project
@login_required
def change_project(request, project_id, action):
    try:
        # Get the user's input and validate it
        form = AddProject(request.POST)
        project = Project.objects.get(pk=project_id)
        if form.is_valid() and action == 'update':
            if form.cleaned_data['status'] in STATUS_CHOICES:
                # Update the information in the database with new values
                project.title = form.cleaned_data['title']
                project.description = form.cleaned_data['description']
                project.status = form.cleaned_data['status']
                project.finish_date = form.cleaned_data['finish_date']
                project.other_info = form.cleaned_data['other_info']
                project.save()
                messages.success(request, 'Project updated!')
            # If input is not valid, inform the user
            else:
                messages.warning(request, 'Invalid input')
            # Redirect user to specific project page
            return HttpResponseRedirect(reverse('capsule:view_project', args=[project_id]))
        elif action == 'delete':
            # Delete the project from database and redirect user to projects page
            project.delete()
            messages.success(request, 'Project deleted!')
            return HttpResponseRedirect(reverse('capsule:projects'))
        # User requested another, unavailable action
        else:
            messages.warning(request, 'Action not permitted')
            return HttpResponseRedirect(reverse('capsule:projects'))
    # Else, project does not exist
    except ObjectDoesNotExist:
        messages.success(request, 'That project does not exist')
        return HttpResponseRedirect(reverse('capsule:projects'))


# Delete account
@login_required
def delete(request):
    # Delete the user's account and user's data from all tables
    User.objects.get(pk=request.user.pk).delete()
    JournalEntry.objects.filter(user_id=request.user.pk).delete()
    Goal.objects.filter(user_id=request.user.pk).delete()
    Project.objects.filter(user_id=request.user.pk).delete()
    ProjectLog.objects.filter(user_id=request.user.pk).delete()
    MiniCapsule.objects.filter(user_id=request.user.pk).delete()
    Book.objects.filter(user_id=request.user.pk).delete()
    messages.success(request, 'Account deleted. We hope you enjoyed the site!')
    return HttpResponseRedirect(reverse('capsule:login'))


# Render the template for user's goals
@login_required
def goals(request):
    return render(request, 'capsule/goals.html')


# Render a template with the user's journal entries
@login_required
def journal(request):
    # User reached via POST, as by submitting the add entry form
    if request.method == 'POST':
        form = AddJournalEntry(request.POST)
        # Validate the user's input in the form and add a journal entry to their journal
        if form.is_valid():
            new_entry = JournalEntry(user_id=request.user.pk, entry=form.cleaned_data['entry'])
            new_entry.save()
            messages.success(request, 'Journal entry added!')
            return HttpResponseRedirect(reverse('capsule:journal'))
        # If an error occured, redirect them to add entry again
        messages.warning(request, 'Invalid input')
        return HttpResponseRedirect(reverse('capsule:journal'))
    # Else user reached via GET, so display the current journal entries
    return render(request, 'capsule/journal.html', {
        'entries': JournalEntry.objects.filter(user_id=request.user.pk),
        'form': AddJournalEntry()
    })


# Display the user's books
@login_required
def library(request, book_id=''):
    # User reached via POST, as by clicking a button to delete a book
    if request.method == 'POST':
        # If the book is in user's library, delete it
        try:
            Book.objects.get(pk=book_id).delete()
            messages.success(request, 'Book deleted!')
        # Else, user does not own the book
        except Book.DoesNotExist:
            messages.warning(request, 'That book is not in your library')
        # Redirect them to library through GET
        return HttpResponseRedirect(reverse('capsule:library'))
    # User reached through GET: find the user's books and display them
    books = Book.objects.filter(user_id=request.user.pk)
    return render(request, 'capsule/library.html', {
        'books': books
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


# Mini time capsules
@login_required
def mini_capsule(request):
    # User reached via POST, as by submitting a form to add a capsule
    if request.method == 'POST':
        # Get user's input and validate it
        form = addMiniCapsule(request.POST)
        if form.is_valid():
            content = form.cleaned_data['content']
            time = form.cleaned_data['time']
            # Save the capsule and redirect user
            MiniCapsule(user_id=request.user.pk, content=content, time=time).save()
            messages.success(request, f'Mini time capsule added! It will be visible again on {time}')
            return HttpResponseRedirect(reverse('capsule:mini_capsule'))
    # User reached via GET
    capsules = MiniCapsule.objects.filter(user_id=request.user.pk)
    today = date.today()
    day, month, year = int(today.strftime('%d')), int(today.strftime('%m')), int(today.strftime('%Y'))
    # List to contain unlocked capsules, i.e. capsules that can be viewed
    unlocked = []
    for capsule in capsules:
        # If the current year is greater than the designated year, add capsule to unlocked
        if year > int(capsule.time.year):
            unlocked.append(capsule)
        # If the current year is the same as the designated one
        else:
            # If the month is greater than the designated one, add capsule to unlocked
            if month > int(capsule.time.month):
                unlocked.append(capsule)
            # If designated month equals current month and day is greater than/equal 
            # to designated day, add capsule to unlocked
            elif month == int(capsule.time.month) and day >= int(capsule.time.day):
                unlocked.append(capsule)

    # Render a template with capsules that should be viewed
    return render(request, 'capsule/mini.html', {
        'capsules': unlocked,
        'form': addMiniCapsule()
    })


# View of user's projects
@login_required
def projects(request):
    # User reached via POST, as by submitting a form to add a project
    if request.method == 'POST':
        # Get the user's input and validate it
        form = AddProject(request.POST)
        if form.is_valid():
            # Create new project with user's input
            title = form.cleaned_data['title']
            description = form.cleaned_data['description']
            finish_date = form.cleaned_data['finish_date']
            status = form.cleaned_data['status']
            other_info = form.cleaned_data['other_info']
            # Ensure status is valid
            if status in STATUS_CHOICES:
                new_project = Project(user_id=request.user.pk, title=title, description=description,
                                      finish_date=finish_date, status=status, other_info=other_info)
                # Save the project and redirect user
                new_project.save()
                messages.success(request, f'{title} added to your projects!')
                return HttpResponseRedirect(reverse('capsule:projects'))
            # Else, status was not valid
            messages.warning(request, 'Invalid input')
            return HttpResponseRedirect(reverse('capsule:projects'))
    # User reached via GET, as by clicking a link
    projects = Project.objects.filter(user_id=request.user.pk)
    return render(request, 'capsule/projects.html', {
        'form': AddProject(),
        'projects': projects
    })


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
        messages.warning(request, 
                         'Verify that you meet all of the requirements in each field!')
        return HttpResponseRedirect(reverse('capsule:register'))

    # Else, user reached via GET, as by clicking a link
    return render(request, 'capsule/register.html', {
        'form': UserRegistrationForm()
    })


# View or delete a mini time capsule
@login_required
def view_capsule(request, capsule_id):
    # User reached via POST, as by submitting a form to delete the mini capsule
    if request.method == 'POST':
        # Delete the capsule with the id provided
        MiniCapsule.objects.get(pk=capsule_id).delete()
        messages.success(request, 'Mini time capsule deleted')
        return HttpResponseRedirect(reverse('capsule:mini_capsule'))
    # User reached via GET: render a template with the requested capsule
    return render(request, 'capsule/view_capsule.html', {
        'capsule': MiniCapsule.objects.get(pk=capsule_id)
    })


# View a journal entry
@login_required
def view_entry(request, entry_id, action=''):
    # User reached via POST, as by submitting a form to update entry
    entry = JournalEntry.objects.get(pk=entry_id)
    if request.method == 'POST':
        # Action is to update the current journal entry
        if action == 'update':
            # Update the entry with new text
            entry.entry = request.POST['entry']
            entry.save()
            messages.success(request, f'{entry} updated!')
        # Action is to delete the current journal entry
        elif action == 'delete':
            # Delete the entry from the database
            entry.delete()
            messages.success(request, f'Entry deleted')
        # Check for attempt at other, unavailable action
        else:
            messages.warning(request, 'That action is not permitted')
        return HttpResponseRedirect(reverse('capsule:journal'))

    # Else, user reached via GET, so render a template with the selected entry
    return render(request, 'capsule/view_entry.html', {
        'entry': entry,
        'form': AddJournalEntry(initial={'entry': entry.entry})
    })


# Show the user's goals or add a new goal
@login_required
def view_goal(request, priority):
    # User reached via POST, as by submitting a form to add a goal
    if request.method == 'POST':
        form = AddGoal(request.POST)
        # Check for valid inputs and add the goal to the database
        if form.is_valid():
            title = form.cleaned_data['title']
            description = form.cleaned_data['description']
            new_goal = Goal(user_id=request.user.pk, title=title, 
                            description=description, priority=priority)
            new_goal.save()
            # Redirect the user to the specific goals page, informing of success
            messages.success(request, f'{priority.capitalize()} goal added!')
            return HttpResponseRedirect(reverse('capsule:view_goal', args=[priority]))
        # Else input was invalid, redirect user and inform them of this
        messages.warning(request, 'Invalid input')
        return HttpResponseRedirect(reverse('capsule:view_goal', args=[priority]))
    # Else, user reached via GET, as by clicking a link
    if priority in ['daily', 'weekly', 'monthly', 'long-term', 'completed']:
        return render(request, 'capsule/view_goal.html', {
            'goals': Goal.objects.filter(user_id=request.user.pk, priority=priority),
            'priority': priority,
            'form': AddGoal()
        })
    # If the type of goals is not valid, redirect user and inform them of this
    messages.warning(request, 'That is not a valid type of goals')
    return HttpResponseRedirect(reverse('capsule:goals'))


# View of project log
@login_required
def view_log(request, project_id, log_id):
    log = ProjectLog.objects.get(pk=log_id)
    # User reached via POST, as by submitting the form to delete a log
    if request.method == 'POST':
        # Delete project log
        log.delete()
        messages.success(request, f'{log} deleted')
        return HttpResponseRedirect(reverse('capsule:view_project', args=[project_id]))
    # User reached via GET: render template with log
    return render(request, 'capsule/log.html', {
        'log': log,
        'project_id': project_id
    })


# View of a specific project
@login_required
def view_project(request, project_id):
    # User reached via POST, as by submitting a form to add a log
    if request.method == 'POST':
        # Get user's input and validate it
        form = addProjectLog(request.POST)
        if form.is_valid():
            log = ProjectLog(user_id=request.user.pk, project_id=project_id,
                             log=form.cleaned_data['log'])
            # Save the log in the database
            log.save()
            messages.success(request, 'Project log added!')
            return HttpResponseRedirect(reverse('capsule:view_project', args=[project_id]))
    # User reached via GET: render a template with the project information
    project = Project.objects.get(pk=project_id)
    return render(request, 'capsule/view_project.html', {
        'project': project,
        'project_form': AddProject(initial={
            'title': project.title,
            'description': project.description,
            'finish_date': project.finish_date,
            'status': project.status,
            'other_info': project.other_info
        }),
        'logs': ProjectLog.objects.filter(user_id=request.user.pk, project_id=project_id),
        'log_form': addProjectLog()
    })