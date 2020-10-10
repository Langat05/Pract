from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.

def home(request):
    return  render(request, 'all/dashboard.html')

def about(request):
    return  render(request, 'all/about.html')  

def images(request):
    images = Image.objects.all()
    categories = Category.objects.all()
    location = Location.objects.all()
    return  render(request, 'all/images.html',{'images':images}) 

def search_category(request):
    if 'image' in request.GET and request.GET["image"]:
        search_term = request.GET.get("image")
        searched_images = Image.search_by_category(search_term)
        message = f"{search_term}"

        return render(request, 'category.html', {"message": message, "images": searched_images})

    else:
        message = "You haven't searched for any term"
        return render(request, 'category.html', {"message": message})    

    