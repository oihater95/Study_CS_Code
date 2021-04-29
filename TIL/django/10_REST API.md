# 10_REST API

> 필요한 module
>
> djangorestframework



## Model Serializer

> 모델 필드에 해당하는 필드가 있는 Serializer 클래스를 자동으로 만들 수 있는 shortcut을 제공

1. 모델 정보에 맞춰 자동으로 필드 생성
2. serializer에 대한 유효성 검사를 자동으로 생성
3. .create 및 .update()의 간단한 기본 구현 포함



### Model (1:N)

```python
class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Comment(models.Model):
    # related_name => article이 comment 부를 때 comments로 부름
    # related_name 안쓰면 serializers에서 comment_set으로 사용해야함 
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')
    content = models.CharField(max_length=200)
```



### Serializer (1:N)

```python
'''
JSON
1. K - V (key - value)
2. Json == string(dict/list로 해석(parsing) 가능)
'''

# Comment 관련 JSON + validation 담당자
class CommentSerializer(serializers.ModelSerializer):
    content = serializers.CharField(min_length=1, max_length=200)
    
    class Meta:
        model = Comment
        #
        fields = '__all__'  # JSON에는 모든 필드가 포함
        read_only_fields = ('article', )  # CUD(Write)관련 validation은 article 포함하지 않는다
        # article을 제외하는 이유: views에서 is_valid유효성 검사 후 article을 채워넣는데
        # 제외하지 않고 쓰면 is_vaild에서 article없어서 통과 못함

        '''
        exclude = ('article', )  
        # article을 제외하는 이유: views에서 is_valid유효성 검사 후 article을 채워넣는데
        # 제외하지 않고 쓰면 is_vaild에서 article없어서 통과 못함
        # but exclude를 사용하면 Write(CUD), READ(R) 에서도 article 없어져버림
        '''

# 1. 데이터 검증 
# 2. JSON 생성
# 단일 담당(detail)
class ArticleSerializer(serializers.ModelSerializer):
    title = serializers.CharField(min_length=2, max_length=100)
    content = serializers.CharField(min_length=2)
    # Comment 관련한 JSON도 포함해야함 -> CommentSerializer가 들어가야함
    # 위에서 읽기 때문에 class CommentSerializer가 위에 있어야함
    # Comment Model에서 related_name과 완전히 동일하게 작성(related_name을 따름)
    comments = CommentSerializer(many=True, read_only=True)  # read_only=True => 수정불가 / many=True 1:N
    class Meta:
        model = Article
        fields = '__all__'


# 여러개 담당(index)
class ArticleListSerializer(serializers.ModelSerializer):
    # title = serializers.CharField(min_length=2, max_length=100)  # 안써도 무방, 읽기만 하기 때문
    # 댓글 개수를 확인하려고 한다 => 댓글 JSON 담당자 소환
    comments = CommentSerializer(many=True)
    # 없는 필드(댓글 개수)를 만들어서 JSON 구성
    comment_count = serializers.IntegerField(source='comments.count')  # comments.count QuerySet명령어
    class Meta:
        model = Article
        fields = ('pk', 'title', 'comments', 'comment_count',)
        read_only_fields = fields  # 읽기 전용으로 만듦
```



## Build RESTful API 

### urls.py

```python
urlpatterns = [
    # RESTful
    # GET/POST => /api/articles/
    path('articles/', views.article_list_or_create),

    # GET/PATCH/PUT/DELETE => /api/articles/1/
    path('articles/<int:article_pk>/', views.article_detail_or_update_or_delete),

    # GET/POST => /api/articles/<pk>/comments/ => <pk>에 대한 댓글 생성 (전체 댓글 조회는 article detail에서 함)
    path('articles/<int:article_pk>/comments/', views.create_comments),

    # PUT/DELETE => /api/articles/<pk>/comments/1/ => 단일 댓글 수정/삭제
    path('articles/<int:article_pk>/comments/<int:comment_pk>/', views.update_or_delete_comment),

```



### GET List & POST Create Article

- `api_view` 데코레이터 설정 필수
- id, title 필드만 시리얼라이징 된 결과를 확인

```python
# RESTful READ, CREATE
@api_view(['GET', 'POST'])
def article_list_or_create(request):
    if request.method == 'GET':
        articles = Article.objects.all()
        serializer = ArticleListSerializer(articles, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        # request.POST => POST 요청 and HTML FormData로 넘어온 데이터만 취급, Querydict
        # request.GET => URL parmas (/?key1=value)
        # request.data => 사용자가 제출한 JSON 데이터는 여기에!, POST 포함, dict
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid():
            article = serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

```



**Serializing multiple objects**

- 단일 객체 인스턴스 대신 쿼리셋 또는 객체 목록을 시리얼라이징하려면 serializer를 인스턴스화 할 때 `many=True` 를 전달해야 함



### GET Detail & PUT(PATCH) Update & DELETE Delete Article

```python
# RESTful READ, UPDATE, DELETE, Comment READ
@api_view(['GET', 'PATCH', 'PUT', 'DELETE'])
def article_detail_or_update_or_delete(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)

    if request.method == 'GET':
        serializer = ArticleSerializer(article)
        return Response(serializer.data)
    # PUT은 모두 업데이트, PATCH는 일부 업데이트
    # PATCH에서 안 건드린 부분은 원래 가지고 있던 데이터를 가져옴
    elif request.method == 'PATCH' or request.method == 'PUT':  
        serializer = ArticleSerializer(data=request.data, instance=article)
        # serializer = ArticleSerializer(article, request.data) 로 써도됨
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        # raise_exception=True가 대신 역할함
        # else:
        #     return Response(serializer.errors, status=400)

    elif request.method == 'DELETE':
        data = {  # customize message, 필수 아님
            'success': True,
            'message': f'{article.pk} 번 게시글이 삭제되었습니다.',
        }
        article.delete()  # DB에 삭제 요청, 해당 함수가 끝날 때까지는 article object살아있음 but id는 삭제됨
        return Response(data=data, status=status.HTTP_204_NO_CONTENT)
```



### GET List Comment

- ArticleSerializer에 CommentSerializer 포함
- GET Detail Article에서 해당 article_pk에 대한 Comment List를 보여줌



### POST Create Comment

```python
# RESTful Comment CREATE
@api_view(['POST'])
def create_comments(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    serializer = CommentSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(article=article)  # CommentSerializer의 article(FK)속성에 article을 넣음 
        return Response(serializer.data, status=status.HTTP_201_CREATED)
```



### PUT Update & DELETE Delete Comment

```python
# RESTful Comment UPDATE, DELETE
@api_view(['PUT', 'DELETE'])
def update_or_delete_comment(request, article_pk, comment_pk):
    article = get_object_or_404(Article, pk=article_pk)
    comment = get_object_or_404(Comment, pk=comment_pk)
    if request.method == 'PUT':
        serializer = CommentSerializer(data=request.data, instance=comment)
        if serializer.is_valid(raise_exception=True):
            serializer.save(article=article)
            return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'DELETE':
        data = {  # customize message, 필수 아님
            'success': True,
            'message': f'{comment.pk} 번 댓글이 삭제되었습니다.',
        }
        comment.delete()
        return Response(data=data, status=status.HTTP_204_NO_CONTENT)
```

