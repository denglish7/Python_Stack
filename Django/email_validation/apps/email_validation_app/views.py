from django.shortcuts import render, redirect
from .models import Email
from django.contrib import messages

def index(request):
    return render(request, "email_validation_app/index.html")

def process(request):
    res = Email.objects.add_email(request.POST)

    if res["added"]:
        messages.success(request, "The email address you entered ( {} ) is a VALID email address! Thank you!".format(res["new_email"].email))
    else:
        for error in res["errors"]:
            messages.error(request, error)
            return redirect('/')

    return redirect('/success')

def success(request):
    context = {
        'list_of_emails': Email.objects.all(),
    }
    return render(request, "email_validation_app/success.html", context)
# Create your views here.
