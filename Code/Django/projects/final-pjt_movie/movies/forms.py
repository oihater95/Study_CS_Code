from django import forms
from .models import Movie, Rate

class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ('title', 'overview', 'poster_path',)


class RateForm(forms.ModelForm):
    rating = forms.IntegerField(max_value=5, min_value=0,)
    class Meta:
        model = Rate
        fields = ("rating",)