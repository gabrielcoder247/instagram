from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile,Image
class NewProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user','bio'] 



class NewImageForm(forms.ModelForm):
	class Meta:
		model = Image
		exclude = ['user','profile','time_updated','pub_date','name']		
