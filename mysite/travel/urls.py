from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('post/', views.post, name='post'),
    path('sign_up/', views.sign_up, name='sign_up'),
    path('login/', views.login, name='login'),
    path('search/', views.search_results, name='search_results'),
    path('myinfo/', views.myinfo, name='myinfo'),
    path('posting_new/', views.posting_new, name='posting_new'),
    path('modify_user/', views.modify_user, name='modify_user'),
]