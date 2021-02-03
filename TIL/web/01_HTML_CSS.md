# HTML_CSS

## HTML

> Hyper Text Markup Language

웹페이지의 내용(content)와 구조(structure)를 담당하는 언어

### 기본구조

```html
<!DOCTYPE html>  <!--문서타입 지정: HTML-->
<html lang="ko"> 
<head>
  <meta charset="UTF-8">  <!--전체 인코딩 설정-->
  <title>Hello, HTML</title>
</head>
<body>
  <h1>나의 첫번째 HTML ㄷㄷㄷㅈ</h1>  <!--contents-->
  <p>이것은 본문입니다.</p>  <!--p는 문단Tag-->
  <span>이것은 인라인 요소</span>  <!--span => inline, a도 inline-->
  <a href="https://www.naver.com">네이버로 이동</a>  <!--a href태그는 링크-->

</body>
</html>
```

- `<head>`요소
  - 문서제목, 문자코드와 같이 문서 정보를 담고 있음
  - 브라우저에 나타나지 않음
- `<body>`요소 
  - 브라우저 화면에 나타나는 정보



### 요소

: 시작 태그(start tag)와 종료 태그(end tag) 그리고 태그 사이에 위치한 내용(contents)로 구성

```html
<p>Hello</p>

<!--
<p>: 시작 태그 (start tag)
Hello: 내용(contents)    
</p>: 종료 태그 (end tag)
-->
```



- 요소의 상속(중첩)

```html
<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
  </head>
  <body>
    <h1>안녕하세요</h1>
    <p>반갑습니다!</p>
    <div>
    	<ul>
            <li>리스트</li>
        </ul>    
        
    </div>
  </body>
</html>

<!-- 
h1과 p는 body를 상속한다.
li는 ul을, ul은 div를 상속
-->
```



### 속성(attribute)

- 요소의 성질, 특징을 정의
- 요소에 추가적인 정보(이미지 파일 경로, 크기 등)제공
- 시작 태그에 위치하며 이름과 값의 쌍을 이룬다(key=value)
- 데이터 할당 및 저장이 아니다.

```html
<img src="html.jpg" width="104" height="142">
<!--
src, width, height 는 속성명
"html.jpg", "104", "142"는 속성값
```



### 시맨틱 요소 (시맨틱 태그)

> 의미부여한 Tag, 가독성을 높여준다.

- `<h1>~<h6>`: 제목 태그
- `<header>`: 머릿말
- `<nav>`: 내비게이션
- `<aside>`: 사이드에 위치하는 공간 의미
- `<section>`: 문서의 일반적인 구분, 본문의 여러내용(article)을 포함하는 공간
- `<article>`: 본문의 주내용이 들어가는 공간
- `<footer>`: 마지막 부분

- Non-Semantic(의미갖지 않음)
  - `<div>`: 구역 나누기 태그 (Block)
  - `<span>`: 텍스트 묶기 (Inline)



