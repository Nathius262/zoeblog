import os
from allauth.socialaccount.models import SocialAccount
from django.conf import settings
from django.http import JsonResponse

from django.contrib import messages
from .forms import AccountUpdateForm
from .models import Account, Follower
from django.shortcuts import render, redirect, get_object_or_404

from blog.models import BlogPost


# Create your views here.


def account_view(request):
    if not request.user.is_authenticated:
        return redirect("account_login")

    context = {}

    if request.POST:
        form = AccountUpdateForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, "Your profile was updated successfully!")
    
    else:
        form = AccountUpdateForm(
            initial={
                "email": request.user.email,
                "username": request.user.username,
                "name": request.user.name,
                "picture": request.user.picture,
            }
        )
    context['account_form'] = form
    return render(request, 'user/account.html', context)

def profile_view(request, user):
    profile_id = get_object_or_404(Account, username=user)
    profile_obj = Account.objects.filter(username=profile_id)

    current_user = profile_obj.first()
    logged_in_user = request.user

    post_obj = BlogPost.objects.all().filter(author=profile_id)
    socialacct =  SocialAccount.objects.all().filter(user=request.user)
    a=[]
    for i in socialacct:
        a.append(i.provider)

    content = {
        'profile': profile_obj,
        'post': post_obj,
        'current_user': current_user,
        'logged_in_user': logged_in_user,
        'socialuser': sorted(a, reverse=False),
    }
    return render(request, 'user/profile.html', content)

def follow_view_get(request):
    user_profile = request.GET.get('user_profile')
    profile_id = Account.objects.get(username=user_profile)
    profile_obj = Account.objects.filter(username=profile_id)

    current_user = profile_obj.first()
    logged_in_user = request.user

    post_obj = BlogPost.objects.all().filter(author=profile_id)
    followers = Follower.objects.all().filter(user=profile_id)
    following = Follower.objects.all().filter(follower=profile_id)

    user_follow = Follower.objects.all().filter(user=profile_id)
    user_follow_list = []
    for i in user_follow:
        user_follow = i.follower
        user_follow_list.append(user_follow)
    if logged_in_user.username in user_follow_list:
        follower_value_button = 'unfollow'
    else:
        follower_value_button = 'follow'

    context={
        'followers':followers.count(),
        'following':following.count(),
        'post_no':post_obj.count(),
        'follower_value_button':follower_value_button,
    }

    return JsonResponse(context, safe=False)

def follow_view(request):
    if request.POST:
        value = request.POST['value']
        user = request.POST['user']
        follower = request.POST['follower']
        if value == 'follow':
            save_follow = Follower.objects.create(follower=follower, user=user)
            save_follow.save()
        else:
            remove_follow = Follower.objects.filter(follower=follower, user=user)
            remove_follow.delete()
    return JsonResponse('success', safe=False)

def login_status_view(request):
    status = request.POST['status']
    current_user = request.POST['user']
    user = Account.objects.get(username=current_user)
    if status == "online":
        user.login_status = True
    elif status == "offline":
        user.login_status = False

    user.save()
    return JsonResponse('success', safe=False)

def must_authenticate_view(request):
    return render(request, 'user/must_authenticate.html')