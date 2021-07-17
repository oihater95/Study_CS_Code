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

