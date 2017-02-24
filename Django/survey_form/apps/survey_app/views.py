from django.shortcuts import render, HttpResponse, redirect

def index(request):
    return render(request, "survey_app/index.html")

def process(request):

    if 'counter' in request.session:
        request.session['counter'] += 1
    else:
        request.session['counter'] = 0


    if request.method == "POST":
        request.session['username'] = request.POST['name']
        request.session['dojo_location'] = request.POST['location']
        request.session['favorite_language'] = request.POST['language']
        request.session['comments'] = request.POST['comments']
    else:
        return redirect('/')
    return render(request, 'survey_app/results.html')

def results(request):
    return render(request, "survey_app/results.html")

# Create your views here.
