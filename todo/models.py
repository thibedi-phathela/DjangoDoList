from django.db import models
from datetime import date

class Todo(models.Model):
    title = models.CharField(max_length=100)
    date = models.CharField(max_length=15,default=date.today)

    def __str__(self):
        return f"{self.title} - {self.date}"