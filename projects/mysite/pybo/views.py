from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from .models import Post
from pathlib import Path
import pymysql


def index(request):
    posts = Post.objects.all()
    return render(request, 'html/main.html', {'posts': posts})

def post(request):
    return render(request, 'html/post.html')

def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            # 사용자가 입력한 데이터를 가져옵니다.
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            email = form.cleaned_data.get('email')
            
            # MySQL 데이터베이스에 연결합니다.
            connection = pymysql.connect(
                host="localhost",
                port=3306,
                user="root",
                password="tkdwogn",
                database="sampledb",
                autocommit=True
            )
            cursor = connection.cursor()
            
            # 사용자 정보를 MySQL 데이터베이스에 삽입합니다.
            query = "INSERT INTO members (member_name, member_email) VALUES (%s, %s)"
            cursor.execute(query, (username, email))
            
            # 새로운 사용자를 인증하고 로그인합니다.
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            
            # 홈 페이지로 리다이렉트합니다.
            return redirect('index')
    else:
        form = UserCreationForm()
    return render(request, 'html/signup.html', {'form': form})

def login(request):
    return render(request, 'html/login.html')

def search_results(request):
    return render(request, 'html/search_results.html')

def posting_new(request):
    return render(request, 'html/posting_new.html')

def myinfo(request):
    return render(request, 'html/myinfo.html')

def modify_user(request):
    return render(request, 'html/modify_user.html')