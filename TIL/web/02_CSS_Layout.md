# CSS_Layout

>웹페이지에 포함되는 요소들을 어떻게 취합하고 그것들이 어느 위치에 놓일 것인지를 제어한다.



## Float

> float한 요소를 좌,우측 주변으로 텍스트 및 inline요소 둘러싸는 레이아웃

- float 속성
  - none: 기본값(양 쪽)
  - left: 요소를 왼쪽에 float, 오른쪽만 둘러싸진다
  - right: 요소를 오른쪽에 float, 왼쪽만 둘러싸진다.



### clearfix

- float 요소와 다른 텍스트가 아닌 block 요소간의 레이아웃 깨짐을 막기 위해 사용

```css
/* clear: left, right, both*/
/* ::after 해당 클래스 수행 후 after 구문 수행*/
.clearfix::after {
  content: "";
  display: block;
  clear: both;  /* 양 쪽 올라오는 것 막음 */
} 
```



## FlexBox

![flexbox](02_CSS_Layout.assets/flexbox.png)

- 요소
  - flex container
  - flex items
- 축
  - main axis(주축)
  - cross axis(교차축)



### flex container

- flexbox 레이아웃을 형성하는 가장 기본적인 모델
- flexbox가 놓여있는 영역
- main axis => justify
- cross axis => align
- content: 여러 줄
- items: 한 줄
- self: 개별 요소 (자식 요소에서 사용)
- 부모 요소에 flex 부여

```css
.flex-container{
      /* 정렬하려고 하는 부모 요소에 선언 => 자식요소에게만 영향, 후손요소는 X */
      display: flex;

      /* 요소들이 강제로 한줄에 배치되게 할 것인지 여부 설정 */
      flex-wrap: wrap;  /* defalut는 nowrap => 컨테이너 벗어둔 채로 둠 */
      /* wrap => 컨테이너 벗어나면 벗어난 요소들을 컨테이너 내부 아래쪽에 다시 정렬 
      column일 경우 내부 오른쪽에 다시 정렬*/

      /* 메인축 방향 설정, 쌓이는 방향 설정 (메인축의 방향만 바뀜, flex는 단방향) */
      flex-direction: row-reverse;  /* right to left */
      flex-direction: column;  /* top to bottom */
      flex-direction: row; /* left to right */

      /* 메인축 정렬 */
      justify-content: flex-start;  /* 왼쪽으로 정렬(이동) default */
      justify-content: flex-end;   /* 오른쪽으로 정렬(이동)되지만 row-reverse와 다름 */
      /* row-reverse는  오른쪽에서 321 로 정렬되지만, flex-end는 오른쪽에 123으로 정렬*/
      justify-content: center;  /* 중앙으로 이동 */
      justify-content: space-between;  /* 요소 사이 공간 생김 양 쪽 끝 여백은 없음*/
      justify-content: space-around;  /* 요소 양 옆에 동일한 여백 생김 여백 겹치지 않음*/
      justify-content: space-evenly; /* 요소 양 옆에 동일한 여백 생김, 여백 겹쳐져 같은 너비가짐 */
      justify-content: flex-start;

      /* 교차축 정렬 */
      align-items: stretch;  /* default 높이 컨테이너에 맞게 맞춰줌 */
      align-items: flex-start;  /* 높이 작아짐, top에 정렬 */
      align-items: baseline;  /* item들의 폰트크기가 다를 때 중앙기준 정렬 */
      align-items: stretch;
      /* 수직 수평 가운데 정렬 */
      /* justify-content: center;
      align-items: center; */

      /* flex-flow: column wrap; => flex-direction + flex-wrap */ 
    }
```

```css
.item1{
      align-self: flex-start;
      order: 0; /* 0이 default */
      flex-grow: 1;  /* 남는 공간 분배 */
    }

    .item2{
      align-self: center;
      order: -1; /* 0기준 왼쪽으로 이동 */
      flex-grow: 2;
    }

    .item3{
      align-self: flex-end;
      order: 1; /* 0기준 오른쪽으로 이동 */
      flex-grow: 3;
    }
    /* 현재 flex-grow(음수 불가) 총합이 6 => 남는 공간 6등분하고 
    flex-grow: 1 => 1/6, flex-grow: 2 => 2/6, flex-grow: 3 => 3/6  */ 

```





