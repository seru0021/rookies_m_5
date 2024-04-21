from django.contrib import admin
from django.urls import path, include
from pybo import views

urlpatterns = [
    path('admin/', admin.site.urls),  # 'admin' 네임스페이스 추가
    path('', include('pybo.urls')),
    path('common/', include('common.urls')),
    path('', views.index, name='index'),  # '/' 에 해당되는 path
]
