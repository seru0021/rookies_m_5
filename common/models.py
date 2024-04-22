from django.contrib.auth.models import User
from django.db import models

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    
    # 사용자의 비밀번호
    password = models.CharField(max_length=20)
    
    # 사용자의 이메일
    email = models.EmailField(max_length=20, blank=True)


    def __str__(self):
        return self.user.username
    
