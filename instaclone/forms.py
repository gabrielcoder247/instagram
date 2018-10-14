from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile,Image,Comments,Likes

class NewProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user','bio'] 
        widgets = {
            'tags': forms.CheckboxSelectMultiple(),
        }



class NewImageForm(forms.ModelForm):
	class Meta:
		model = Image
		exclude = ['user','profile','time_updated','pub_date','name']
        
        



class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        exclude = ['user','comment_date','image','post']

class LikesForm(forms.ModelForm):
    class Meta:
        model=Likes
        exclude=['user']
        fields=[]         		
