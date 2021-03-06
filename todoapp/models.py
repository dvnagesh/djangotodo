from django.db import models

# Create your models here.
from django.db import models
from django.utils import timezone

class Todo(models.Model):
    author = models.ForeignKey('auth.User')
    task = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)
    due_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.task