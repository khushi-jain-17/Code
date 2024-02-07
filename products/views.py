from django.shortcuts import render,get_object_or_404 ,redirect
from .models import Product
from .forms import  ProductForm
from django.http import Http404 
# Create your views here.

def product_detail(request):
    obj = Product.objects.get(id=1)
    context={
        'object' : obj
    }

    return render(request,'products/product_detail.html',context)

def dynamic_look(request,my_id):
    #obj=get_object_or_404(Product,id=my_id)
    #obj=Product.objects.get(id=my_id)
    try:
        obj=Product.objects.get(id=my_id)
    except Product.DoesNotExist:
        raise Http404     
    context={
        "object": obj 
    }
    return render(request,"products/product_detail.html",context)

def product_create(request):
    form = ProductForm(request.POST)
    if form.is_valid():
        form.save()
        form=ProductForm()
    context = {
        'form': form 
    }
    return render(request,"products/product_create.html",context)

def product_delete(request,my_id):
    obj=get_object_or_404(Product,id=my_id)
    if request.method == "POST":
        obj.delete()
        return redirect('../../')
    context={
        "object" : obj 
    }
    return render(request,"products/product_delete.html",context)


    
