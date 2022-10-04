import json
from .models import BlogPost, Comment, Like, Category
from django.db.models import Q
from django.shortcuts import redirect, get_object_or_404

# GET POST BASED ON CATEGORY FUNCTION
def get_blog_category_queryset(query=None):
    queryset = []
    queries = query.split(" ")
    for q in queries:
        posts = BlogPost.objects.all().filter(
            Q(category__category_name__icontains=q)
        ).distinct()
        for post in posts:
            queryset.append(post)
    return list(set(queryset))

# SEARCH POST FUNCTION
def get_blog_queryset(query=None):
    queryset = []
    queries = query.split(" ")
    for q in queries:
        posts = BlogPost.objects.all().filter(
            Q(title__icontains=q) |
            Q(body__icontains=q)
        ).distinct()
        for post in posts:
            queryset.append(post)
    return list(set(queryset))

# SEARCH CATEGORY FUNCTION
def get_category_queryset(query=None):
    queryset = []
    queries = query.split(" ")
    for q in queries:
        category = Category.objects.all().filter(
            Q(category_name__icontains=q)
        ).distinct()
        for cat in category:
            queryset.append(cat)
    return list(set(queryset))

def likeFormData(request):
    slug = request.POST['slug']        
    post_id = request.POST['post_id']
    post_value = request.POST['value']

    post = BlogPost.objects.get(id=post_id)
    user = request.user

    like, created = Like.objects.get_or_create(user=user, postLike_id=post_id)

    obj = like
    
    if created:
        like.value = post_value
    else:
        if post_value == obj.value:
            like = like.delete()
        else:     
            like.value = post_value
    like.save()

def commentFormData(request):
    pass
    user = request.user

    obj = json.loads(request.POST['comment_data'])
    post = BlogPost.objects.get(id=obj['post'])
    c = Comment.objects.all().filter(id=int(obj['parent']))
    if user.is_authenticated:
        comment = Comment.objects.create(
            post=post,
            parent=c.first(),
            name_comment=user.name,
            email_comment=user.email,
            username_comment=user.username,
            content=obj['content']

            )
    else:
        comment = Comment.objects.create(
            post=post,
            parent=c.first(),
            name_comment=obj['name_comment'],
            email_comment=obj['email_comment'],
            username_comment=obj['username_comment'],
            content=obj['content'],
            

            )