## Bootstrap

> 반응형 웹 디자인, 그리드 시스템 지원

- 클래스 사용 ex) class="d-flex justify-content-center"
- d-flex => display: flex (flexbox)

```css
<head>
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" crossorigin="anonymous">
</head>

<body>
  <h1>적용 되었나?</h1>
  <h2>spacing</h2>
  <div class="box mt-3 ms-5">1</div>  
  <div class="box m-4">2</div>
  <div class="box mx-auto">3</div>  <!-- 수평 중앙정렬 -->  
  <div class="box ms-auto">4</div>  <!-- 오른쪽 정렬 -->  

  <hr>

  <h2>Color</h2>
  <!-- 배경색은 bg-  -->
  <div class="bg-primary">이건 파랑</div>
  <div class="bg-success">이건 초록</div>
  <div class="bg-warning">이건 노랑</div>

  <!-- 글씨색 text-  -->
  <p class="text-danger">이건 빨간색</p>
  <p class="text-info">이건 하늘색</p>
  <p class="text-secondary">이건 회색</p>

  <h2>Text</h2>
  <p class="text-start">Start aligned text on all viewport sizes.</p>
  <p class="text-center">Center aligned text on all viewport sizes.</p>
  <p class="text-end">End aligned text on all viewport sizes.</p>

  <!-- sm 범위로 들어오면 none(사라짐), md 사이즈로 오면 block -->
  <span class="d-block p-2 d-sm-none d-md-block bg-primary text-white">d-block</span>

   <!-- md 범위로 들어오면 none(사라짐), lg 사이즈로 오면 block -->
  <span class="d-block p-2 d-md-none d-lg-block bg-dark text-white">d-block</span>
  <!-- sm, md, lg => grid breakpoints의 요소(크기 범위) -->

  <!-- /body바로 위에 씀 -->
  <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/js/bootstrap.bundle.min.js" integrity="sha384-ygbV9kiqUc6oa4msXn9868pTtWMgiQaeYH7/t7LECLbyPA2x65Kgf80OJFdroafW" crossorigin="anonymous"></script>
</body>
```

```css
/* flexbox 사용가능 */
<footer class="d-flex align-items-center justify-content-center
  fixed-bottom bg-primary text-white mt-5">
    <p>HTML & CSS project.</p>
  </footer>
```



- Bootstrap Docs

: https://getbootstrap.com/docs/5.0/getting-started/introduction/



### Component

모르는 것 위주로 추가 예정

- display-1: 글씨 크기(Heading)
- Grid (row-cols-n): col-n은 12칸 중 n칸 배분이지만 row-cols-n은 1개의 row에 col을 n개 생성한다는 의미

```html
<section class="row g-3 row-cols-sm-1 row-cols-md-2 row-cols-lg-4"> <!-- grid -->
        <a class="text-decoration-none text-dark" href="">
          <article class="card">
            <img class="img-fluid card-img-top" src="images/buds.jpg" alt="buds image">
            <div class="card-body">
              <h3 class="card-title fs-5 p-1">Buds</h3>
              <p class="card-text">179,000</p>
            </div>
          </article>
        </a>
    
=

 <section class="row"> <!-- grid -->
        <!-- card Component 사용 .card, .card-img-top, card-body -->
        <a class="text-decoration-none text-dark col-md-6 col-lg-3 g-2" href="">
          <article class="card">
            <img class="img-fluid card-img-top" src="images/buds.jpg" alt="buds image">
            <div class="card-body">
              <h3 class="card-title fs-5 p-1">Buds</h3>
              <p class="card-text">179,000</p>
            </div>
          </article>
        </a>    
```



- gutter: grid 사이 간격(padding)

```css
<section class="row g-3 "> <!-- grid -->
    
        <article class="col-12 col-md-6 col-lg-3">
          <div class="card">
            <img class="img-fluid card-img-top" src="images/buds.jpg" alt="buds image">
            <div class="card-body">
              <h3 class="card-title fs-5 p-1">Buds</h3>
              <p class="card-text">179,000</p>
            </div>
          </div>
        </article>
```



