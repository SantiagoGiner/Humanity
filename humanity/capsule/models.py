from django.db import models

# Create your models here.
class Client(models.Model):
    name = models.CharField(max_length=64)
    def __str__(self):
        return f"{self.name}"

class JournalEntry(models.Model):
    client_id = models.ForeignKey(Client, on_delete=models.CASCADE, related_name="journal_entry")
    entry = models.TextField()
    date = models.DateField(auto_now_add=True)
    def __str__(self):
        return f"Journal entry #{self.id}: {self.date}"

class Goal(models.Model):
    client_id = models.ForeignKey(Client, on_delete=models.CASCADE, related_name="goal")
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
