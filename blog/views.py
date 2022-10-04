from django.contrib import messages
from django.contrib.auth import login
from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Count
from hitcount.views import HitCountDetailView
from django.http import JsonResponse, HttpResponse
from django.core import serializers
import json

from .models import BlogPost, Category, Like, Comment
from .forms import CreateBlogPostForm, EditBlogPostForm
from .utils import commentFormData, likeFormData, mustAuthenticate
from user.models import Account
from django.views.generic import ListView
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from operator import attrgetter


# all categories
def category_list(request):
    category = Category.objects.all()
    context = list(category.values())

    return JsonResponse(context, safe=False)

# create blog
def create_blog_view(request):
    mustAuthenticate(request)

    form = CreateBlogPostForm(request.POST or None, request.FILES or None)
 
    try:
        if form.is_valid():
            a = form.cleaned_data['category']
            
            obj = form.save(commit=False)

            author = request.user
            obj.author = author        
            obj.save()
            for i in a:
                obj.category.add(i)
            obj.save()
            messages.success(request, f'"{obj.title}" created!')
            form = CreateBlogPostForm()
    except:
        messages.success(request, f'"{obj.title}" already exist! you can rename {obj.title} to {obj.title}_part 2')
       
    context = {
        'form': form,
    }

    return render(request, "blog/create_blog.html", context)


# edit blog post
def edit_blog_view(request, slug):
    context = {}

    mustAuthenticate(request)

    blog_post = get_object_or_404(BlogPost, slug=slug)

    if request.POST:
        form = EditBlogPostForm(request.POST, request.FILES, instance=blog_post)

        if form.is_valid():
            obj = form.save(commit=False)
            obj.save()

            messages.success(request, "Updated Successfully!")

    form = EditBlogPostForm(
        initial={
            "title": blog_post.title,
            "category": blog_post.category.all(),
            "body": blog_post.body,
            "image": blog_post.image_url,
        }
    )

    context['form'] = form
    return render(request, 'blog/edit_blog.html', context)


POSTS_PER_PAGE = 9


# blog pages
def blog_view(request):
    context = {}

    all_post = sorted(BlogPost.objects.all(), key=attrgetter('date_updated'), reverse=True)
    context['all_post'] = all_post

    # Pagination
    page = request.GET.get('page', 1)
    all_post_paginator = Paginator(all_post, POSTS_PER_PAGE)

    try:
        all_post = all_post_paginator.page(page)
    except PageNotAnInteger:
        all_post = all_post_paginator.page(POSTS_PER_PAGE)
    except EmptyPage:
        all_post = all_post_paginator.page(all_post_paginator.num_pages)
    context['all_post'] = all_post

    return render(request, 'blog/blog.html', context)


class DetailPostView(HitCountDetailView):
    model = BlogPost
    template_name = 'blog/detail_blog.html'
    context_object_name = 'post'
    slug_field = 'slug'
    count_hit = True

    def get_queryset(self):
        posts = BlogPost.objects.all().filter(slug=self.kwargs['slug'])
        return posts

    def get_context_data(self, **kwargs):
        context = super(DetailPostView, self).get_context_data(**kwargs)
        user = self.request.user
        post = self.get_queryset()
        post = post.first()

        cat = post.category.all()
        related_post = BlogPost.objects.filter(category__in=cat).exclude(slug=self.kwargs['slug'])
        related_post = related_post.annotate(tag_count=Count('category')).order_by('-tag_count', '-date_published')

        comments = post.comments.all()

        context.update({
            'popular_posts': BlogPost.objects.order_by('-hit_count_generic__hits')[:3],
            'related_post':related_post[:1],
            'comments': comments,
            'user': user,
            'cat': cat,
        })
        return context


def likesCount(request):
    postId = request.GET

    a= []
    for i in postId:
        
        post = BlogPost.objects.get(id=postId[i])
        likes = Like.objects.all().filter(postLike=post, value='Like').count()
        dislikes = Like.objects.all().filter(postLike=post, value='Unlike').count()
        comments = Comment.objects.all().filter(post=post).count()
        context = {
            'likes':str(likes),
            'dislikes':str(dislikes),
            'comments':str(comments)
        }
        a.append(context)
    return JsonResponse(a, safe=False)

def like_view(request):
    
    if request.method == 'POST':
        likeFormData(request)
    return JsonResponse("success", safe=False)


def comment_view(request):
    if request.POST:
        commentFormData(request)
    return JsonResponse("comment success", safe=False)

def commet_reply_view(request):
    print(request.POST)
    return JsonResponse('yes', safe=False)

def delete_post(request):
    posts = request.POST['deleteData']
    post = BlogPost.objects.get(id=posts)
    post.delete()

    return JsonResponse('post deleted', safe=False)


# category view
class CatListView(ListView):
    template_name = 'blog/category.html'
    context_object_name = 'catlist'

    def get_queryset(self):
        content = {}

        post = sorted(BlogPost.objects.all().filter(
            category__category_name=self.kwargs['category']), key=attrgetter('date_updated'), reverse=True)

        content = {
            'cat': self.kwargs['category'],
            'posts': post,
        }

        return content


# create category view
def create_category_view(request):
    obj = json.loads(request.POST['catVal'])
    cat, created = Category.objects.get_or_create(category_name=obj)
    if not created:
        content = "this category name already exist in the database!"
    else:
        content = "created category Successfully"

    return JsonResponse(content, safe=False)
