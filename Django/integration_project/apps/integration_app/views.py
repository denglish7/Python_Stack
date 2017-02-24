from django.shortcuts import render, HttpResponse, redirect
from django.db.models import Count
from ..login_and_registration_app.models import User
from ..courses_app.models import Course

def index(request):
    context = {
        "user_id": User.objects.all(),
        "course_id": Course.objects.all(),
        "courses": Course.objects.filter()
    }
    return render(request, "integration_app/index.html", context)

def add_user(request):
    user = User.objects.get(id=request.POST['myuser'])
    print user
    course = Course.objects.get(id=request.POST['mycourse'])
    print course
    course.student.add(user)

    return redirect('/')


# Create your views here.
