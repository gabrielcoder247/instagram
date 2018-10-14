from django.db import models
from django.contrib.auth.models import User
from datetime import datetime as dt

# Create your models here.


class Profile(models.Model):
    pub_date = models.DateField(auto_now_add=True)
    likes = models.IntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    profile_photo = models.ImageField(upload_to = 'profile/') 
    bio = models.TextField(max_length=255) 
    

    def find_profile(cls,first_name):
        profile = Profile.objects.filter_by_name(name__icontains=first_name).all()

        return profile


    def save_user(self):
         self.save()

    def __str__(self):
        return self.bio

  


class Image(models.Model):
    name = models.CharField(max_length=30)
    caption = models.CharField(max_length=30)
    image_comments = models.CharField(max_length=500)
    image_likes = models.PositiveIntegerField()
    pub_date = models.DateField(auto_now_add=True)
    image_path = models.ImageField(upload_to = 'images/')
    profile = models.ForeignKey('Profile', on_delete=models.CASCADE)

    def save_image(self):
        self.save()


    def delete_image(self):
        self.delete()

    @classmethod
    def update_image(cls, id, update):
        updated =cls.objects.filter(id=id).update(image = update)

        return updated
    @classmethod
    def update_caption(cls, id, caption):
        updated =cls.objects.filter(id=id).update(caption = update)

        return updated    
        

    @classmethod
    def get_image_by_id(cls, id):
        images = cls.objects.all(id = id).all()
        return images
                
        

    class meta:
        ordering = ['-pub_date'] 



    def __str__(self):
        return self.name


class Comment(models.Model):
    user = models.ForeignKey(User,null=True)
    post=models.ForeignKey(Image,related_name='comments',null=True)
    comment=models.CharField(max_length=200,null=True)

    def __str__(self):
        return self.comment

class Likes(models.Model):
    user = models.OneToOneField(User,related_name='likes_user')
    post=models.ForeignKey(Image,related_name='likes')
    likes=models.CharField(max_length=3,default='1')




    


    


    
