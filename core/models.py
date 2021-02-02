from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Event(models.Model):
    title = models.CharField(max_length=70)
    description = models.TextField(blank=True, null=True)
    date = models.DateTimeField(verbose_name="Data do evento")
    created_at = models.DateTimeField(auto_now=True)
    place = models.TextField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = 'event'

    def __str__(self):
        return self.title

    def get_event_date(self):
        return self.date.strftime('%d/%m/%Y %H:%M')


