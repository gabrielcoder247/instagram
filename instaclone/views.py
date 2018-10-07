from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from . models import Image,Profile
# from friendship.models import Friend, Follow
from django.http import HttpResponse, Http404,HttpResponseRedirect


# Create your views here.

def home(request):
    #query all images by id
    images = Image.objects.all()
    

    return render(request, 'home.html', {"images":images,})
@login_required(login_url='/accounts/login/')
def profile(request):
    profile = Profile.objects.all()

    return render(request, 'profile.html', {"profile":profile})

    

@login_required(login_url='/accounts/login/')
def search_results(request): 

    #query all username to find search_term  
    if 'username' in request.GET and request.GET["username"]:
        search_term =request.GET.get("username")
        search_images = Image.search_image(search_term)
        message = f"{search_term}"

        return render(request,'search.html',{"message":message, "searched":search_images})

    else:

        message = "You haven't searched for any term"
        return render(request, 'search.html', {"message":message})      