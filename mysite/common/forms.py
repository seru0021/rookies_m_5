from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class UserForm(UserCreationForm):
    email = forms.EmailField(label="이메일", max_length=254)  # 최대 글자수 설정

    class Meta:
        model = User
        fields = ("username", "password1", "password2", "email")

    def clean_email(self):
        email = self.cleaned_data.get('email')
        # 이메일 형식이 올바르지 않은 경우 ValidationError 발생
        if '@' not in email:
            raise ValidationError("올바른 이메일 형식이 아닙니다.")
        return email

    def clean_username(self):
        username = self.cleaned_data.get('username')
        # 유저 이름이 영어, 숫자, '-', '_'로만 이루어져야 함
        if not username.replace('-', '').replace('_', '').isalnum():
            raise ValidationError("아이디는 영어, 숫자, '-', '_'로만 이루어 져야합니다.")
        if len(username) < 5 or len(username) > 20:
            raise ValidationError("아이디는 5자에서 20자 사이어야 합니다.")
        return username
    
    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        self.fields['password1'].widget.attrs['maxlength'] = 20  # 최대 글자수 설정
        self.fields['password2'].widget.attrs['maxlength'] = 20  # 최대 글자수 설정
