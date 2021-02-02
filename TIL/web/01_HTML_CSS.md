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

가장 많이 사용

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





### 크기 단위



### Box Model



### Display



### Position



