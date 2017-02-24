from django.shortcuts import render, HttpResponse, redirect
from datetime import datetime


# Create your views here.
def index(request):
    context = {
    "dateTime":datetime.now()
    }
    return render(request, "timedisplay/index.html", context )
