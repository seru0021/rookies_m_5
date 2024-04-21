from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import User


class UserProfile(models.Model):
    password = models.CharField(max_length=128, null=True)
    
class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    rating = models.CharField(max_length=10)
    hashtags = models.CharField(max_length=200)
    region = models.CharField(max_length=50)
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    destination = models.CharField(max_length=100)

    create_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)  # ForeignKey to User model

    def __str__(self):
        return self.title

# 사용자 매니저 클래스 정의
class CustomUser(AbstractBaseUser):
    user_id = models.CharField(max_length=20, unique=True)
    nickname = models.CharField(max_length=20)
    email = models.EmailField(max_length=30, unique=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    objects = CustomUserManager()

    user_id = 'user_id'
    REQUIRED_FIELDS = ['nickname']

    def __str__(self):
        return self.user_id

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True

    def create_superuser(self, user_id, nickname):
        user = self.create_user(
            user_id=user_id,
            nickname=nickname,
        )
        user.is_admin = True
        user.is_staff = True
        user.save(using=self._db)
        return user

# 사용자 모델 클래스 정의
class CustomUser(AbstractBaseUser):
    user_id = models.CharField(max_length=20, unique=True)
    nickname = models.CharField(max_length=20)
    email = models.EmailField(max_length=30, unique=True)
    password = models.CharField(max_length=20)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    objects = CustomUserManager()

    user_id = 'user_id'
    REQUIRED_FIELDS = ['nickname']

    def __str__(self):
        return self.user_id

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True
