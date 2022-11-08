from rest_framework import serializers
from ..models import BlogPost

class BlogPostSerializer(serializers.ModelSerializer):
    author = serializers.CharField(source='author.username', read_only=True)

    class Meta:
        model = BlogPost
        fields = ['title', 'body', 'image', 'category', 'author', 'date_updated', ]