from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# 질문 모델 클래스를 정의
class Question(models.Model):
    # 질문 모델이 가지는 속성을 정의 
    subject = models.CharField(max_length=200)      # 글자 수 제한이 있는 데이터
    content = models.TextField()                    # 글자 수 제한이 없는 데이터
    create_date = models.DateTimeField()            # 날짜, 시간을 나타내는 데이터

    def __str__(self):
        return self.subject

# 답변 모델 클래스를 정의
class Answer(models.Model):
    # 답변 모델이 가지는 속성을 정의
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()


class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    rating = models.IntegerField(null=True, blank=True)
    hashtag = models.CharField(max_length=100, null=True, blank=True)

# 사용자 매니저 클래스 정의
class CustomUserManager(BaseUserManager):
    def create_user(self, username, nickname, password=None):
        if not username:
            raise ValueError('The Username must be set')
        
        user = self.model(
            username=username,
            nickname=nickname,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, nickname, password=None):
        user = self.create_user(
            username=username,
            nickname=nickname,
            password=password,
        )
        user.is_admin = True
        user.is_staff = True
        user.save(using=self._db)
        return user

# 사용자 모델 클래스 정의
class CustomUser(AbstractBaseUser):
    username = models.CharField(max_length=50, unique=True)
    nickname = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['nickname']

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True