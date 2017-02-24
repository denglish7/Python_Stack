from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def index(request):
    return render(request, "wall_app/index.html")

def process(request):
    if 'commentLog' not in request.session:
        request.session['commentLog'] = []
    if request.method == 'POST':
        request.session['user_comments'] = request.POST['comment']

    request.session['commentLog'].append(request.session['user_comments'])

    return render(request, "wall_app/index.html")

def reset(request):
    request.session.clear()
    return redirect('/')
