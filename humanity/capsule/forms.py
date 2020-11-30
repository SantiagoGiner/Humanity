from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

# Modify the Django UserCreationForm so as to include first name, last name, and email
class UserRegistrationForm(UserCreationForm):
    first_name = forms.CharField(max_length=64, help_text='Enter your first name.')
    last_name = forms.CharField(max_length=64, help_text='Enter your last name.')
    email = forms.EmailField(max_length=254, help_text='Required. Enter a valid email address.')
    # Save these new fields
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

# Form to add a journal entry
class AddJournalEntry(forms.Form):
    entry = forms.CharField(help_text='What has been on your mind?', widget=forms.Textarea)

# Form to add a new goal
class AddGoal(forms.Form):
    title = forms.CharField(help_text='In a few words, what is your goal?')
    description = forms.CharField(help_text='Describe the goal (optional)', widget=forms.Textarea, required=False)

# Declare an input class that accepts a date
class DateInput(forms.DateInput):
    input_type = 'date'

# Form to add a new project
class AddProject(forms.Form):
    # Only allow these choices of project status
    STATUS_CHOICES = [
        ('c', 'Completed'),
        ('i', 'In progess'),
        ('s', 'Stopped')
    ]
    title = forms.CharField(help_text='What is the title of your project?')
    description = forms.CharField(help_text='Provide a project description', widget=forms.Textarea)
    finish_date = forms.DateField(help_text='When do you want to have the project done?', 
        widget=DateInput())
    status = forms.CharField(help_text='What is the current status of the project?', 
        widget=forms.Select(choices=STATUS_CHOICES))
    other_info = forms.CharField(help_text='Any other important information about the project?',
        widget=forms.Textarea, required=False)

# Form to add a project log
class addProjectLog(forms.Form):
    log = forms.CharField(help_text='Project log', widget=forms.Textarea)