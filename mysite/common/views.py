from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib import messages
from common.forms import UserForm

def logout_view(request):
    logout(request)
    return redirect('index')

def signup(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')

            user = authenticate(username=username, password=raw_password)  # 사용자 인증
            login(request, user)  # 로그인

            messages.success(request, '회원가입이 완료되었습니다.')  # 회원가입 성공 메시지 설정

            return redirect('index')
    else:
        form = UserForm()
    return render(request, 'common/signup.html', {'form': form})