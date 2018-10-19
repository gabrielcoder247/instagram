from django.db import models
from django.contrib.auth.models import User
from datetime import datetime as dt

# Create your models here.


class Profile(models.Model):

    pub_date = models.DateField(auto_now_add=True)
    likes = models.IntegerField(default=0)
    user=models.OneToOneField(User, on_delete=models.CASCADE, blank=True, related_name="profile")
    profile_photo = models.ImageField(upload_to = 'profile/') 
    bio = models.TextField(max_length=255) 
    followers = models.ManyToManyField(User, related_name="followers_profile", blank=True)
    following = models.ManyToManyField(User, related_name="following_profile", blank=True)


    @classmethod
    def get_all(cls):
        profile = Profile.objects.all()
        return profile


    def find_profile(cls,first_name):
        profile = Profile.objects.filter_by_name(name__icontains=first_name).all()

        return profile


    def save_user(self):
         self.save()

    def delete_profile(self):
        self.delete()     


    def follow_user(self, follower):
        return self.following.add(follower)

    def unfollow_user(self, to_unfollow):
        return self.following.remove(to_unfollow)

    def is_following(self, checkuser):
        return checkuser in self.following.all()

    def get_number_of_followers(self):
        if self.followers.count():
            return self.followers.count()
        else:
            return 0

    def get_number_of_following(self):
        if self.following.count():
            return self.following.count()
        else:
            return 0
     

    def __str__(self):
        return self.user.username

  


class Image(models.Model):
    name = models.CharField(max_length=30)
    username = models.CharField(max_length=30)
    caption = models.CharField(max_length=30)
    image_comments = models.CharField(max_length=500)
    image_likes = models.PositiveIntegerField()
    pub_date = models.DateField(auto_now_add=True)
    image_path = models.ImageField(upload_to = 'images/')
    profile = models.ForeignKey('Profile', on_delete=models.CASCADE)


    @classmethod
    def get_all(cls):
        images = Image.objects.all()
        return images


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
    def search_users(cls, search_term):
        profiles = cls.objects.filter(username__icontains=search_term)
        return profiles
                
        

    class meta:
        ordering = ['-pub_date'] 



    def __str__(self):
        return self.name


class Comments(models.Model):
    user = models.ForeignKey(User,null=True)
    post=models.ForeignKey(Image,related_name='comments',null=True)
    comment=models.CharField(max_length=200,null=True)


    def get_comment(self,id):
        comments = self.objects.filter(id=id)
        return comments

    def __str__(self):
        return self.comment

class Likes(models.Model):
    user = models.OneToOneField(User,related_name='likes_user')
    post=models.ForeignKey(Image,related_name='likes')
    likes=models.CharField(max_length=3,default='1')

class Followers(models.Model):

    user = models.CharField(max_length=20, default="")
    follower = models.CharField(max_length=20, default="")





    


    


    
