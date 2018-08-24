from django.contrib import admin
from .models import Post
from .models import Member
from .models import Logo
from .models import Description


# Register your models here.
admin.site.register(Post)
admin.site.register(Member)
admin.site.register(Logo)
admin.site.register(Description)