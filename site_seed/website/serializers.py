from rest_framework import serializers

from .models import Post
from .models import Member
from .models import Logo
from .models import Description

class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = '__all__'

class MemberSerializer(serializers.ModelSerializer):

    class Meta:
        model = Member
        fields = '__all__'


class LogoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Logo
        fields = '__all__'

class DescriptionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Description
        fields = '__all__'
