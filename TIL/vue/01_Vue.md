# 01_Vue

## Babel & Webpack

### Babel

- JavaScript Transcompiler
- JS의 신버전 코드를 구버전으로 번역/변환 해주는 도구
  - JS는 파편화와 표준화의 영향으로 작성된 코드의 스펙트럼이 매우 다양
  - 최신 문법을 사용해도 브라우저의 버전별로 동작하지 않는 상황 발생
  - 같은 의미의 다른 코드를 작성하는 등의 대응이 필요해졌고 이 문제를 해결하기 위한 도구
- 원시 코드(최신 버전)를 목적 코드(구 버전)으로 옮기는 번역기

- Babel 동작 예시

```js
// Babel Input: ES2015 arrow function (원시 코드)
[1, 2, 3].map((n) => n + 1);

// Babel Output: ES5 equivalent (목적 코드)
[1, 2, 3].map(function(n) {
    return n + 1;
});
```



### Webpack

- static module bundler
- 모듈 간의 의존성 문제를 해결하기 위한 도구



#### Module

- 모듈은 단지 파일 하나를 의미 (ex: 스크립트 하나 === 모듈 하나)
- 배경
  - 브라우저만 조작할 수 있었던 시기의 JS는 모듈 관련 문법없이 사용
  - JS와 애플리케이션이 복잡해지고 크기 커지면서 전역 스코프를 공유하는 형태의 기존 개발 방식의 한계점 드러남
  - 그래서 라이브러리를 만들어 필요한 모듈을 언제든지 불러오거나 **코드를 모듈 단위로 작성하는등의 다양한 시도가 이루어짐**

- 과거 모듈 시스템
  - AMD, CommonJS, UMD
- 모듈 시스템 2015년 표준으로 등재, 현재 대부분의 브라우저와 Node.js가 모듈 시스템을 지원



#### Module 의존성 문제

- **모듈의 수가 많아지고 라이브러리 혹은 모듈 간의 의존성(연결성)이 깊어지면서 특정한 곳에서 발생한 문제가 어떤 모듈 간의 문제인지 파악하기 어려워짐 (의존성 문제)**
  - 예시: A 모듈은 B 모듈의 버전이 4.2 이상일 때 동작 외에는 충돌 발생
- Webpack은 모듈 간의 의존성 문제를 해결하기 위해 존재하는 도구



#### Bundler

- 모듈 의존성 문제를 해결해주는 작업이 Bundling이고 이러한 일을 해주는 도구가 Bundler, Webpack은 다양한 Bundler 중 하나
- 모듈들을 하나로 묶어주고 묶인 파일은 하나(혹은 여러 개)로 만들어짐
- Bundling된 결과물은 더이 상 서순에 영향 받지 않고 동작
- Bundling ㅗ가정에서 문제가 해결되지 않으면 최종 결과물을 만들어 낼 수 없기 때문에 유지&보수 측면에서 매우 편리해짐
  - snowpack, parcel, rollup.js 등의 webpack 이외에도 다양한 모듈 번들러 존재
- Vue CLI는 이러한 Babel, Webpack에 대한 초기 설정이 자동으로 되어있음



#### 의존성 문제 예시

```html
<!--index.html-->
<body>
    <script src="a.js"></script>
    <script src="b.js"></script>
</body>
```

```js
// a.js
const a = 1
console.log(a)

// b.js
a = 2
```

- a.js를 불러온 후 b.js를 불러옴
- a.js에서 const로 a를 선언, 할당함
- b.js에서 a를 재할당하는데 const로 a.js에서 선언과 할당을 했으므로 오류 발생



## Vue

- vue 생성시 git init 되어있는 상태(master)

- babel.config.js => Babel 설정
- node_modules => Node.js의 여러 모듈들이 들어있음 (webpacks 포함)

- public
  - index.html: 뼈대가 되는 html, src의 main.js에서 마운트 대상이 되는 DOM Element들이 존재 (npm run build=> main.js가 동작)
- src
  - assets: webpack에서 빌드되는 static 파일들
  - components: 하위 컴포넌트
  - App.vue: 최상위 컴포넌트
  - main.js: webpack이 빌드할 때 가장 먼저 불러오는 시작점, Vue 전역에서 사용하는 모듈 등록 가능
- package.json
  - scripts: 사용할 명령어 스크립트
  - dependencies: 개발환경 + 배포환경 버전 명시 (requirements)
- package-lock.json:  개발 또는 배포시 동일한 환경을 유지하도록 도와주는 것(종속성), 개발과정에서 의존성 충돌 방지해줌



### App.vue

> template / script / style 로 구분



#### Template

- HTML
- 불러온 components를 사용 (불러온 components의 template)



#### Script

- JS
- components와 연결 (불러오기 & 등록)
- import로 불러오고 export default의 components에 등록



#### Style

