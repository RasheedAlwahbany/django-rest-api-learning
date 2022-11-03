from django.shortcuts import render
from .models import Item

# Create your views here.
def addItem(request):
    Item.objects.create(name="Ahmed")
    return render(request,"index.html",{"name":"Ahmed"})

# def UpdateItem(request):
#     Item.objects.update(name="Ahmed")
#     return render(request,"index.html",{"name":"Ahmed"})

def getItem(request):
    obj=Item.objects.all()
    return render(request,"index.html",{"items":obj})