### 주요 속성(추가 예정)

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
</head>
<body>
  <h1>This is Heading 1</h1>
  <h2>Heading 2</h2>
  <h3>Heading 3</h3>
  <h4>Heading 4</h4>
  <h5>Heading 5</h5>
  <h6>Heading 6</h6>

  <p>본문(paragraph)</p>
  <ol>  <!-- 순서가 있는 리스트 Ordered list -->
    <li>쌀을 씻는다</li>
    <li>밥을 한다</li>
    <li>md: 1. </li>
  </ol>

  <!-- ul>li*3 + Tab 자동완성 사용 -->
  <ul>  <!-- 순서가 없는 리스트 Unordered list -->
    <li>순서가 없는 리스트</li>  
    <li>Unordered List</li>
    <li>md: - </li>
  </ul>

  <!-- form => 하나의 박스 -->
  <form action="">  <!-- action => attribute(key=value), 할당 저장 아님 -->
    <input type="text">  <!-- type => attribute, Inline -->
    <input type="text">
    <input type="submit">  <!-- 제출확정? -->
  </form>
  <div>
    <input type="text">  
  </div>
  <div>
    <input type="text">
  </div>
  <div>
    <input type="submit">
  </div>
  

  <div></div>
  <section></section>
  <header></header>
  <article></article>
  <aside></aside>
  <footer></footer>
  <nav></nav>
  <h2>여기까지는 Block 요소들</h2>

  <hr>  <!-- 가로선 -->

  <h2>여기서부터는 Inline 요소들</h2>

  <a href=""></a>
  <span></span>
  <b></b>
  <strong></strong>
  <i></i>
  <em></em>
  <!-- b와 i는 거의 안쓴다. 모양만 낸 것이라서, 강조의미가 있는 strong과 em 사용 -->
  
  <a href="https://google.com">google</a>은 내가 자주 사용하는 검색엔진
  <button>HTML</button> <em>문서</em>에서 가장 <strong>중요한</strong> 내용은 다음과 같다.
  <br>
  시험 성적 확인은 <a href="https://edu.ssafy.com" target="_blank">이곳</a>에서
  <!-- target="_blank" => 새 탭에서 열기, 없으면 현재 탭에서 열기 -->

  
</body>
</html>

<!-- html 선언, Alt + B = open in browser 
기본 tag => html, head, body, 하지만 없어도 에러 안남 
html은 프로그래밍 언어가 아니기 때문에 
! + Tab을 하면 기본 프레임 만들어줌 
Tag + Tab => 자동완성
Ctrl + Enter => 아랫 줄 추가
Ctrl + Shift + Enter => 윗줄 추가
Alt + 방향키 위아래 => 해당 줄 위치 옮기기

Block Element = 해당 줄 면적을 모두 차지, 옆에 못 씀
Inline Element = 해당 줄 면적을 일부 차지, 옆에 쓸 수 있음
<br> => 줄바꿈

브라우저 보고 고치는 html은 NO
html은 초안일뿐 세세한 조정은 못한다.(글자 크기, 행간 거리 등등)
세부사항(스타일) 조정은 CSS에서 한다.
-->

```





## CSS

> Cascading Style Sheets

시각적인 디자인과 레이아웃 표현

- CSS 정의 방법

  - Inline

  ```css
  <h1 style="color: blue; font-size: 10px;">Hello</h1>
  ```

  

  - 내부 참조

  ```css
  <style>
    h1 {
        color: blue;
    }
  </style>
  ```

  

  - 외부 참조

  ```css
  <link rel="stylesheet" href="reference.css">
  
  /* reference.css */
  h1 {
      color: blue;
  }
  ```

  

  

### 선택자 selector

> 스타일을 적용하고자 하는 HTML 요소를 선택하는 수단

- Property: 표준 스펙으로 이미 지정되어 있음, 임의 설정 불가, 여러 개의 프로퍼티를 연속해서 지정 가능 ;로 구분
- Value: 해당 프로퍼티에 사용할 수 있는 값을 키워드나 크기 단위 또는 색상 표현 단위 등의 특정 단위로 지정

![selector](01_HTML_CSS.assets/selector.PNG)



CSS를 위해 id 선택자를 사용하지 않는다. 클래스 선택자 이용

#### 요소(태그) 선택자 Type Selector

```css
/* 모든 p 태그 요소를 선택 */
<style>
	p {color: red;}
</style>
<body>
	<p>paragraph</p>
</body>

/* 모든 요소 선택 */
* {color: blue;}
```



#### ID 선택자

- id는 문서당 한번만 사용할 수 있고 요소에는 단일 id값만 적용할 수 있다.

```css
/* #사용 */
<style>
	#p1 {color: red;}
</style>

<body>
    <p id="p1">paragraph1</p>  /* id=p1만 적용 */
    <p id="p2">paragraph1</p>
