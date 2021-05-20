from django.db import models
from datetime import datetime

class Todo(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    todo_time = models.DateTimeField(default=datetime.now, blank=False)

    def __str__(self):
        return "{} || {}".format(self.title, str(self.todo_time.strftime("%b %d > %I:%M %p")))
