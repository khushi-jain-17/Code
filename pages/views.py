from django.shortcuts import render
from django.http import HttpResponse 

# Create your views here.
def home(request):
    return render(request,'home.html',{})

def about(request):
    mycontext = {
        "job": "python django developer",
        "my_number": 1234,
        "my_list": [17,3,5,"Abc"],
        "my_html": "<h1> hello world </h1>"
    }
    return render(request,'about.html', mycontext )

def contact(request):
    return render(request,'contact.html',{'name':'telusko'})