</body>
```



#### 클래스 선택자

- 가장 많이 사용
- 상속받은 스타일보다 직접 적용된 스타일이 우선순위가 높다

```css
/* . 사용 */
<style>
/* class 어트리뷰트 값이 container인 모든 요소를 선택 */
/* color 어트리뷰트는 자식 요소(p)에 상속된다. */
.container { color: red; } 
</style>
<body>
  <div class="container">
    <p id="p1">paragraph 1</p>
    <p id="p2">paragraph 2</p>
  </div>
  <p>paragraph 3</p>
</body>

```



#### Inline 선택자 (속성 선택자)

```css
<h2 style="color: yellowgreen;">Heading 2</h2> 
```



#### 자손(후손) 선택자

- selector A selector B
- selector A의 모든 후손(하위) 요소 중 selector B와 일치하는 요소 선택(하위의 하위 가능)

```css
<!DOCTYPE html>
<html>
<head>
  <style>
    /* div 요소의 후손요소 중 p 요소 */
    div p { color: red; }
  </style>
</head>
<body>
  <h1>Heading</h1>
  <div>
    <p>paragraph 1</p>
    <p>paragraph 2</p>
    <span><p>paragraph 3</p></span>
  </div>
  <p>paragraph 4</p>
</body>
</html>

/* div의 자손 p(paragraph1~3) (span안의 p까지) 모두 영향을 받음 */
```



#### 자식 선택자

- selector A > selector B
- selector A의 모든 자식 요소(후손 요소와 다름) 중 selector B와 일치하는 요소 선택

```css
<!DOCTYPE html>
<html>
<head>
  <style>
    /* div 요소의 자식요소 중 p 요소 */
    div > p { color: red; }
  </style>
</head>
<body>
  <h1>Heading</h1>
  <div>
    <p>paragraph 1</p>
    <p>paragraph 2</p>
    <span><p>paragraph 3</p></span>
  </div>
  <p>paragraph 4</p>
</body>
</html>

/* div의 자식 p(paragraph1, 2)만 영향받음 paragraph3은 span의 하위라 div의 자식이 아닌 자손*/
```



#### 인접 형제 선택자

- selector A + selector B
- 선택자 A의 형제 요소 중 선택자 A 바로 뒤에 위치하는 선택자 B 요소 선택
- A와 B 사이에 다른 요소 존재 시 선택되지 않음

```css
<!DOCTYPE html>
<html>
<head>
  <style>
    /* p 요소의 형제 요소 중에 p 요소 바로 뒤에 위치하는 ul 요소를 선택한다. */
    p + ul { color: red; }
  </style>
</head>
<body>
  <div>A div element.</div>
  <ul>
    <li>Coffee</li>  /*그냥 ul은 영향 없음*/
    <li>Tea</li>
    <li>Milk</li>
  </ul>

  <p>The first paragraph.</p>
  <ul>
    <li>Coffee</li>  /* p다음 ul 영향받음*/
    <li>Tea</li>
    <li>Milk</li>
  </ul>
</body>
</html>
```



#### 일반 형제 선택자

- 선택자 A ~ 선택자 B
- 선택자 A의 형제 요소 중에서 선택자 A 뒤에 위치하는 선택자 B 요소를 모두 선택

```css
<!DOCTYPE html>
<html>
<head>
  <style>
    /* p 요소의 형제 요소 중에 p 요소 뒤에 위치하는 ul 요소를 모두 선택한다.*/
    p ~ ul { color: red; }
  </style>
</head>
<body>
  <div>A div element.</div>
  <ul>
    <li>Coffee</li>
    <li>Tea</li>
    <li>Milk</li>
  </ul>

  <p>The first paragraph.</p> /* 여기부터 모든 ul은 영향받음*/
  <ul>
    <li>Coffee</li>
    <li>Tea</li>
    <li>Milk</li>
  </ul>

  <h2>Another list</h2>
  <ul>
    <li>Coffee</li>
    <li>Tea</li>
    <li>Milk</li>
  </ul>