- img-fluid: 반응형 이미지
- container-fluid: 반응형 컨테이너
- a태그의 text-decoration-none: 밑줄 삭제

## Grid System

- 부트스트랩의 grid system 은 containers, rows 그리고 columns 를 사용해서 컨텐츠를 레이아웃하고 정렬한다.
- d-flex와 혼용하지 않는게 좋다.
- 12개의 column 가진다 => 12가 약수가 많기 때문에
- 구조
  - .container > .row > col-*

### row

- column의 wrapper
- column에는 공간 사이를 제어하기 위한 좌우 padding값 gutter 존재
  - row의 margin 값과 gutter 제거하려면 .row에 .no-gutter class 사용



### col

- column 클래스는 row당 가능한 12개 중 사용하려는 column 수 나타냄
- column 너비는 백분율로 설정되므로 항상 부모 요소를 기준으로 유동적으로 크기 조정
- grid layout에서 내용은 반드시 column안에 있어야하며 오직 column만이 row의 직계 자식 요소일 수 있다.
- 12칸을 초과한 칸은 밑으로 내려간다.
- 

```css
<div class="container">  <!-- container 안써주면 적용안됨 -->
    <div class="row">
      <!-- 3개의 col이 12칸 중 4칸씩 가짐 -->
      <div class="box col">1</div>
      <div class="box col">2</div>
      <div class="box col">3</div>
    </div>

	<div class="row">
      <!-- 12칸을  2칸, 8칸, 2칸 나눠가짐 -->
      <div class="box col-2">1</div>
      <div class="box col-8">2</div>
      <div class="box col-2">3</div>
    </div>
</div>
```



### offset

- 지정한 offset 만큼의 column 공간 무시하고 다음 공간부터 컨텐츠 적용
- 같은 라인에 offset과 col구문이 있으면 offset이 먼저 적용

```css
<div class="row"> /*4칸 띄고 시작*/
      <div class="box col-4 offset-4">1</div>
      <div class="box col-4">2</div>
</div>
```

```css
<div class="row">
      <div class="item col-4 offset-md-4 offset-lg-7 col-lg-5">
        <p>item1</p>
      </div>
      <div class="item col-4 offset-4 offset-md-0 offset-lg-2 col-lg-8">
        <p>item2</p>
      </div>
    </div>
```



- btn: 버튼



### nesting (중첩)

```css
<!-- 중첩 nesting -->
<div class="row">
  <div class="box col-6">
    <div class="row">
      <div class="box col-3">1</div>
      <div class="box col-3">2</div>
      <div class="box col-3">3</div>
      <div class="box col-3">4</div>
    </div>  
  </div>
  <div class="box col-6">2</div>
  <div class="box col-6">3</div>
  <div class="box col-6">4</div>
</div>

/*
6칸(3|3|3|3)	|	6칸
6칸			|	6칸
*/
```



### Grid breakpoints

- 부트스트랩 grid system 은 다양한 디바이스에서 적용하기 위해 특정 px 조건에 대한 지점을 정해 두었는데 이를 breakpoints 라고 한다

- 부트스트랩은 대부분의 크기를 정의하기 위해 em 또는 rem 을 사용하지만 px 는 그리드  breakpoint 에 사용된다. (뷰포트 너비가 픽셀 단위이고 글꼴 크기에 따라 변하지 않기 때문)

```css
<h2>Grid breakpoints</h2>
    <div class="row">
      <!-- sm 사이즈 넘어가면 비율 8:2:2 md 넘어가면 4:4:4 -->
      <div class="box col-2 col-sm-8 col-md-4">1</div>
      <div class="box col-8 col-sm-2 col-md-4">2</div>
      <div class="box col-2 col-sm-2 col-md-4">3</div>
    </div>
```



### 크기

- xs(none): 0 이상

- sm: 576 이상

- md: 768px 이상

- lg: 992px 이상

- xl: 1200px 이상

- xxl: 1400px 이상