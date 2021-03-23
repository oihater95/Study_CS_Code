from django.shortcuts import render, redirect, get_object_or_404
from .models import Article
from .forms import ArticleForm
from django.views.decorators.http import require_GET, require_POST, require_http_methods  # require_GET 대신 safe를 쓰는 추세

@require_http_methods(['GET', 'POST'])
def new(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES)  # 업로드한 파일은 request.FILES로 따로 들어감
        if form.is_valid():
            article = form.save()
            return redirect('uploader:detail', article.pk)
    else:
        form = ArticleForm()
    
    context = { 'form': form }
    return render(request, 'uploader/forms.html', context)

@require_GET
def index(request):
    return render(request, 'uploader/index.html')


@require_GET
def detail(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    context = {'article': article}
    return render(request, 'uploader/detail.html', context)