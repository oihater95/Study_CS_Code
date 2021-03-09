from django.shortcuts import render
from django.http.response import HttpResponse
import random

def lotto(request):
    lotto = random.sample(range(1, 46), 6)
    # context는 반드시 딕셔너리
    context = {
        'lotto': lotto,
        'greeting': 'hello'
    }
    return render(request, 'workshop0308/lotto.html', context)