- CSS
- App.vue의 style에는 `<style>`만 적혀있음
  - components의 style에는 `<style scoped>`가 되어있는데 `<style scoped>`는 해당 컴포넌트에서만 동작하는 옵션
  - App.vue의 style은 하위 컴포넌트에도 적용



### Components

- 컴포넌트 이름은 PascalCase
- 새 컴포넌트 생성시 `vue + Enter` 하면 기본 뼈대 작성됨



## SFC

> Single File Component

- Vue 컴포넌트 기반 개발의 핵심 특징
- 하나의 컴포넌트는 .vue라는 하나의 파일 안에서 작성되는 코드의 결과물
- 화면의 특정 영역에 대한 HTML, CSS, JS 코드를 하나의 파일(.vue)에서 관리
- .vue 확장자를 가진 싱글 파일 컴포넌트를 통해 개발
- Vue 컴포넌트 === Vue 인스턴스 === .vue 파일



### Component

- 기본 HTML 엘리먼트를 확장하여 **재사용** 가능한 코드르 캡슐화 하는데 도움을 줌
- CS에서는 다시 사용할 수 있는 범용성을 위해 개발된 소프트웨어 구성 요소를 의미
- 컴포넌트는 개발을 함에 있어 유지보수를 쉽게 만들어주고 **재사용성**의 측면에서도 강력한 기능 제공
- Vue 컴포넌트 === Vue 인스턴스







## Vue CLI

- Vue.js 개발을 위한 표준 도구
- 프로젝트의 구성을 도와주는 역할을 하며 Vue 개발 생태계에서 표준 tool 기준을 목표로함
- 확장 플러그인, GUI, ES2015 구성 요소 제공 등 다양한 툴 제공



### Node.js

- JS를 브라우저가 아닌 환경에서도 구동할 수 있도록 하는 JS 런타임 환경
  - 브라우저 밖을 벗어날 수 없던 JS언어의 태생적 한계 해결
- 단순히 브라우저만 조작할 수 있던 JS를 SSR에서도 사용 가능하도록 함



### NPM

- JS 언어를 위한 패키지 관리자
  - pip와 마찬가지로 다양한 의존성 패키지 관리
- Node.js의 기본 패키지 관리자 (Node.js와 같이 설치됨)



### Vue CL 설치

- vue-cli 설치

```bash
$ npm install -g @vue/cli
```

  

- 버전 확인

```bash
$ vue --version
```



- 프로젝트 생성

```bash
$ vue create [프로젝트 이름]
```



- run server

```ba
$ npm run serve
```



## Component

- **컴포넌트 방식에서 data는 반드시 함수**
  - 함수로 안할 경우 스코프 문제로 data 공유됨

- 하위 컴포넌트 사용
  - script에서 import => components에 등록 => template에서 사용

#### components

- 하위 컴포넌트가 있을 때 등록하는 곳

``` vue
<template>
  <div>
    <h1>this is about page</h1>
    <NewComponent my-message="this is prop data" @child-input-change="prarengGetChange"/>  <!--사용-->
  </div>
</template>

<script>
import NewComponent from '@/components/NewComponent.vue'  // 불러오기, @ === '/src' 절대경로
export default {
  name: 'About',
  components: {
    NewComponent  // 등록
  },
  methods: {
    prarengGetChange: function (textInput) {
      console.log(`이것은 하위 컴포넌트 NewComponent로 부터 받은 ${textInput}이다.`)
    }
  }
}
</script>

<style>

</style>
```



#### props

- 상위 컴포넌트에서 넘겨주는 인자
- data 변수명과 type 써줘야함

```vue
<template>
  <div>
    <h2>New Component</h2>
    <h2>{{ myMessage }}</h2>
    <input @keyup.enter="childInputChange" v-model="childInputData" type="text">
  </div>
</template>

<script>
export default {
  name: 'NewComponent',
  data: function () {
    return {
      childInputData: '',
    }
  },
  props: {  // 
    myMessage: {
      type: String,
      required: true,
    }
  },
  methods: {
    childInputChange: function () {
      this.$emit('child-input-change', this.childInputData)
    }
  }
}
</script>

<style>

</style>
```



## Vue Router

- Vue.js의 공식 라우터
- 중첩된 라우트/뷰 매핑 모듈화 된, 컴포넌트 기반의 라우터 설정 등 SPA 상에서 라우팅을 쉽게 개발할 수 있는 기능 제공

- 설치

```bash
$ vue add router
```



### router-link

- **index.js** 파일에 정의한 경로에 등록한 특정한 **컴포넌트와 매핑**
  - index.js => django의 urls.py와 비슷
