from django.urls import path
from . import views         # 현재 패키지에서 views 모듈을 가져옴

urlpatterns = [
    path('', views.index, name='index'),
    path('post/', views.post, name='post'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('search/', views.search_results, name='search_results'),
    path('myinfo/', views.myinfo, name='myinfo'),
    path('posting_new/', views.posting_new, name='posting_new'),
    path('modify_user/', views.modify_user, name='modify_user'),
]