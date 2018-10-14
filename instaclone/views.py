from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from . models import Image,Profile
from .email import send_welcome_email
from .forms import NewProfileForm,NewImageForm
from friendship.models import Friend, Follow
from django.http import HttpResponse, Http404,HttpResponseRedirect


# Create your views here.

def home(request):
    #query all images by id
    images = Image.objects.all()
    user = User.objects.all()
    
    return render(request, 'home.html', {"images":images,"user":user})

@login_required(login_url='/accounts/login/')
def profile(request):
    profile = Profile.objects.all()
    user = User.objects.all()
    followers=len(Follow.objects.followers(request.user))
    following=len(Follow.objects.following(request.user))

    return render(request, 'profile.html', {"profile":profile,"user":user})

    

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


@login_required(login_url='/accounts/login')
def new_profile(request):
	current_user = request.user
	if request.method == 'POST':
		form = NewProfileForm(request.POST,request.FILES, instance=request.user.profile)
		if form.is_valid():
			form.save()
			return redirect('current_profile')

	else:
			form = NewProfileForm()
	return render(request, 'new_profile.html',{"form":form })


@login_required(login_url='/accounts/login')
def new_image(request):
	current_user = request.user
	if request.method == 'POST':
		form = NewImageForm(request.POST,request.FILES)
		if form.is_valid():
			article = form.save(commit=False)
			article.user = current_user
			article.save()
			return redirect('current_profile')
	else:
			form = NewImageForm()
	return render(request, 'new_image.html',{"form":form })


@login_required(login_url='/accounts/login')
def follow_function(request,other_user):
	other_users=User.objects.get(id=other_user)
	addfollow=Follow.objects.add_follower(request.user, other_users)
	return redirect('home')    

@login_required(login_url='/accounts/login')
def unfollow_function(request,other_user):
	other_users=User.objects.get(id=other_user)
	unfollow=Follow.objects.remove_follower(request.user, other_users)
	return redirect('home')


@login_required(login_url='/accounts/login')
def otherprofile(request,others_user):
	followers=len(Follow.objects.followers(request.user))
	other_users=User.objects.get(id=others_user)
	following=len(Follow.objects.following(request.user))
	image_count=len(Image.objects.filter(user_id=other_users))
	images=Image.objects.filter(user_id=other_users)
	return render(request,'profile_other.html',{"followers":followers,"other_users":other_users,"following":following,"image_count":image_count,"images":images})