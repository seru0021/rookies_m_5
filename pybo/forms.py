from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Post
from django import forms


#######################################################
#문자열 길이 제한
class MyForm(forms.Form):
    my_field = forms.CharField(max_length=100)
#######################################################

class UserForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)

class PostForm(forms.ModelForm):
    REGION_CHOICES = [
        ('서울', '서울'),
        ('경기도', '경기도'),
        ('제주도', '제주도'),
    ]

    RATING_CHOICES = [
        ('★★★★★', '★★★★★'),
        ('★★★★☆', '★★★★☆'),
        ('★★★☆☆', '★★★☆☆'),
        ('★★☆☆☆', '★★☆☆☆'),
        ('★☆☆☆☆', '★☆☆☆☆'),
    ]

    HASHTAG_CHOICES = [
        ('#여행','#여행'),
        ('#아이와', '#아이와'),
        ('#연인과', '#연인과'),
        ('#부모님과', '#부모님과'),
        ('#친구와', '#친구와'),
        ('#혼자', '#혼자'),
        ('#테마파크', '#테마파크'),
        ('#박물관', '#박물관'),
        ('#시장', '#시장'),
        ('#유적지', '#유적지'),
        ('#랜드마크', '#랜드마크'),
        ('#즐길거리', '#즐길거리'),
        ('#먹거리', '#먹거리')
    ]

    title = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'id': 'title', 'required': True}))
    content = forms.CharField(max_length=1000, widget=forms.Textarea(attrs={'id': 'content', 'required': True}))
    region = forms.ChoiceField(choices=REGION_CHOICES, widget=forms.Select(attrs={'id': 'region'}))
    rating = forms.ChoiceField(choices=RATING_CHOICES, widget=forms.Select(attrs={'id': 'rating'}))
    hashtags = forms.ChoiceField(choices=HASHTAG_CHOICES, widget=forms.Select(attrs={'id': 'hashtags'}))

    class Meta:
        model = Post
        fields = ['region', 'destination', 'rating', 'hashtags', 'image', 'title', 'content']
        widgets = {
            'destination': forms.TextInput(attrs={'id': 'destination', 'required': True}),
            'image': forms.FileInput(attrs={'id': 'image'}),
            'title': forms.TextInput(attrs={'id': 'title', 'required': True}),
            'content': forms.Textarea(attrs={'id': 'content', 'required': True}),
        }
