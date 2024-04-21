from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls import include
from django.conf.urls.static import static # 이미지를 업로드
from django.urls import re_path
from django.views.generic import TemplateView
from django.contrib.auth.views import LogoutView
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('common/', include('common.urls')), # 404 not found 안뜸! 곤
    path('', views.index, name='index'),
    path('post/', views.post, name='post'),
    path('search/', views.search_results, name='search_results'),
    path('myinfo/', views.myinfo, name='myinfo'),
    path('posting_new/', views.posting_new, name='posting_new'),
    path('modify_user/', views.modify_user, name='modify_user'),
    path('post/<int:post_id>/posting_change/', views.posting_change, name='posting_change'),
    path('post/<int:post_id>/posting_delete/', views.posting_delete, name='posting_delete'),
    # path('common:logout/', views.logout_view, name='logout'),
    # re_path(r'^.*$', TemplateView.as_view(template_name="404.html"), name="404"),
    ]

# 이미지 URL 설정
urlpatterns += static(settings.IMAGE_URL, document_root=settings.IMAGE_ROOT)
