from django.db import models

# Create your models here.

# Database to store a journal entry
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
        return f"Journal entry from {self.date}"

# Database to store a goal
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
            return f"Long-term goal to: {self.title}"
        elif self.priority == 'monthly':
            return f"Monthly goal to: {self.title}"
        elif self.priority == 'weekly':
            return f"Weekly goal to: {self.title}"
        elif self.priority == 'daily':
            return f"Daily goal to: {self.title}"
        else:
            return f"Goal completed to: {self.title}"