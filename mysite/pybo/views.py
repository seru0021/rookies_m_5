from django.shortcuts import render, redirect,  get_object_or_404
from django.contrib.auth import authenticate, login
from pathlib import Path
from .models import CustomUser
from django.contrib.auth.models import User
from django.http import JsonResponse
from .models import Post
from .forms import PostForm
from django.utils import timezone
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.http import HttpResponse

#######################################################################
#SQL 인젝션 금지 문자 필터링
def process_user_input(request):
    if request.method == 'POST':
        user_input = request.POST.get('user_input', '')  # 사용자 입력 가져오기
        filtered_input = filter_input(user_input)  # 입력 필터링
        # 여기서 필터링된 입력을 사용하여 원하는 작업을 수행합니다.
        return HttpResponse('Filtered input: ' + filtered_input)
    else:
        return HttpResponse('Only POST requests are allowed')

def filter_input(input_string):
    forbidden_chars = ["'", '"', ';', '-']  # 금지할 특수 문자 목록
    filtered_string = ''.join(char for char in input_string if char not in forbidden_chars)
    return filtered_string
#######################################################################

def index(request):
    posts = Post.objects.all()
    return render(request, 'main.html', {'posts': posts})

def search_results(request):
    return render(request, 'search_results.html')

@login_required(login_url='common:login')
def post(request):
    kw = request.GET.get('kw', '')  # 검색어
    posts = Post.objects.all().order_by('-create_date')  # 모든 게시물을 가져옴
    
    if kw:
        posts = posts.filter(
            Q(title__icontains=kw) |  # 제목 검색
            Q(content__icontains=kw)  # 내용 검색
        )
    context = {'kw': kw, 'posts': posts}
    return render(request, 'post.html', context)

@login_required(login_url='common:login')
def posting_new(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)  # request.FILES를 추가하여 파일 업로드를 처리합니다.
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('post') # 새로 생성된 게시물 상세 페이지로 이동합니다.
    else:
        form = PostForm()
    return render(request, 'posting_new.html', {'form': form})

@login_required(login_url='common:login')
def posting_change(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    if post.author == request.user:  # 현재 사용자가 게시물의 저자인 경우에만 수정 가능
        if request.method == "POST":
            form = PostForm(request.POST, request.FILES, instance=post)
            if form.is_valid():
                post = form.save(commit=False)
                post.modify_date = timezone.now()
                post.save()
                messages.success(request, '게시물이 성공적으로 수정되었습니다.')
                return redirect('post')  # 수정된 게시물이 있는 post 페이지로 이동
        else:
            form = PostForm(instance=post)
        return render(request, 'posting_change.html', {'form': form})
    else:
        messages.error(request, '해당 게시물을 수정할 수 있는 권한이 없습니다.')
        return redirect('post')
    

@login_required(login_url='common:login')
def posting_delete(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    if post.author == request.user:
        if request.method == 'POST':
            post.delete()
            messages.success(request, '게시물이 성공적으로 삭제되었습니다.')
            return HttpResponseRedirect(reverse('post'))

@login_required(login_url='common:login')
def myinfo(request):
    return render(request, 'myinfo.html') # 내 정보 : 정보 수정

@login_required(login_url='common:login')
def modify_user(request):
    if request.method == 'POST':
        username = request.user.username
        email = request.POST.get('email')
        new_password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        
        try:
            # 사용자 정보 가져오기
            user = User.objects.get(username=username)
            
            # 비밀번호 확인 및 업데이트
            if new_password == confirm_password:
                # 비밀번호 업데이트
                user.set_password(new_password)
                user.email = email  # 이메일 업데이트
                user.save()
                
                # 성공 메시지
                messages.success(request, '성공적으로 변경되었습니다.')
                
                # 리다이렉션
                return redirect('index')
            else:
                messages.error(request, '비밀번호와 비밀번호 확인이 일치하지 않습니다.')
        except User.DoesNotExist:
            messages.error(request, '해당 사용자가 존재하지 않습니다.')

    return render(request, 'modify_user.html', {'messages': messages.get_messages(request)})