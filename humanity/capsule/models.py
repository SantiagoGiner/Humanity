from django.db import models

# Create your models here.

# Table to store a journal entry
class JournalEntry(models.Model):
    # Reference a user_id so that the entry is unique to the user themself
    user_id = models.IntegerField()
    entry = models.TextField()
    date = models.DateField(auto_now_add=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    # Order the entries by date added
    class Meta:
        ordering = ('-created',)
    def __str__(self):
        return f'Journal entry from {self.date}'

# Table to store a goal
class Goal(models.Model):
    user_id = models.IntegerField()
    title = models.TextField()
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    # Add a priority to the goal
    priority = models.CharField(max_length=9, default='daily')
    # Order the goals by date added
    class Meta:
        ordering = ('-created',)
    def __str__(self):
        if self.priority == 'long-term':
            return f'Long-term goal to: {self.title}'
        elif self.priority == 'monthly':
            return f'Monthly goal to: {self.title}'
        elif self.priority == 'weekly':
            return f'Weekly goal to: {self.title}'
        elif self.priority == 'daily':
            return f'Daily goal to: {self.title}'
        else:
            return f'Goal completed to: {self.title}'

# Table to store a project
class Project(models.Model):
    # Only allow these options for project status
    STATUS_CHOICES = [
        ('c', 'Completed'),
        ('i', 'In progess'),
        ('s', 'Stopped')
    ]
    user_id = models.IntegerField()
    title = models.CharField(max_length=64)
    description = models.TextField()
    finish_date = models.DateField()
    status = models.CharField(choices=STATUS_CHOICES, max_length=11)
    other_info = models.TextField()
    # Order projects by date added
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    class Meta:
        ordering = ('-created',)
    def __str__(self):
        return f'Project: {self.title}'

# Table to store a project log
class ProjectLog(models.Model):
    user_id = models.IntegerField()
    # Reference a specific project, using the project's primary key
    project_id = models.IntegerField()
    log = models.TextField()
    date = models.DateField(auto_now_add=True)
    # Order the logs by date added
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    class Meta:
        ordering = ('-created',)
    def __str__(self):
        return f'Project log from {self.date}'

class MiniCapsule(models.Model):
    user_id = models.IntegerField()
    content = models.TextField()
    date_added = models.DateField(auto_now_add=True)
    time = models.DateField()
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    class Meta:
        ordering = ('-created',)
    def __str__(self):
        return f'Mini Time Capsule from {self.date_added}'