</body>
</html>
```



#### !important

- 어떤 선택자이든 다 무시하고 가장 우선
- 잘 안씀



#### 선택자 우선순위

1. !important
2. Inline 선택자
3. Id 선택자
4. Class 선택자
5. 요소(태그) 선택자
6. 동일한 우선순위라면 소스 코드 순서가 나중에 읽힌 것 우선
7. 상속받은 것보다 직접 쓰여진 것이 더 우선

```css
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
  <style>
    h2 {
      color: darkviolet !important;
    }
    p {
      color: orange;
    }
    .blue{
      color: blue;
    }
    .green {
      color: green;
    }
    #red {
      color: red;
    }
  </style>
</head>
<body>
  <p>1</p>  <!-- 요소 선택자 스타일 -->
  <p class="blue">2</p>  <!-- 클래스 선택자 스타일 -->
  <p class="blue green">3</p>  <!-- green 클래스 선택자 스타일이 더 최근에 읽힘 -->
  <p class="green blue">4</p>  <!-- green 클래스 선택자 스타일이 더 최근에 읽힘 -->
  <p id="red" class="blue">5</p>  <!-- id 선택자 스타일 -->
  <h2 id="red" class="blue">6</h2>  <!-- h2 선택자 스타일 !important -->
  <p id="red" class="blue" style="color: saddlebrown;">7</p>  <!-- Inline style -->
  <h2 id="red" class="blue" style="color: yellowgreen;">8</h2>  <!-- h2 선택자 스타일 !important -->
</body>
</html>
```





### 크기 단위

- px: 절대값 but 디바이스마다 차이가 있다.
- em: 상대값, 배수 단위, 요소에 지정된 사이즈(상속 or 디폴트)에 상대적인 사이즈를 설정한다.
  - 크기 단위도 상속된다.
- %: 상대값, 요소에 지정된 사이즈(상속 or 디폴트)에 상대적인 사이즈 출력
- rem: 절대값, 최상위 요소(html)을 기준으로 함.

```css
<!DOCTYPE html>
<html lang="en"> /*default = 16px*/
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
</head>
  <style>
    .em {
      font-size: 1.5em;
    }

    .rem {  /* 주로 사용 고정 비율이라서 */
      font-size: 1.5rem;
    }

  </style>
<body>
  <ul class="em">
    <li class="em">1.5em</li>  <!-- 16*1.5(ul)*1.5(li) = 32px (상속 받은 것도 곱해짐)-->
    <li class="rem">1.5rem</li>  <!-- 16*1.5 = 24px -->
    <li>no class</li>  <!-- 16*1.5(ul) = 24px (상속받음)-->
  </ul>
  
</body>
</html>
```



### Box Model

- Content: 요소의 텍스트나 이미지 등 실제 내용 위치하는 영역
- Padding: Border(테두리) 안 쪽의 내부 여백 영역
- Border: 테두리 영역
- Margin: Border 바깥에 위치하는 요소의 외부 여백 영역

![box model](01_HTML_CSS.assets/box model.PNG)

```css
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
  <style>
    .box{
      width: 100px;
      margin: 10px auto; /*상하 좌우, 4개의 값이면 상 우 하 좌 시계방향*/
      padding: 20px;
      border: 1px solid black;
      color: white;  /* 텍스트 색상 */
      text-align: center;  /* 텍스트 가운데 정렬 */
      background-color: blueviolet;
    }

    .box-sizing{
      box-sizing: border-box;
      margin-top: 50px;  /* 이론상 위 박스 10px + 아래 박스 50px로 60px가 되어야하지만
      마진 상쇄가 일어나 위 박스 10px이 상쇄되어 50px만 나타남 */
    }

  </style>
