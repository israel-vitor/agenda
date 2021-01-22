from django.db import models

# Create your models here.


class Event(models.Model):
    title = models.CharField(max_length=70)
    description = models.TextField(blank=True, null=True)
    date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now=True)


