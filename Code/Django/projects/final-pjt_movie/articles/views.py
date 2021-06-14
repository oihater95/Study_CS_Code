from django.core import paginator
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods, require_POST, require_safe
from .models import Article, Comment
from .forms import ArticleForm, CommentForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

@require_safe
def index(request):
    articles = Article.objects.order_by('-pk')
    paginator = Paginator(articles, 10)  # 페이지 당 10개씩
    page = request.GET.get('page','1')

    try:
        pages = paginator.page(page)
    except PageNotAnInteger:  # 페이지번호 없으면 1페이지로
        pages = paginator.page(1)
    except EmptyPage:  # 페이지 범위 벗어나면 마지막 페이지로
        pages = paginator.page(paginator.num_pages)

    idx = pages.number  # 해당 페이지 인덱스
    max_idx = len(paginator.page_range)  # 마지막 페이지
    page_size = 5  # 하단에 보여줄 페이지 범위 크기

    if idx > page_size: 
        start_idx = idx - page_size
    else: 
        start_idx = 1

    if idx + page_size == max_idx:
        end_idx = max_idx
    else:
        if idx <= max_idx:
            end_idx = idx + page_size
        else:
            end_idx = max_idx

    page_range = list(paginator.page_range[start_idx-1:end_idx])

    context = {
        'articles': articles,
        'pages': pages,
        'page_range': page_range,
        'max_idx': max_idx,
        'page_size': page_size
    }
    return render(request, 'articles/index.html', context)

@login_required
@require_http_methods(['GET', 'POST'])
def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            article.user = request.user
            article.save()
            return redirect('articles:index')

    else:
        form = ArticleForm()
    context = {
        'form': form
    }
    return render(request, 'articles/create.html', context)


@login_required
@require_safe
def detail(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    comments = article.comment_set.all()
    comment_form = CommentForm()
    context = {
        'article': article,
        'comment_form': comment_form,
        'comments': comments
    }
    return render(request, 'articles/detail.html', context)


@login_required
@require_http_methods(['GET', 'POST'])
def update(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    if request.user == article.user:
        if request.method == 'POST':
            form = ArticleForm(request.POST, instance=article)
            if form.is_valid():
                form.save()
                return redirect('articles:detail', article.pk)
        else:
            form = ArticleForm(instance=article)
        context = {
            'form': form,
            'article': article,
        }
        return render(request, 'articles/update.html', context)
    else:
        return redirect('articles:index')
    

@require_POST
def delete(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    if request.user.is_authenticated:
        if article.user == request.user:
            article.delete()
            return redirect('articles:index')
    return redirect('articles:detail', article.pk)


@require_POST
def create_comment(request, article_pk):
    if request.user.is_authenticated:
        article = get_object_or_404(Article, pk=article_pk)
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.article = article
            comment.user = request.user
            comment.save()
            return redirect('articles:detail', article_pk)
        context = {
            'comment_form': comment_form,
            'article': article
        }
        return render(request, 'articles/detail.html', context)
    return redirect('accounts:login')

# 추후 수정(오류) => comment update html 추가
@require_http_methods(['GET', 'POST'])
def update_comment(request, article_pk, comment_pk):
    article = get_object_or_404(Article, pk=article_pk)
    comment = get_object_or_404(Comment, pk=comment_pk)
    comments = article.comment_set.all()
    if request.user == comment.user:
        if request.method == 'POST':
            comment_form = CommentForm(request.POST, instance=comment)
            if comment_form.is_valid():
                comment_form.save()

                return redirect('articles:detail', article.pk)
        else:
            comment_form = CommentForm(instance=comment)
        context = {
            
            'comments': comments,
            'article': article,
        }
        return render(request, 'articles/detail.html', context)

    else:
        return redirect('articles:index')
    


@require_POST
def delete_comment(request, article_pk, comment_pk):
    if request.user.is_authenticated:
        comment = get_object_or_404(Comment, pk=comment_pk)
        if request.user == comment.user:
            comment.delete()
    return redirect('articles:detail', article_pk)

