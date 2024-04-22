from django.contrib import admin
from .models import Post

admin.site.register(Post)
admin.site.site_header = "Team 5의 관리자 페이지"
admin.site.site_title = "Team 5의 관리자 페이지"
admin.site.index_title = "Team 5의 대시보드"