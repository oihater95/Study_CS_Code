from django.http.response import HttpResponse

def test(request):
    '''
    view함수가 동작하는 영역
    '''
    return HttpResponse('hoit')  # 템플릿은 여기만 담당?
