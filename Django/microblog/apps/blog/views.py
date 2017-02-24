from django.shortcuts import render, redirect
from .models import Blog

# Create your views here.
def index(request):
  context = {
    "blog": Blog.objects.order_by('-created_at'),
  }
  print "hello"
  return render(request, "blog/index.html", context)


def process(request):
    Blog.objects.create(name=request.POST['name'], blog=request.POST['blog'])
    return redirect('/')
