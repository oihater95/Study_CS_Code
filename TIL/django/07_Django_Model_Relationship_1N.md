[TOC]

# 07. Django_Model_Relationship 1:N

> https://docs.djangoproject.com/ko/3.1/ref/models/fields/#module-django.db.models.fields.related

<br>

## Foreign Key

**개념**

- 외래 키(외부 키)
- RDBMS에서 한 테이블의 필드 중 다른 테이블의 행을 식별할 수 있는 키
- 참조하는 테이블에서 1개의 키(속성 또는 속성의 집합)에 해당하고 이는 참조되는 측의 테이블의 기본 키를 가리킴
- 참조하는 테이블의 속성의 행 1개의 값은, 참조되는 측 테이블의 행 값에 대응
  - 이 때문에 참조하는 테이블의 행에는, 참조되는 테이블에 나타나지 않는 값을 포함할 수 없음
- 참조하는 테이블의 행 여러 개가, 참조되는 테이블의 동일한 행을 참조할 수 있음

**특징**

- 키를 사용하여 부모 테이블의 유일한 값을 참조 (참조 무결성)
- 외래 키의 값이 부모 테이블의 기본 키 일 필요는 없지만 유일해야 함

<br>

## ForeignKey field

> A many-to-one relationship

- 2개의 필수 위치 인자가 필요
  - 참조하는 model class
  - on_delete 옵션

<br>

### 1:N model manager

```python
# articles/models.py

class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    content = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.content
```

- Article : Comment = 1 : N → 하나의 게시글에는 여러 개의 댓글이 달릴 수 있다.

<br>

`on_delete`

- ForeignKey의 필수 인자이며, ForeignKey가 참조하고 있는 부모(Article) 객체가 사라졌을 때 달려 있는 댓글들을 어떻게 처리할 지 정의
- Database Integrity(데이터 무결성)을 위해서 매우 중요한 설정이다.

<br>

**possible values for `on_delete`**

- `CASCADE` : **부모 객체(참조 된 객체)가 삭제 됐을 때 이를 참조하는 객체도 삭제**
- `PROTECT` 
- `SET_NULL`
- `SET_DEFAULT`
- `SET()`
- `DO_NOTHING` 
- `RESTRICT`

<br>

**migration**

```bash
$ python manage.py makemigrations
# $ python manage.py sqlmigrate articles 0002
$ python manage.py migrate
```

<br>

**데이터베이스 표현**

- Django는 필드 이름에 `_id`를 추가하여 데이터베이스 필드 이름을 만듦

<br>

**Table 직접 확인하기**

- `article_id` 라는 컬럼이 생성
- 만약 ForeignKey 를 article 이라고 하지 않고 `abcd = models.ForeignKey(..)` 형태로 생성 했다면 `abcd_id` 로 만들어진다. 
- 이렇게되면 모델 관계를 파악하는 것이 어렵기 때문에 부모 클래스명의 소문자(단수형)로 작성하는 것이 바람직하다.

<br>

**1 : N 관계 manager**

- **Article(1)** : **Comment(N)** : `comment_set`
  - `article.comment` 형태로는 가져올 수 없다. 
  - 게시글에 몇 개의 댓글이 있는지 Django ORM이 보장할 수 없기 때문
  - 본질적으로는 Article 클래스에 Comment 와의 어떠한 관계도 연결하지 않음
- **Comment(N)** : **Article(1)** : `article`
  - 댓글의 경우 어떠한 댓글이든 반드시 자신이 참조하고 있는 게시글이 있으므로 `comment.article`와 같이 접근할 수 있음

<br>

**`related_name`**

> https://docs.djangoproject.com/en/3.1/ref/models/fields/#django.db.models.ForeignKey.related_name

- 위에서 확인한 것처럼 부모 테이블에서 역으로 참조할 때(the relation from the related object back to this one.) `모델이름_set` 이라는 형식으로 참조한다. (**역참조**)

- related_name 값은 django 가 기본적으로 만들어 주는 `_set` manager를 임의로 변경할 수 있다.

  ```python
  # articles/models.py
  
  class Comment(models.Model):
      article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')
    ...
  ```

- 위와 같이 변경하면 `article.comment_set` 은 더이상 사용할 수 없고 `article.comments` 로 대체된다.

- 1:N 관계에서는 거의 사용하지 않지만 M:N 관계에서는 반드시 사용해야 할 경우가 발생한다.

<br>

------

<br>

## Comment

### CREATE

```python
# forms.py

from .models import Article, Comment


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = '__all__'
```

