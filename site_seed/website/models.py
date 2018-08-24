from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    title = models.CharField(max_length = 200)
    intro = models.TextField()
    achievements = models.TextField(default =None)


    user = models.ForeignKey(User, default=None, on_delete= models.CASCADE)

    def __str__(self):
        return self.title

class Member(models.Model):
    title = models.ForeignKey(Post, default = None, on_delete=models.CASCADE)
    secretary = models.CharField(max_length = 200)
    joint_secretary = models.CharField(max_length = 200)
    member = models.CharField(max_length = 1000)

class Description(models.Model):
    title = models.ForeignKey(Post, default =None, on_delete=models.CASCADE)
    description = models.TextField()

class Logo(models.Model):
    title = models.ForeignKey(Post, default =None, on_delete=models.CASCADE)
    thumb = models.ImageField(default = None, blank = True)


class Contact(models.Model):
    title = models.ForeignKey(Post, default=None, on_delete=models.CASCADE)
    email = models.EmailField()
    Contact_No= models.IntegerField()








