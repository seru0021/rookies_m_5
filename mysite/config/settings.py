import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent



# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'z@few2eb!y#ln0j$cjvt8_sdjughtp(w9$75p3jvg$oet2a4f3'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition


INSTALLED_APPS = [
    'common.apps.CommonConfig',  # 로그인 전용 파일
    'django.contrib.admin',
    'django.contrib.auth', # 로그인 사용자 인증 기능 사용하려면 필요함.
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'pybo.apps.PyboConfig',
    #'debug_toolbar',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware'
]

INTERNAL_IPS = ('127.0.0.1')

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        #'DIRS': [
        #    BASE_DIR / 'pybo' / 'templates',  # 프로젝트 루트 디렉토리의 pybo/templates 디렉토리
        #],
        'DIRS': [os.path.join(BASE_DIR, 'templates')], # 루트 변경
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]


WSGI_APPLICATION = 'config.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'sampledb',  # 데이터베이스 이름
        'USER': 'admin',  # MySQL 사용자 이름, RDS할때는 admin
        'PASSWORD': 'abc123123',  # MySQL 비밀번호 #그니깐, RDS할때는 abc123123
        'HOST': 'rookies-team5-db.c3w0mgioep1e.us-west-2.rds.amazonaws.com',  # MySQL 호스트 (예: localhost) RDS할때 rookies-team5-db.c3w0mgioep1e.us-west-2.rds.amazonaws.com
        'PORT': '3306' # '3306',  # MySQL 포트 (기본값: 3306)
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
]

# 로그인 후 리다이렉션 URL 설정
# LOGIN_REDIRECT_URL = 'index/'
LOGIN_REDIRECT_URL = '/' # 새 로그인 리다이렉션 url

# 로그아웃 후 리다이렉션 URL 설정
LOGOUT_REDIRECT_URL = '/'

# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

# 한국기준으로 수정
LANGUAGE_CODE = 'ko-kr'

TIME_ZONE = 'Asia/Seoul'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

STATIC_URL = '/static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]

STATIC_ROOT = BASE_DIR / 'staticfiles'

IMAGE_ROOT = os.path.join(BASE_DIR, 'images')
IMAGE_URL = '/images/'