- HTML5 히스토리 모드에서 router-link는 클릭 이벤트를 차단하여 브라우저가 페이지를 다시 로드하지 않도록 함
- a 태그지만 우리가 알고있는 GET 요청을 보내는 a태그와 조금 다르게 **기본 GET 요청을 보내는 이벤트를 제거한 형태로 구성** => 이벤트 제거 안했다면 페이지가 새로 로드되어 SPA가 아니게 됨



### router-view

- **실제 컴포넌트가 DOM에 부착되어 보이는 자리를 의미**
- router-link를 클릭하면 해당 경로와 연결되어 있는 **index.js에 정의한 컴포넌트가 위치**



### History mode

- HTML history API를 사용해서 router를 구현한 것
- 브라우저 히스토리는 남기지만 실제 페이지는 이동하지 않는 기능을 지원
- 뒤로가기, 앞으로가기



### Vue Router가 필요한 이유

- SPA 등장 이전
  - 서버가 모든 라우팅을 통제
  - 요청 경로에 맞는 HTML을 제공
- SPA 등장 이후
  - 서버는 index.html 하나만 제공
  - 이후 모든 처리는 HTML 위에서 JS 코드를 활용하여 진행
  - 요청에 대한 처리를 더 이상 서버가 하지 않음
- 라우팅 처리 차이
  - SSR
    - 라우팅에 대한 결정권을 서버가 가짐
  - CSR
    - 클라이언트는 더 이상 서버로 요청을보내지 않고 응답 받은 HTML 문서안에서 주소가 변경되면 특정 주소에 맞는 컴포넌트를 렌더링
    - 라우팅에 대한 결정권을 클라이언트가 가짐
  - Vue Router는 라우팅의 결정권을 가진 Vue.js에서 라우팅을 편리하게 할 수 있는 Tool을 제공해주는 라이브러리



### components vs views

- 컴포넌트를 만들어갈 때 정해진 구조가 있는 것은 아님 주로 아래와 같이 구조화 하여 활용
- App.vue
  - 최상위 컴포넌트
- views/
  - router(index.js)에 매핑되는 컴포넌트를 모아두는 폴더
  - ex) App 컴포넌트 내부에 About & Home 컴포넌트 등록
- components
  - router에 매핑된 컴포넌트 내부에 작성하는 컴포넌트를 모아두는 폴더
  - ex) Home 컴포넌트 내부에 HelloWorld 컴포넌트 등록
- 하위 컴포넌트가 없는 경우 The를 붙인다.



### index.js

- 동적 라우팅 => /: 사용
  - path: '/~/:nums'



## Pass Props & Emit Events

- 컴포넌트는 부모-자식 관계에서 가장 일반적으로 함께 사용하기 위함
- 부모는 자식에게 데이터를전달 (Pass Props)하며, 자식은 자신에게 일어난 일을 부모에게 알림 (Emit Event)
  - 부모와 자식이 명확하게 정의된 인터페이스를 통해 격리된 상태로 유지할 수 있음
- props는 아래로, events는 위로
- 부모는 props를 통해 자식에게 데이터를 전달, 자식은 events를 통해 부모에게 메시지를 보냄



### Props

- prop는 상위 컴포넌트의 정보를 전달하기 위한 사용자 지정 특성
- 하위 컴포넌트는 props 옵션을 사용하여 수신하는 props를 명시적으로 선언해야함
- 데이터는 props 옵션을 사용하여 하위 컴포넌트로 전달됨
- 주의: **하위 컴포넌트의 템플릿에서 상위 데이터를 직접 참조할 수 없음**
- 이름 컨벤션
  - HTML: kebab-case
  - script: camelCase



### 단방향 데이터 흐름

- 모든 props는 하위 속성과 상위 속성 사이의 단방향 바인딩을 형성
- **부모의 속성이 변경되면 자식 속성에게 전달되지만, 반대 방향으로는 안됨**
  - 자식 요소가 의도치 않게 부모 요소의 상태를 변경함으로써 앱의 데이터 흐름을 이해하기 어렵게 만드는 일 방지
- **부모 컴포넌트가 업데이트 될때마다 자식 요소의 모든 prop들이 최신 값으로 업데이트 됨**



### Emit Event

- $emit(event)
  - 현재 인스턴스에서 이벤트를 트리거
  - 추가 인자는 리스너의 콜백 함수로 전달
- 부모 컴포넌트는 자식 컴포넌트가 사용되는 템플릿에서 **v-on을 사용**하여 자식 컴포넌트가 보낸 이벤트를 청취(v-on을 이용한 사용자 지정 이벤트)
- 이벤트 이름
  - 컴포넌트 및 props와는 달리 이벤트는 자동 대소문자 변환 제공하지 않음
  - HTML의 대소문자 구분을 위해 DOM 템플릿의 v-on 이벤트 리스너는 항상 자동으로 소문자 변환되기 때문에 v-on:myEvent는 자동으로 v-on:myevent로 변환
  - 이러한 이유로 이벤트 이름에는 kebab-case 권장
