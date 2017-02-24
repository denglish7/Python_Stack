from django.shortcuts import render

# Create your views here.
# knows to look in templates folder
def index(request):
    return render(request, 'vinmyMVC/index.html')

def show(request):
    print(request.method)
    return render(request, 'vinmyMVC/show_users.html')
