from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.contrib import messages
from common.forms import UserForm
from django.contrib.auth import logout
from django.conf import settings
from django.utils import timezone

class CustomLoginView(LoginView):
    template_name = 'common/login.html'  # 로그인 페이지 템플릿 설정

    def dispatch(self, request, *args, **kwargs):
        # 세션 만료 시간 설정
        request.session.set_expiry(settings.SESSION_COOKIE_AGE)
        return super().dispatch(request, *args, **kwargs)

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

# 로그인 후 일정 시간 동안 활동하지 않으면 세션을 종료하는 기능
class CustomLoginRequiredMixin(LoginRequiredMixin):
    idle_timeout = settings.SESSION_IDLE_TIMEOUT

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            last_activity = request.session.get('last_activity')
            if last_activity:
                elapsed_time = timezone.now() - last_activity
                if elapsed_time.total_seconds() > self.idle_timeout:
                    logout(request)
                    messages.warning(request, '세션이 만료되었습니다. 다시 로그인해주세요.')
                    return redirect('common:login')
        request.session['last_activity'] = timezone.now()
        return super().dispatch(request, *args, **kwargs)
