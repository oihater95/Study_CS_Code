from django import forms
from .models import Reservation

BIRTH_YEAR_CHOICES = ['1980', '1981', '1982']
FAVORITE_COLORS_CHOICES = [
    ('blue', 'Blue'),
    ('green', 'Green'),
    ('black', 'Black'),
]


class ReservationForm(forms.ModelForm):
    name = forms.CharField(min_length=2)  # 여기서 글자 수 제한이 적용됨
    number = forms.IntegerField(min_value=1, max_value=9)  # 숫자 범위 제한
    my_comment = forms.CharField(widget=forms.Textarea)  # 모델에 없음 => 화면에는 출력되지만 해당 부분은 DB에 저장되지 않음
    birth_year = forms.DateField(widget=forms.SelectDateWidget(years=BIRTH_YEAR_CHOICES))
    favorite_colors = forms.MultipleChoiceField(
        required=False,
        widget=forms.CheckboxSelectMultiple,
        choices=FAVORITE_COLORS_CHOICES,
    )

    class Meta:
        model = Reservation
        fields = '__all__'