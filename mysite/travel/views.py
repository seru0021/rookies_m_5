from django.shortcuts import render
from .models import Post
# Create your views here.

def index(request):
    return render(request, 'travel/main.html')

def post(request):
    return render(request, 'travel/post.html')

def sign_up(request):
    return render(request, 'travel/sign_up.html')

def login(request):
    return render(request, 'travel/login.html')

def search_results(request):
    return render(request, 'travel/search_results.html')

def posting_new(request):
    return render(request, 'travel/posting_new.html')

def myinfo(request):
    return render(request, 'travel/myinfo.html')

def modify_user(request):
    return render(request, 'travel/modify_user.html')

def index(request):
    posts = Post.objects.all()
    return render(request, 'travel/main.html', {'post': posts})