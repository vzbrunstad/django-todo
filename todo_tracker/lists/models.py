from django.db import models

class List(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200)

    def __str__(self):
        return f"ID: {self.id} Title: {self.title}"