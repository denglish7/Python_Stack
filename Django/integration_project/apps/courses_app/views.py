from django.shortcuts import render, redirect
from .models import Course

def index(request):
    context = {
        'courses': Course.objects.all()
    }
    return render(request, "courses_app/index.html", context)

def process(request):
    created_course = Course.objects.create(name=request.POST['name'], description=request.POST['description'])
    created_course.save()

    return redirect('/')

def remove(request, id):
    context = {
        'remove_course': Course.objects.get(id=id)
    }
    return render(request, "courses_app/remove.html", context)
#
def delete(request, id):
    delete_course = Course.objects.get(id=id)
    delete_course.delete()

    return redirect('/')