```python
# articles/views.py

from .forms import ArticleForm, CommentForm


def detail(request, pk):
    article = get_object_or_404(Article, pk=pk)
    comment_form = CommentForm()
    context = {
        'article': article,
        'comment_form': comment_form,
    }
    return render(request, 'articles/detail.html', context)
```

- **detail page 에 댓글 작성 form 추가**

  ```html
  <!-- articles/detail.html -->
  
  {% extends 'base.html' %}
  
  {% block content %}
    ...
    <a href="{% url 'articles:index' %}">back</a>
    <hr>
    <form action="" method="POST">
      {% csrf_token %}
      {{ comment_form }}
      <input type="submit">
    </form>
  {% endblock %}
  ```

- 필드 출력 재설정

  ```python
  # articles/forms.py
  
  class CommentForm(forms.ModelForm):
  
      class Meta:
          model = Comment
          exclude = ('article',)
  ```

```python
# articles/urls.py

path('<int:pk>/comments/', views.comments_create, name='comments_create'),
save()
```

<br>

**`save()` method**

>  https://docs.djangoproject.com/en/3.0/topics/forms/modelforms/#the-save-method

- Create, but don't save the new instance.

  ```python
  # articles/views.py
  
  @require_POST
  def comments_create(request, pk):
      article = get_object_or_404(Article, pk=pk)
      comment_form = CommentForm(request.POST)
      if comment_form.is_valid():
          comment = comment_form.save(commit=False)
          comment.article = article
          comment.save()
          return redirect('articles:detail', article.pk)
      context = {
          'comment_form': comment_form,
          'article': article,
      }
      return render(request, 'articles/detail.html', context)
  ```

  ```html
  <!-- articles/detail.html -->
  
  <form action="{% url 'articles:comments_create' article.pk %}" method="POST">
    {% csrf_token %}
    {{ comment_form }}
    <input type="submit">
</form>
  ```
  
  - 댓글을 작성한 후 admin 페이지 혹은 sqlite 확장에서 확인

<br>

### READ

- 특정 article에 있는 모든 댓글을 가져온 후 template 으로 전달한다.

  ```python
  # articles/views.py
  
  from .models import Article, Comment
  
  
  def detail(request, pk):
      article = Article.objects.get(pk=pk)
      comment_form = CommentForm()
      comments = article.comment_set.all()
      context = {
          'article': article,
          'comment_form': comment_form,
          'comments': comments,
      }
      return render(request, 'articles/detail.html', context)
  ```
```
  
  ```html
  <!-- articles/detail.html -->
  
  {% extends 'base.html' %}
  
  {% block content %}
    ...
    <a href="{% url 'articles:index' %}">back</a>
    <hr>
    <h4>댓글 목록</h4>
    {% for comment in comments %}
      <li>{{ comment.content }}</li>
    {% endfor %}
    <hr>
    ...
  {% endblock %}
```

<br>

### DELETE

```python
# articles/urls.py

path('<int:article_pk>/comments/<int:comment_pk>/delete/', views.comments_delete, name='comments_delete'),
```

```python
# articles/views.py

@require_POST
def comments_delete(request, article_pk, comment_pk):
    comment = get_object_or_404(Comment , pk=comment_pk)
    comment.delete()
    return redirect('articles:detail', article_pk)
```

```django
<!-- articles/detail.html -->

{% block content %}
  ...
  <h4>댓글 목록</h4>
  {% for comment in comments %}
    <li>
      {{ comment.content }}
      <form action="{% url 'articles:comments_delete' article.pk comment.pk %}" method="POST" class="d-inline">
        {% csrf_token %}
        <input type="submit" value="DELETE">
      </form>
    </li>
  {% endfor %}
  <hr>
	...
{% endblock %}
```

<br>

------

<br>

## Comment 관련 추가 사항

### 댓글 개수 출력

```python
# 1. {{ comments|length }}

# 2. {{ article.comment_set.all|length }}

# 3. {{ comments.count }} 
```

```django
<!-- articles/detail.html -->

<h4>댓글 목록</h4>
{% if comments|length %}
  <p><b>{{ comments|length }}개의 댓글이 있습니다.</b></p>
{% endif %}
```

<br>

### 댓글이 없는 경우 다른 문장 출력

- `for empty` 활용

  ```html
  <!-- articles/detail.html -->
  
  {% for comment in comments %}
    <li>
      {{ comment.content }}
      <form action="{% url 'articles:comments_delete' article.pk comment.pk %}" method="POST" class="d-inline">
        {% csrf_token %}
        <input type="submit" value="DELETE">
      </form>
    </li>
  {% empty %}
    <p><b>댓글이 없어요</b></p>
  {% endfor %}
  ```

<br>

------