</head>
<body>
  <div class="box">content-box</div>
  <div class="box box-sizing">border-box</div>
</body>
</html>
```



### Display

| Property 값 키워드 | 설명                                                  |
| ------------------ | ----------------------------------------------------- |
| block              | block은 해당 열을 모두 차지, 옆에 아무것도 올 수 없다 |
| inline             | inline은 일부만 차지, 옆에 올 수 있다.                |
| inline-block       | 일부만 자리 차지하지만 block의 특징도 가짐            |
| none               | 화면에 표시 x (공간도 사라짐)                         |

#### Block

- 항상 새로운 라인에서 시작한다.

- 화면 크기 전체의 가로폭을 차지한다. (width: 100%)

- width, height, margin, padding 프로퍼티 지정이 가능하다.

- block 레벨 요소 내에 inline 레벨 요소를 포함할 수 있다

- block 레벨 요소 예

  - div
  - h1 ~ h6
  - p
  - ol
  - ul
  - li
  - hr
  - table
  - form

  

#### Inline

- 새로운 라인에서 시작하지 않으며 문장의 중간에 들어갈 수 있다. 즉, 줄을 바꾸지 않고 다른 요소와 함께 한 행에 위치한다.

- content의 너비만큼 가로폭을 차지한다.

- **width, height, margin-top, margin-bottom 프로퍼티를 지정할 수 없다.** 상, 하 여백은 line-height로 지정한다.

- inline 레벨 요소 뒤에 공백(엔터, 스페이스 등)이 있는 경우, 정의하지 않은 space(4px)가 자동 지정된다.

- inline 레벨 요소 내에 block 레벨 요소를 포함할 수 없다. inline 레벨 요소는 일반적으로 block 레벨 요소에 포함되어 사용된다.

- inline 레벨 요소 예

  - span
  - a
  - strong
  - img
  - br
  - input
  - select
  - textarea
  - button

  

#### Inline-block

- 기본적으로 inline 레벨 요소와 흡사하게 줄을 바꾸지 않고 다른 요소와 함께 한 행에 위치시킬 수 있다.
- block 레벨 요소처럼 width, height, margin, padding 프로퍼티를 모두 정의할 수 있다. 상, 하 여백을 margin과 line-height 두가지 프로퍼티 모두를 통해 제어할 수 있다.
- content의 너비만큼 가로폭을 차지한다.
- inline-block 레벨 요소 뒤에 공백(엔터, 스페이스 등)이 있는 경우, 정의하지 않은 space(4px)가 자동 지정된다



#### None

- 해당 요소를 화면에서 사라지게 하며 요소의 공간조차 사라지게 한다.
- `visibility: hidden;`은 해당 요소를 화면에서 사라지게는 하나 공간은 사라지지 않는다.



### Position

#### static

- default이다.
- 기본적인 요소의 배치 순서에 따라 위에서 아래로, 왼쪽에서 오른쪽으로 순서에 따라 배치되며 부모 요소 내에 자식 요소로서 존재할 때는 **부모 요소의 위치를 기준으로 배치**된다.
- 좌표 프로퍼티(top, bottom, left, right)를 같이 사용할 수 없으며 사용할 경우에는 무시된다.



#### relative

- 기본 위치(static으로 지정되었을 때의 위치)를 기준으로 좌표 프로퍼티(top, bottom, left, right)를 사용하여 위치를 이동시킨다.



#### absolute

- **부모 요소 또는 가장 가까이 있는 조상 요소(static 제외)를 기준으로 좌표 프로퍼티(top, bottom, left, right)만큼 이동한다. 즉, relative, absolute, fixed 프로퍼티가 선언되어 있는 부모 또는 조상 요소를 기준으로 위치가 결정된다.**
- 만일 부모 또는 조상 요소가 static인 경우, document body를 기준으로 하여 좌표 프로퍼티대로 위치하게 된다.



#### fixed

- 부모 요소와 관계없이 브라우저의 viewport를 기준으로 좌표프로퍼티(top, bottom, left, right)을 사용하여 위치를 이동시킨다.

**스크롤이 되더라도 화면에서 사라지지 않고 항상 같은 곳에 위치한다.**

```css
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Position</title>
</head>
<style>
  div{
    height: 100px;  /* div(block) style */
    width: 100px;  /* div style */
    background-color: purple;  /* div style */
    color: white;  /* 여기서 부터 contents(text) style */
    line-height: 100px;  /* 행간(줄간격), 위 아래 50px*/
    text-align: center;  /* 가운데 정렬 */
  }

  .parent{
    position: relative;
    margin: 0 auto;
    width: 300px;
    height: 300px;
  }

  .abs{
    /* 원래 있던 자리 비워주고 이동 */
    position: absolute;
    top: 100px;
    background-color: seagreen;
  }

  .rel{
    /* 원래 있던 자리도 차지하면서 이동 */
    position: relative;
    top: 100px;
    background-color: steelblue;
  }

  .sibling{
    width: 200px;
    height: 100px;
    background-color: hotpink;
  }


  .parent-static{
    position: static;
    margin: 0 auto;
  }

  .child {
    /* 특별한 (static이 아닌)부모 요소가 없으면 
       body 기준으로 움직인다 
       static 아닌 부모 요소가 있으면 그 부모를
       기준으로 움직인다. 
       static이 아닌 부모가 여러 개가 있으면
       가장 인접한 부모를 기준으로 한다.*/
    position: absolute;
    background-color: black;
    top: 50px;
    left: 50px;
  }

  .fixed {
    /* 스크롤해도 위치 고정(카톡 입력창처럼) */
    position: fixed;
    width: 100%;
    bottom: 0;
  }

