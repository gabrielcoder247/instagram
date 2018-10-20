from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from . models import Image,Profile,Likes,Comments
from .email import send_welcome_email
from .forms import NewProfileForm,NewImageForm,CommentForm,LikesForm,SignUpForm
from friendship.models import Friend, Follow
from django.http import HttpResponse, Http404,HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm


# Create your views here.

def home(request):
    #query all images by id
	images = Image.get_all()
	profiles = Profile.get_all()
	current_user = request.user
	comment = CommentForm()
	like = LikesForm()
    # user = User.objects.all()
    
	return render(request, 'home.html', {"images":images,"current_user":current_user,"comment":comment,"like":like,"profiles":profiles })

def signup(request):
	if request.method == POST:
		form = SignUpForm(request.POST, request.FILES)
		if form.is_valid():
			user = form.save()
			user.refresh_from_db()
			user.save()
			username = form.cleaned_data.get('username')
			raw_password = form.cleaned_data.get('password1')
			user = authenicate(username =username, password=raw_password)
			login(request, user)
		return redirect('home')
	else:
		form = SignUpForm()
	return render(request, 'signup.html', {"form":form})		


@login_required(login_url='/accounts/login/')
def profile(request):
	images= Image.get_all()
	profiles = Profile.objects.all()
	user = User.objects.all()
	followers=len(Follow.objects.followers(request.user))
	following=len(Follow.objects.following(request.user))

	return render(request, 'profile.html', {"profiles":profiles,"user":user,"images":images})

    

@login_required(login_url='/accounts/login/')
def search_results(request): 

    #query all username to find search_term  
    if 'username' in request.GET and request.GET["username"]:
        search_term =request.GET.get("username")
        search_user = Image.search_users(search_term)
        message = f"{search_term}"

        return render(request,'search.html',{"message":message, "searched":search_user})

    else:

        message = "You haven't searched for any term"
        return render(request, 'search.html', {"message":message}) 


@login_required(login_url='/accounts/login')
def edit_profile(request):
	current_user = request.user
	if request.method == 'POST':
		form = NewProfileForm(request.POST,request.FILES, instance=request.user.profile)
		if form.is_valid():
			form.save()
			return redirect('profile')

	else:
			form = NewProfileForm()
	return render(request, 'new_profile.html',{"form":form })


@login_required(login_url='/accounts/login')
def image(request,id):

	try:
		image = Image.objects.get(pk = id)
		
	except DoesNotExist:
		raise Http404()

	current_user = request.user
	comments = Comments.get_comment(Comments,id)

	if request.method == 'POST':
		form = CommentForm(request.POST)
		if form.is_valid():
			comment = form.cleaned_data['comment']
			review = Comments()
			review.image = image
			review.user = current_user
			review.comment=comment
			review.save()
			
	else:
		form = CommentForm()
	return render(request,'image.html',{"image":image,"form":form,"comments":comments})

@login_required(login_url='/accounts/login/')
def new_image(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewImageForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.user = current_user
            image.save()
        return redirect('home_page')

    else:
        form = NewImageForm()
    return render(request, 'registration/new_image.html', {"form": form})



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


# @login_required(login_url='/accounts/login')
# def comment(request,id):
#     upload = Image.objects.get(id=id)
#     if request.method == 'POST':
#         comm=CommentForm(request.POST)
#         if comm.is_valid():
#             comment=comm.save(commit=False)
#             comment.user = request.user
#             comment.post=upload
#             comment.save()
#             return redirect('home')
#     return redirect('home')