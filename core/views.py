from django.http import HttpResponse
from django.shortcuts import render
from core.models import Event


def get_event_location(request, event_id):
    event = Event.objects.get(id=event_id)
    return HttpResponse(f'<h4>{event.place}</h4>')