</style>
<body>
  <div class=fixed>Fixed</div>

  <div class="parent">
    부모(relative)
    <div class="child">
      <!-- relative부모 좌상단 기준 -->
      자식(absolute)
    </div>
  </div>  


  <div class="parent-static">
    부모(static)
    <div class="child" style="color:crimson">
      <!-- html 좌상단 기준 -->
      자식(absolute)
    </div>
  </div>

  <!-- div.parent>div.abs+div.sibling --> 
  <div class="parent" style="background-color: khaki;">
    <div class="abs">abs형</div>
    <div class="sibling">동생</div>
  </div>

  <div class="parent" style="background-color: khaki;">
    <div class="rel">rel형</div>
    <div class="sibling">동생</div>
  </div>


  <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Itaque laborum assumenda accusantium fuga eaque est neque odit sint sit officia, quas quo cumque, ducimus ipsam minima magni repellat quisquam ab?</p>
  <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Numquam, fugiat neque? Delectus soluta, reiciendis quibusdam atque culpa quidem earum velit est commodi, veniam maiores quam perspiciatis aspernatur quis a praesentium.</p>
  <p>Lorem ipsum dolor, sit amet consectetur adipisicing elit. Praesentium, necessitatibus numquam! Quae vel temporibus accusantium dolorem, mollitia cumque nulla veniam minus dolores ratione, nisi expedita nemo qui cupiditate voluptatibus reprehenderit.</p>
  <p>Lorem ipsum dolor sit, amet consectetur adipisicing elit. Voluptate nemo alias nulla nihil quaerat quam consectetur excepturi nisi perferendis perspiciatis assumenda vero ratione saepe iure debitis, veniam sunt nobis officia.</p>
  <p>Lorem ipsum, dolor sit amet consectetur adipisicing elit. Debitis nesciunt, odio voluptates eum possimus dolor laboriosam voluptas ullam obcaecati esse, cum libero fugit veniam commodi? Rerum corporis aliquam iure. Ipsa?</p>
</body>
</html>

<!-- absolute는 위에 떠있다고 보면 됨 -->
```

