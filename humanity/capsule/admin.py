from django.contrib import admin
from .models import *

# Register the models of the application
admin.site.register(JournalEntry)
admin.site.register(Goal)
admin.site.register(Project)
admin.site.register(projectLog)