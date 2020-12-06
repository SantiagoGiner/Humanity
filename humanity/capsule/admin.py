# Django admin page
from django.contrib import admin
from .models import *

# Register all models of the application
admin.site.register(JournalEntry)
admin.site.register(Goal)
admin.site.register(Project)
admin.site.register(ProjectLog)
admin.site.register(MiniCapsule)
admin.site.register(Book)
admin.site.register(BookNote)