from django.db import models
from datetime import datetime
from pytz import timezone

class Todo(models.Model):
    title = models.CharField('Title', max_length=200)
    text = models.TextField('Description')
    created_at = models.DateTimeField(auto_now_add=True, blank=False)
    todo_time = models.DateTimeField('Assign Time', default=datetime.now, blank=False)

    def __str__(self):
        tz_dhaka = timezone('Asia/Dhaka')
        return "{} || {}".format(self.title, self.todo_time.astimezone(tz_dhaka).strftime("%b %d -- %I:%M %p"))
