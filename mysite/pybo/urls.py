from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls import include
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),  # admin 네임스페이스 추가
    path('common/', include('common.urls')),  # common 네임스페이스 추가
    path('', views.index, name='index'),
    path('post/', views.post, name='post'),
    path('search/', views.search_results, name='search_results'),
    path('myinfo/', views.myinfo, name='myinfo'),
    path('posting_new/', views.posting_new, name='posting_new'),
    path('modify_user/', views.modify_user, name='modify_user'),
    path('post/<int:post_id>/posting_change/', views.posting_change, name='posting_change'),
    path('post/<int:post_id>/posting_delete/', views.posting_delete, name='posting_delete'),
]

# 이미지 URL 설정
urlpatterns += static(settings.IMAGE_URL, document_root=settings.IMAGE_ROOT)
