from django.shortcuts import render,get_object_or_404 ,redirect
from .models import Product
from .forms import  ProductForm
#from django.http import Http404 

def product_list(request):
    queryset = Product.objects.all()
    context = {
        "object_list": queryset 
    }
    return render(request,"products/product_list.html",context)

def product_create(request):
    form = ProductForm(request.POST)
    if form.is_valid():
        form.save()
        form=ProductForm()
    context = {
        'form': form 
    }
    return render(request,"products/product_create.html",context)

def product_detail(request,my_id):
    obj = get_object_or_404(Product, id=my_id)
    context={
        "object":obj 
    }
    return render(request,"products/product_detail.html",context)

def product_update(request,my_id):
    obj=get_object_or_404(Product,id=my_id)
    form=ProductForm(request.POST,instance=obj)
    if form.is_valid():
        form.save()
    context = {
        'form' : form 
    }    
    return render(request,"products/product_update.html",context)

def product_delete(request,my_id):
    obj=get_object_or_404(Product,id=my_id)
    if request.method == "POST":
        obj.delete()
        return redirect('../../')
    context={
        "object" : obj 
    }
    return render(request,"products/product_delete.html",context)



    
