from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
# from friendship.models import Friend, Follow
from django.http import HttpResponse, Http404,HttpResponseRedirect


# Create your views here.

def home(request, id):
    #query all images by id
    images =  Image.get_image_by_id(id=id).all()

    return render(request, 'home.html', {"images":images})

def search_results(request): 
      
    if 'image' in request.GET and request.GET["image"]:
        search_term =request.GET.get("image")
        search_images = Image.search_image(search_term)
        message = f"{search_term}"

        return render(request,'search.html',{"message":message, "searched":search_images})

    else:

        message = "You haven't searched for any term"
        return render(request, 'search.html', {"message":message})      