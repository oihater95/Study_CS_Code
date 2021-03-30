from django import forms
from .models import Article, Comment

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = '__all__'


class CommentForm(forms.ModelForm):
    # 1. 유효성 검사, 2. HTML
    class Meta:
        model = Comment
        fields = ('content', )