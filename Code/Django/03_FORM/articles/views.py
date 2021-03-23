from django.shortcuts import render, redirect, get_object_or_404
from .models import Article
from .forms import ContactForm, ArticleForm

'''
1. 사용자가 /crud/contact/로 접속 => GET /crud/contact/
2. 사용자가 HTML > form에서 데이터 제출 => POST(contact.html에서 POST 방식으로 보냈기 때문에), POST /crud/contact
3. view 함수에서 contact로 redirect 시킴 => GET /crud/contact, form태그에서 제출한 것 아니면 다 GET
'''

def contact(request):
    # contact에 GET 요청 시 contact.html을 보내줌 
    if request.method == 'GET':
        contact_form = ContactForm()
        context = {
            'contact_form': contact_form
        }
        return render(request, 'articles/contact.html', context)
    # submit => POST => redirect => GET => contact.html (POST 302 -> GET 200)
    # 처음 contact로 온 것은 GET요청(데이터를 보낸 것이 아니기 때문)
    # contact에 POST 요청 시 조회 후 GET으로 contact.html로 보냄
    elif request.method == 'POST':
        contact_form = ContactForm(request.POST)  # request.POST = POST한 데이터
        # 데이터 검증
        print(contact_form.is_valid())  
        print(contact_form.errors)
        return redirect('articles:contact')  # urls.py의 contact로 == /crud/contact => GET


# c
def new(request):
    # 사용자 요청 GET인 경우
    if request.method == 'GET':
        # 비어있는 새로운 form 생성
        form = ArticleForm()
        context = {
            'form': form
        }
        # HTML에 form 실어서 전송
        return render(request, 'articles/new.html', context)
    # 사용자 요청 POST인 경우
    elif request.method == 'POST':
        # form에 요청 data를 입력
        form = ArticleForm(request.POST)
        # form을 통해 data 유효성 검사(validation)
        if form.is_valid():  # 유효할 경우
            # 유효한 경우 저장
            article = form.save()  # 본래 form은 save X but model form은 모델과 연동되기 때문에 저장 가능
            # 저장한 article의 상세보기 페이지로 redirect
            return redirect('articles:detail', article_pk=article.pk)  # article_pk: 변수 라우팅
        else:  # 틀렸을 때
            # 잘못 작성한 데이터 그대로 담고 다시 작성하도록 함(저장은 안된 상태) + 에러메세지 출력
            # 유효하지 않다면 기존의 잘못된 data를 담은 form(L34)을 담고
            context = {
                'form': form
            }
            # HTML에 실어서 전송
            return render(request, 'articles/new.html', context)
        

# r
def index(request):
    articles = Article.objects.all()
    context = {
        'articles': articles
    }
    return render(request, 'articles/index.html', context)


def detail(request, article_pk):
    article = get_object_or_404(Article, pk=article.pk)  # pk: get_object 함수의 인자
    context = {
        'article': article
    }
    return render(request, 'articles/detail.html', context)
    

# u
def edit(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)  # 특정 데이터를 가져옴

    if request.method == 'POST':
        # new와 다르게 특정 article에 대한 내용을 request.POST로 덮어 쓰기
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            article = form.save()
            return redirect('articles:detail', article.pk)
    
    elif request.method == 'GET':
        form = ArticleForm()
    
    context = {'form': form}  # edit.html에서 form action 쓰려면  context = {'form': form, 'article':article}
    return render(request, 'articles/edit.html', context)

    # if request.method == 'GET':
    #     # 기존 게시글 내용을 포함한 HTML을 만들기 위해 instance 추가
    #     # 인스턴스를 주었기 때문에 html에서 value를 쓰지 않아도 내용이 들어있음
    #     form = ArticleForm(instance=article)  # article은 Article의 인스턴스, data는 request데이터만 취급
    #     context = {
    #         'form': form
    #     }
    #     return render(request, 'articles/edit.html', context)
    
    # elif request.method == 'POST':
    #     # new와 다르게 특정 article에 대한 내용을 request.POST로 덮어쓰기
    #     form = ArticleForm(request.POST, instance=article)  # instance 안쓰면 새로 생성됨
    #     if form.is_valid():
    #         article = form.save()  # 본래 form은 save X but model form은 모델과 연동되기 때문에 저장 가능
    #         return redirect('detail', article_pk=article.pk)  # article_pk: 변수 라우팅
        

# d
# def delete(request, article_pk):
#     return redirect()