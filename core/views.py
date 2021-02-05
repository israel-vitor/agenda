from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
from core.models import Event


def login_user(request):
    return render(request, 'login.html')


def logout_user(request):
    logout(request)
    return redirect('/')


def submit_login(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
    else:
        redirect('/')


def get_event_location(request, event_id):
    event = Event.objects.get(id=event_id)
    return HttpResponse(f'<h4>{event.place}</h4>')


@login_required(login_url='/login/')
def list_events(request):
    user = request.user
    events = Event.objects.filter(user=user)
    data = {'events': events}
    return render(request, 'agenda.html', data)
