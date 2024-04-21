from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import User

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
class CustomUserManager(BaseUserManager):
    def create_user(self, user_id, nickname, password=None):
        if not user_id:
            raise ValueError('The user_id must be set')
        
        user = self.model(
            user_id=user_id,
            nickname=nickname,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, user_id, nickname, password=None):
        user = self.create_user(
            user_id=user_id,
            nickname=nickname,
            password=password,
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
