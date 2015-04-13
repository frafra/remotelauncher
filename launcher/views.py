from django.shortcuts import render
from django.http import HttpResponse
from launcher.models import Application

import shlex
import subprocess

def index(request):
    applications = Application.objects.all().filter(enabled=True)
    return render(request, 'launcher/index.html', {
        'applications':applications,
    })

def start(request, name):
    application = Application.objects.get(name=name)
    subprocess.Popen(shlex.split(application.command))
    return HttpResponse('OK')
