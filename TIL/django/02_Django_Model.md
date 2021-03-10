# 02. Django_Model

## Model

- 단일한 데이터에 대한 정보를 가짐
- 사용자가 저장하는 데이터들의 필수적인 필드들과 동작들을 포함
- 저장된 데이터베이스 구조(layout)
- 각각의 model은 하나의 데이터베이스 테이블에 매핑
- 웹 어플리케이션의 데이터를 구조화하고 조작하기 위한 도구



### DataBase(DB)

- 체계화된 데이터의 모임



### Query

- 데이터를 조회하기 위한 명령어
- 조건에 맞는 데이터를 추출하거나 조작하는 명령어



### 스키마(Schema)

- DB에서 자료의 구조, 표현방법, 관계 등을 정의한 구조
- DB의 구조와 제약조건에 관련한 전반벅인 명세를 기술한 것



### 테이블(Table)

- 행과 열의 모델을 사용해 조직된 데이터 요소들의 집합
- SQL DB에서는 테이블 관계라 함
- field = column = 속성(데이터 형식)
- record = row = 튜플(데이터)
- PK(Primary Key): 각 레코드의 고유값, 반드시 설정해야함
- PK는 절대 바꾸지 않는다. 강제로 바꿀 경우 충돌 가능성 높음



## ORM

> Object-Relational-Mapping

- 파이썬과 DB 사이에서 파이썬 언어와 SQL언어로 번역
- SQL을 몰라도 DB 조작 가능
- SQL의 절차적 접근이 아닌 객체 지향적 접근으로 인한 높은 생산성



## Migrations

- django가 model에 생긴 변화를 반영하는 방법



### makemigrations

- model을 변경한 것에 기반한 새로운 마이그레이션(설계도)을 만들 때 사용

```shell
python manage.py makemigrations
```





### migrate

- 마이그레이션을 DB에 반영하기 위해 사용
- 설계도를 실제 DB에 반영하는 과정
- 모델에서의 변경 사항들과 DB의 스키마가 동기화를 이룸

```shell
python manage.py migrate
```





### sqlmigrate

- 마이그레이션에 대한 SQL 구문을 보기 위해 사용
- 마이그레이션이 SQL문으로 어떻게 해석되어 동작할지 미리 확인 가능





### showmigrations

- 프로젝트 전체의 마이그레이션 상태를 확인하기 위해 사용
- migrate 됐는지 안됐는지 여부 확인 가능



## DB API

> ClassName.Manager(objects).QuerySet API
>
> ex) Article.objects.all()

- DB를 조작하기 위한 도구
- Model을 만들면 django는 객체들을 만들고 읽고 수정하고 지울 수 있는 (CRUD) DB-abstract-API를 자동으로 만듦
- Manager
  - django 모델에 DB query 작업이 제공되는 인터페이스
  - 기본적으로 모든 django 모델 클래스에는 objects라는 Manager 추가
- QuerySet
  - DB로부터 전달받은 객체 목록
  - queryset안에 객체는 0개, 1개, 여러개 모두 가능
  - 조회, 필터, 정렬 등 수행할 수 있음

```python
class Article(models.Model):  # 모델 상속, 클래스 이름 = 테이블 이름
    # 각 column 이름, 스키마(각 데이터 타입이 어떻게 되는지)
    title = models.CharField(max_length=100)  # CharField는 글자 수 제한
    content = models.TextField()  # TextField는 글자 수 제한 없음
    created_at = models.DateTimeField(auto_now_add=True)  # 최초 생성 시 현재 시간을 자동으로 넣어줌
    updated_at = models.DateTimeField(auto_now=True)  # 저장 될 때마다 (갱신될 때) 현재 시간을 자동으로 넣어줌
    # models.DateField() => 시, 분, 초 없음, models.DateTimeField() => 시, 분, 초까지
```





## CRUD

> Create(생성), Read(조회), Update(갱신), Delete(삭제)



### Create

```shell
python manage.py shell_plus

article = Article()  # 인스턴스 생성
article.title = 'first'
article.content = 'django!'
article.save()  # save()해야 DB에 저장됨

article = Article(title='second', content='django!!')
article.save()

# 인스턴스 생성X, create가 자동으로 save()해줌
Article.objects.create(title='third', content='django!!!')
```

- save() method를 해야 DB에 저장된다.



### Read

- 새로운 쿼리를 반환하는 메서드: all(), filter()
- 쿼리셋을 반환하지 않는 메서드: get()

- db => articles_article: 앱이름_테이블(모델)이름

- QuerySet은 유사 리스트, 리스트와 비슷하지만 다른 것, 인덱싱, 슬라이싱 가능

- get은 없거나 여러 개 걸리면 에러, 무조건 하나만 걸리게 해야함

- 쿼리셋에서 get으로 하나 들고 온 것은 쿼리셋이 아니다.

- 쿼리셋에서 filter로 들고 온 것은 몇 개이든 쿼리셋으로 가져옴

```shell
Article.objects.get(id=2).delete() # 한줄로 지우기
Article.objects.all()[0].delete() # 한줄로 지우기
```



#### Field lookups

- 조회 시 특정 조건을 적용
- QuerySet Method(get, filter, exclude)



#### get()

- 리턴 값이 한개일 때만 사용
- 리턴 값이 없거나 여러 개의 경우 에러
- 리턴 값이 한개여야 해서 `.get(pk=?)`식으로 주로 사용한다.

- 리턴 값이 쿼리셋 형식 아님



#### filter()

- filter안에 조건에 맞는 레코드 모두 반환
- 반환은 쿼리셋 형식

- 0개든 1개든 여러개든 모두 가능



#### all()

- DB 레코드 모두 쿼리셋 형식으로 반환



### Update

- 데이터를 덮어씀

```shell
article = Article.title
article.title = 'change'
article.save()
# 변경사항 저장
```



### Delete

- 해당 레코드를 삭제
- pk(id)까지 삭제된다. 
- 삭제된 id는 비워둔 채로 둔다. 지워진 id를 재활용하지 않는다.

```shell
article = Article.objects.get(id=1)
article.delete()
# id=1인 DB 레코드 삭제
```



## Admin

- 계정 만들기 => 계정을 DB에 저장
- Admin Site = 사용자가 아닌 서버의 관리자가 활용하기 위한 페이지
- class를 admin.py에 등록하고 관리
- 레코드 생성 여부 확인 유용
- 직접 레코드 삽입 및 수정, 삭제 가능

```python
# 계정 생성
python manage.py createsuperuser
username: ####
password: 
password(again):
```

```python
# admin.py 등록
from django.contrib import admin
from .models import Article  # 상대경로
# Register your models here.
class ArticleAdmin(admin.ModelAdmin):  # admin site customizing class
    # 튜플이나 리스트로 작성, 아래는 필드를 표현하기 위함
    list_display = ('pk', 'title', 'content', 'created_at', 'updated_at') 



# admin site에 등록하겠다.
admin.site.register(Article, ArticleAdmin)
```

