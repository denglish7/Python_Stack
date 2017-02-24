from django.shortcuts import render
import random
import string

def index(request):
    return render(request, "random_word/index.html")

def counter(request):
    if 'counter' in request.session:
        request.session['counter'] += 1
    else:
        request.session['counter'] = 0

    if 'randomWord' in request.session:
        request.session['randomWord'] = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(14))
    return render(request, 'random_word/index.html')


# Create your views here.
