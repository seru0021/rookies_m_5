from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('post/', views.post, name='post'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),  # 수정된 로그인 뷰 함수명으로 변경
    path('search/', views.search_results, name='search_results'),
    path('myinfo/', views.myinfo, name='myinfo'),
    path('posting_new/', views.posting_new, name='posting_new'),
    path('modify_user/', views.modify_user, name='modify_user'),
]