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

class AddGoal(forms.Form):
    title = forms.CharField(help_text='In a few words, what is your goal?')
    description = forms.CharField(help_text='Describe the goal', widget=forms.Textarea, blank=True)