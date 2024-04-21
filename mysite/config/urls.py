from django.contrib import admin
from django.urls import path, include
from pybo import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('pybo.urls')),
    path('board/', include('common.urls')),  # common 앱의 URL 패턴을 board/ 아래로 변경
]
