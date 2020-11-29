from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(JournalEntry)
admin.site.register(Goal)
admin.site.register(Project)