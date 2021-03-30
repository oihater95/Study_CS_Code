from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_safe, require_POST, require_http_methods
from .models import Article, Comment
from .forms import ArticleForm, CommentForm
from django.contrib.auth.decorators import login_required

@require_safe
def index(request):
    articles = Article.objects.order_by('-pk')  # ('-updated_at') => 생성시간 내림차순(최신순)
    context = { 'articles': articles }
    return render(request, 'articles/index.html', context)


@login_required
@require_http_methods(['GET', 'POST'])
def create(request):
    if request.method == "POST":
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save()
            return redirect('articles:detail', article.pk)
    else:
        form = ArticleForm()
    context = { 'form': form }

    return render(request, 'articles/create.html', context)


@require_safe
def detail(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    comment_form = CommentForm()  # 댓글 작성 폼
    comments = article.comment_set.all()  # 역참조 (해당 게시글에 대한 댓글들 쿼리셋)  == Comments.objects.filter()
    context = { 
        'article': article,
        'comment_form': comment_form,
        'comments': comments,
    }
    return render(request, 'articles/detail.html', context)

@login_required
@require_http_methods(['GET', 'POST'])
def update(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    if request.method == "POST":
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            article = form.save()
            return redirect('articles:detail', article.pk)
    else:
        form = ArticleForm(instance=article)
    context = {
        'form': form,
    }
    return render(request, 'articles/update.html', context)


@require_POST
def delete(request, pk):
    if request.user.is_authenticated:
        article = get_object_or_404(Article, pk=pk)
        article.delete()
    return redirect('articles:index')


@require_POST
def comment_create(request, article_pk):
    if request.user.is_authenticated:  # 로그인했을 경우에만 if 동작
        article = get_object_or_404(Article, pk=article_pk)
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():  # article_id 없는데 통과하는 이유: forms.py에서 'content'만 썼기 때문에 'content'만 검사
            # comment_form.save() 바로 못함, article_id 없음, form의 역할은 is_vaild넘어오면 끝
            comment = comment_form.save(commit=False)  # 인스턴스 넘겨주고(comment가 반환됨) DB에는 나중에 저장
            comment.article = article  # comment 테이블에 article_id 작성, form이 해줄 수 없음(form에 없음)
            comment.save()  # DB에 저장
            return redirect('articles:detail', article_pk)
        context = {
            'comment_form': comment_form,
            'article': article,
        }
        return render(request, 'articles/detail.html', context)


@require_POST
def comment_delete(request, article_pk, comment_pk):
    if request.user.is_authenticated:  # 로그인한 사용자라면
        comment = get_object_or_404(Comment, pk=comment_pk)
        comment.delete()
    return redirect('articles:detail', article_pk)


# def update_comment(request, article_pk)