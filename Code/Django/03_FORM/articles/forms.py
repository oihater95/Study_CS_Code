from django import forms
from .models import Article  # Article 모델과 연동하기 위해 필요
'''
Form을 쓰는 이유
1. 데이터 검증(Data Validation)
2. html을 쉽게 쓰기 위해서 (HTML easy)
'''

# forms.Form => 특정 모델과 연동 X 단순히 데이터 검증/HTML 생성용
class ContactForm(forms.Form):
    # forms는 min_length 같은 옵션들 자동완성됨 => models.py와 다르다(비슷하지만 다름!)
    name = forms.CharField(min_length=2, max_length=10)
    email = forms.EmailField()
    age = forms.IntegerField(min_value=3, max_value=100)
    content = forms.CharField(widget=forms.Textarea)  # form.Form은 TextField 없음
    # widget은 겉모습만 바꿈 => HTML 생성 시 주는 옵션, 위젯은 반드시 form field에 할당 단독 사용 불가
    # widget은 유효성 검사 X
 
# forms.ModelForm => 특정 모델과 연동 O
class ArticleForm(forms.ModelForm):
    # 자동 연동
    class Meta:  # 모델 클래스에 대한 정보
        model = Article  # 모델 등록, Article()로 하면 안됨
        fields = '__all__'  # 필드 전체 but auto_now(_add)가 붙은 필드는 알아서 채우기 때문에 보여주지 않음

    '''
    Form
    어떤 모델에 저장해야하는지 알 수 없으므로 유효성 검사 이후 cleaned_data 딕셔너리 생성
    cleaned_data 딕셔너리에서 데이터 가져온 후 save()호출
    모델에 연관되지 않은 데이터 받을 때 사용

    ModelForm
    모델에서 양식에 필요한 대부분의 정보를 이미 정의
    어떤 레코드를 만들어야 할 지 알고 있으므로 바로 save()호출
    모델에 연관된 데이터 받을 때 사용
    '''