from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from .models import Post
from pathlib import Path
from django.contrib import messages
from .models import CustomUser
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
            user_id = form.cleaned_data.get('user_id')
            raw_password = form.cleaned_data.get('password')
            nickname = form.cleaned_data.get('nickname')
            
            # MySQL 데이터베이스에 연결합니다.
            connection = pymysql.connect(
                host="rookies-team5-db.c3w0mgioep1e.us-west-2.rds.amazonaws.com",
                port=3306,
                user="admin",
                password="abc123123",
                database="sampledb",
                autocommit=True
            )
            cursor = connection.cursor()
            
            # 사용자 정보를 MySQL 데이터베이스에 삽입합니다.
            query = "INSERT INTO users (user_id, nickname, password) VALUES (%s, %s, %s)"
            cursor.execute(query, (user_id, nickname, raw_password)) # users 테이블
        
            # 새로운 사용자를 인증하고 로그인합니다.
            user = authenticate(username=user_id, password=raw_password)
            login(request, user)
            
            # 홈 페이지로 리다이렉트합니다.
            return redirect('index')
    else:
        form = UserCreationForm()
    return render(request, 'html/signup.html', {'form': form})

def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        
        # 사용자 인증
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            # 인증된 사용자일 경우 로그인 처리
            login(request, user)
            return redirect('index')
        else:
            # 인증되지 않은 사용자일 경우 에러 메시지 출력 혹은 재시도 요청
            # 예: return render(request, 'login.html', {'error_message': 'Invalid login'})
            pass
    return render(request, 'html/login.html')

def search_results(request):
    return render(request, 'html/search_results.html')

def posting_new(request):
    return render(request, 'html/posting_new.html')

def myinfo(request):
    return render(request, 'html/myinfo.html')

def modify_user(request):
    return render(request, 'html/modify_user.html')