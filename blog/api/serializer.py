from rest_framework import serializers
from ..models import BlogPost, Category

class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields= '__all__'

class BlogPostSerializer(serializers.ModelSerializer):
    author = serializers.CharField(source='author.username', read_only=True)
    category = serializers.SerializerMethodField(read_only=True)

    def get_category(self, obj):
        category_list=[]
        for item in obj.category.all():
            category_list.append(item.category_name)
        return category_list

    class Meta:
        model = BlogPost
        fields = ['title', 'body', 'image', 'category', 'author', 'date_updated', ]
