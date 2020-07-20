from rest_framework import serializers
from .models import Blogs


class BlogSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Blogs
        fields = ("id", "url", "title", "author")
