from django.shortcuts import render, HttpResponse, redirect
from django.core.urlresolvers import reverse
from .models import Product

def index(request):
    context = {
        "products": Product.objects.all()
    }
    return render(request, "semi_restful_app/index.html", context)

def show(request, id):
    context = {
        "product": Product.objects.get(id=id)
    }
    return render(request, "semi_restful_app/show.html", context)

def new(request):

    return render(request, "semi_restful_app/new.html")

def edit(request, id):
    context = {
        "product": Product.objects.get(id=id)
    }
    return render(request, "semi_restful_app/edit.html", context)

def update(request, id):
    new_product = Product.objects.get(id=id)
    new_product.name = request.POST['name']
    new_product.description = request.POST['description']
    new_product.price = request.POST['price']
    new_product.save()
    return redirect(reverse('my_index'))

def create(request):
    new_product = Product.objects.create(name=request.POST['name'], description=request.POST['description'], price=request.POST['price'])
    print new_product
    return redirect('/')

def destroy(request, id):
    Product.objects.get(id=id).delete()
    return redirect('/')
