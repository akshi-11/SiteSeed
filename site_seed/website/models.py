from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    title = models.CharField(max_length = 200)
    slug = models.SlugField()
    intro = models.TextField()
    thumb = models.ImageField(default='default.png', blank=True)
    user = models.ForeignKey(User, default=None, on_delete= models.CASCADE)

    def __str__(self):
        return self.title


