from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

class UserRegistrationForm(UserCreationForm):
    first_name = forms.CharField(max_length=64, help_text='Enter your first name.')
    last_name = forms.CharField(max_length=64, help_text='Enter your last name.')
    email = forms.EmailField(max_length=254, help_text='Required. Enter a valid email address.')
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

class AddJournalEntry(forms.Form):
    entry = forms.CharField(help_text='What has been on your mind?', label='Entry', widget=forms.Textarea)