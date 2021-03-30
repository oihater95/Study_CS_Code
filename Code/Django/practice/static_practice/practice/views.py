from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_GET, require_POST, require_http_methods
from .models import Article
from .forms import ArticleForm

@require_http_methods(['GET', 'POST'])
def new(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            article = form.save()
            return redirect('practice:detail', article.pk)
    else:
        form = ArticleForm()
    context = { 'form': form }
    return render(request, 'practice/forms.html', context)


@require_GET
def index(request):
    articles = Article.objects.all()
    context = { 'articles': articles }
    return render(request, 'practice/index.html', context)


@require_GET
def detail(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    context = { 'article': article }
    return render(request, 'practice/detail.html', context)