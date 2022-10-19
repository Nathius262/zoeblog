from django.shortcuts import render
from user.models import Account
from blog.utils import get_blog_queryset, get_category_queryset, get_blog_category_queryset
from operator import attrgetter
from blog.models import BlogPost, Category, Comment

from mptt.templatetags.mptt_tags import cache_tree_children as child
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

from django.http import JsonResponse, HttpResponse
from django.views import View

from django.core import serializers
import json


class DNSView(View):

    def get(self, request, *args, **kwargs):
        return render(request, "dns.txt")


class GoogleVerifyView(View):

    def get(self, request, *args, **kwargs):
        return render(request, "googleb1215a559aaa2a13.html")


def latest_blog_post(request):
    context= {}
    context['latest_posts'] = BlogPost.objects.order_by('-date_published')[:7],
    return context

def home_screen_view(request):
    context = {}
    post = []
    cat = []
    category = Category.objects.all()[1:4]
    for i in category:
        getCategory = str(i.category_name)
        cat.append(getCategory)

        posts = sorted(get_blog_category_queryset(getCategory), key=attrgetter('date_updated'), reverse=True)
        post.append(posts[0:3])

    accounts = Account.objects.all()

    context = {
        'popular_posts': BlogPost.objects.order_by('-hit_count_generic__hits')[:4],
        'accounts': accounts,
        'cats': cat,
        'posts': post
    }
    return render(request, "home/home.html", context)

def search_view(request):
    context = {}

    query = ""
    if request.GET:
        query = request.GET.get('q')
        context['query'] = str(query)

        posts = sorted(get_blog_queryset(query), key=attrgetter('date_updated'), reverse=True)

        # Pagination
        POSTS_PER_PAGE = 6
        page = request.GET.get('page', 1)
        post_paginator = Paginator(posts, POSTS_PER_PAGE)

        try:
            posts = post_paginator.page(page)
        except PageNotAnInteger:
            posts = post_paginator.page(POSTS_PER_PAGE)
        except EmptyPage:
            posts = post_paginator.page(post_paginator.num_pages)

        category = get_category_queryset(query)

        context = {
            'all_post': posts,
            'category':category,
            'query': query,
        }
    return render(request, 'home/search.html', context)
