from django.db import models

# Create your models here.
class JournalEntry(models.Model):
    user_id = models.IntegerField()
    entry = models.TextField()
    date = models.DateField(auto_now_add=True)
    def __str__(self):
        return f"Journal entry from {self.date}"

class Goal(models.Model):
    user_id = models.IntegerField()
    goal = models.TextField()
    priority = models.CharField(max_length=9, default='daily')
    def __str__(self):
        if self.priority == 'long-term':
            return f"Long-term goal to: {self.goal}"
        elif self.priority == 'monthly':
            return f"Monthly goal to: {self.goal}"
        elif self.priority == 'weekly':
            return f"Weekly goal to: {self.goal}"
        else:
            return f"Daily goal to: {self.goal}"