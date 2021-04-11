from django import forms
from .models import Article, Comment

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ('content', )

class CommentForm(forms.ModelForm):
    # Form => HTML 만들기, 데이터 검증하기
    # fields 에 없는 속성은 HTML X & validation X

    # wow라는 이름의 input 태그 원래 안나옴, 넘어온 데이터 검증 O, but 이름 맞는 컬럼 없음=>DB에 안들어감
    wow = forms.CharField(min_length=2, max_length=100)  
    
    # content 라는 이름의 input type=email, 넘어온 데이터도 email 규격에 대해 검증 O, 이름 맞는 컬럼있으므로 DB에 들어감
    content = forms.EmailField() # 이거 안쓰면 model의 content와 같이 CharField로 생각하고 CharField인지 검증, DB에 저장
    # password만 따로 써줌 (암호화 관련)
    class Meta:
        model = Comment
        fields = ('content', )