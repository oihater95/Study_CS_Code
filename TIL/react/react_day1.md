# React

## 1. Hello World

   > 가장 기본적인 React 예시

```react
ReactDOM.render(
    <h1>Hello, world!</h1>,
     document.getElementById('root')
);
```


   ## 2. JSX

> JSX는 JS를 확장한 문법으로 React Element를 생성

```react
const element = <h1>Hello, world!</h1>;
```

- 리액트에서는 렌더링로직이 UI로직(이벤트가 처리되는 방식, 시간에 따라 state가 변하는 방식, 화면에 표시하기 위해 데이터가 준비되는 방식 등)과 연결
- 리액트는 마크업과 로직 모두 포함하는 '컴포넌트' 유닛으로 구성
- HTML보다는 JS에 가깝기 때문에 React DOM은 camelCase 사용 => `<div class>`가 아닌 `<div className>` 사용
- 예시 1

```react
const name = 'Josh'
const element = <h1>Hello, {name}</h1>
ReactDOM.render(
  element,
  document.getElementById('root')
);
```
- 예시 2 (함수 사용)

```react
function formatName(user) {
  return user.firstName + ' ' + user.lastName;
}

const user = {
  firstName: 'Harper',
  lastName: 'Perez'
};

const element = (
  <h1>
    Hello, {formatName(user)}!  </h1>
);

ReactDOM.render(
  element,
  document.getElementById('root')
);
```

- JSX는 표현식 => 컴파일이 끝나면 JSX 표현식이 JS함수 호출, JS 객체로 인식

- JSX를 `if` 구문 및 `for` 루프 안에 사용하고, 변수에 할당 또는 인자로 인식, 함수로부터 반환 가능

- 예시

  ```react
  function getGreeting(user) {
  if (user) {
    return <h1>Hello, {formatName(user)}!</h1>;  }
  return <h1>Hello, Stranger.</h1>;}
  ```



### JSX 속성 정의

- 문자열 리터럴("")

    ```react
    const element = <div tabIndex="0"></div>
    ```




- JS 표현식 삽입(중괄호)

  ```react
  const element = <img src={user.avatarUrl}></img>
  ```

  

- JS 표현식 삽입할 때 중괄호 주변에 `""` 입력 X 둘 중 하나만 사용할 것



### JSX 자식 정의
```react
const element = (
	<div>
		<h1>Hello!</h1>
		<h2>Good to see you here.</h2>
	</div>
);
```
### JSX 사용자 입력
```react
const title = response.potentiallyMaliciousInput;
const element = <h1>{title}</h1>;
```

- **React DOM은 JSX에 삽입된 모든 값을 렌더링하기 전에 escape => 명시적으로 작성되지 않은내용은 주입X**

- 모든 항목은 렌더링 되기 전에 문자열로 변환

- XSS 공격을 방지

  

### JSX 객체 표현
- 아래 두 예시는 동일한 출력

  ```react
  const element = (
      <h1 className="greeting">
    		Hello, world!
  	</h1>
   );
  
  const element = React.createElement(
  	'h1',
  	{className: 'greeting},
  	'Hello, world!');
  ```

  

- `React.createElement()`는 버그 검사 수행 후 객체를 생성

  ```react
  // 실제로 생성되는 객체가 아닌 단순화한 객체
  // 이러한 객체를 React Element라 함
  const element = {
      type: 'h1',
      props: {
        className: 'greeting',
        children: 'Hello, world!'
      }
  };
  ```

- React는 이 객체를 읽어 DOM을 구성하고 최신 상태로 유지하는 데 사용



## 3. 엘리먼트 렌더링
> React 앱의 가장 작은 단위

- 브라우저 DOM 엘리먼트와 달리 React 엘리먼트는 일반 객체
- React DOM은 React 엘리먼트와 일치하도록 DOM을 업데이트
- 엘리먼트는 컴포넌트의 구성 요소
- **엘리먼트는 불변 객체, 생성 후에는 해당 엘리먼트 자식이나 속성 변경 불가**
-  엘리먼트는 특정 시점의 UI를 보여줌



### DOM에 엘리먼트 렌더링
```react
const element = <h1>Hello, world</h1>;
ReactDOM.render(element, document.getElementById('root'));
```



### 렌더링 된 엘리먼트 업데이트
-  엘리먼트 업데이트 하려면 새로운 엘리먼트를 생성하고 이를 `ReactDOM.render()`로 전달

```react
function tick() {
  const element = (
    <div>
      <h1>Hello, world!</h1>
      <h2>It is {new Date().toLocaleTimeString()}.</h2>
    </div>
  );
  ReactDOM.render(element, document.getElementById('root'));}

setInterval(tick, 1000);
```

- setInterval() 콜백을 이용해 ReactDOM.render()를 1000ms 간격으로 호출



### 변경된 부분만 업데이트
-  **React DOM은 해당 엘리먼트와 자식 엘리먼트를 이전 엘리먼트와 비교**
- **DOM을 원하는 상태로 만드는데 필요한 경우에만 DOM을 업데이트함**



## 4. Components & Props
- 개념: props라는 임의의 입력을 받은 후, 화면에 어떻게 표시되는지를 기술하는 React 엘리먼트를 반환



### 함수 컴포넌트와 클래스 컴포넌트
#### 함수 컴포넌트
> JS 함수 작성
```react
function Welcome(props) {
    return <h1>Hello, {props.name}</h1>;
}
```

- 해당 함수는 데이터를 가진 하나의 props 객체 인자를 받은 후 React 엘리먼트를 반환하므로 유효한 React 컴포넌트
- props: 속성을 나타내는 데이터
- 해당 컴포넌트는 JS함수이기 때문에 함수 컴포넌트라 함



#### 클래스 컴포넌트
```react
class Welcome extends React.Component {
	render() {
		return <h1>Hello, {props.name}</h1>;
	}
}
```



### 컴포넌트 렌더링
- React 엘리먼트는 사용자 정의 컴포넌트로도 나타낼 수 있음

- Vue 컴포넌트와 비슷, 차이점은 Vue는 template 단에서 html 형식으로 컴포넌트를 렌더링하지만 React는 JS 형식으로 나타낸다(변수에 할당)

- React가 사용자 정의 컴포넌트로 작성한 엘리먼트를발견하면 **JSX 속성과 자식을 해당 컴포넌트에 단일 객체로 전달**, 이 객체를 **props** 라고 함

- 컴포넌트 이름은 항상 대문자로 시작

  ```react
  function Welcome(props) {  
  	return <h1>Hello, {props.name}</h1>;
  }
  const element = <Welcome name="Sara" />;
  ReactDOM.render(
    element,
    document.getElementById('root')
  );
  ```

  

- 동작과정
	- `<Welcome name="Sara" />`엘리먼트로 `ReactDOM.render()` 호출
	- React는 `{name: 'Sara'}`를 props로 하여 Welcome 컴포넌트를 호출
	- Welcome 컴포넌트는 결과적으로 `<h1>Hello, Sara</h1>`엘리먼트를 반환
	- React DOM은  `<h1>Hello, Sara</h1>`  엘리먼트와 일치하도록 DOM을 효율적으로 업데이트
	
	

### 컴포넌트 합성
- 컴포넌트는 자신의 출력에 다른 컴포넌트 참조 가능

- 모든 세부 단계에서 동일한 추상 컴포넌트를 사용할 수 있음

- Ex) 버튼, 폼, 다이얼로그, 화면 등 => 컴포넌트로 표현

- Welcome을 여러번 렌더링하는 App 컴포넌트 예시

  ```react
  function Welcome(props) {
  	return <h1>Hello, {props.name}</h1>;
  }
  function App() {
    return (
      <div>
        <Welcome name="Sara" />      
        <Welcome name="Cahal" />      
        <Welcome name="Edite" />    
      </div>
    );
  }
  
  ReactDOM.render(
    <App />,
    document.getElementById('root')
  );
  ```

  

### 컴포넌트 추출
- 구성요소가 중첩된 컴포넌트 => 수정 및 재사용 어려움

  ```react
  function Comment(props) {
      return (
          <div className="Comment">
          <div className="UserInfo">
          <img className="Avatar"
             src={props.author.avatarUrl}
             alt={props.author.name}
          />
          <div className="UserInfo-name">
              {props.author.name}
          </div>
          </div>
          <div className="Comment-text">
            {props.text}
          </div>
          <div className="Comment-date">
            {formatDate(props.date)}
          </div>
        </div>
    );
  }
  ```

  

- Avatar 추출 => Comment 내에서 렌더링 된다는 것 알 필요 없어짐
  

  ```react
  function Avatar(props) {
      return (
          <img className="Avatar" src={props.user.avatarUrl} alt={props.user.name}/>
      );
  }
  ```

  

- UserInfo 추출

  ```react
  function UserInfo(props) {
      return (
          <div className="UserInfo">
              <Avatar user={props.user} />
              <div className="UserInfo-name>
                  {props.user.name}
              </div>
          </div>
      );
  }
  ```

  

- 단순해진 Comment

  ```react
  function Comment(props) {
  return (
  	<div className="Comment">
      <UserInfo user={props.author} />     
      <div className="Comment-text">
        {props.text}
      </div>
      <div className="Comment-date">
        {formatDate(props.date)}
      </div>
    </div>
    );
  }
  ```

  

### props는 읽기 전용
- 함수 컴포넌트나 클래스 컴포넌트 모드 컴포넌트의 자체 props를 수정해서는 안됨

- 순수 함수: 입력값을 바꾸려 하지 않고 항상 동일한 입력값에 대해 동일한 결과를 반환

  ```react
  function sum(a, b) {
  	return a + b;
  }
  ```

  

- 순수함수가 아닌 함수: 자신의 입력값을 변경

  ```react
  function withdraw(account, amount) {
  	account.total -= amout;
  }
  ```

  

- **모든 React 컴포넌트는 자신의 props를 다룰 때 반드시 순수 함수처럼 동작해야함**

- React 컴포넌트는 `state`를 통해 위 규칙을 위반하지 않고 사용자 액션, 네트워크 응답 및 다른 요소에 대한 응답으로 시간에 따라 자신의 출력값 변경 가능



## 5. State & Lifecycle
```react
function Clock(props) {
  return (
    <div>      
    <h1>Hello, world!</h1>      
    <h2>It is {props.date.toLocaleTimeString()} </h2>    
    </div>  
  );
}
function tick() {
  ReactDOM.render(
    <Clock date={new Date()} />,    document.getElementById('root')
  );
}
setInterval(tick, 1000);
```



- 위 예시에서는 이상적으로 한 번만 코드를 작성하고 `Clock`이 스스로 업데이트하지 못함 => `setInterval()`을 통해 주기적으로 호출되어짐

- 이상적인 코드 구현

  ```react
  ReactDOM.render(
  <Clock />,
  document.getElementById('root')
  );
  ```

  

- 위 예시를 구현하려면 `Clock` 컴포넌트에 `state`를 추가해야함

- `state`는 `props`와 유사하지만, 비공개이며 컴포넌트에 의해 완전히 제어됨



### 함수에서 클래스로 변환하기
- 다섯 단계로 위 예시 `Clock`과 같은 함수 컴포넌트를 클래스로 변환 가능
	- React.Component를 확장하는 동일한 이름의 ES6 class 생성
	- `render()` 라고 불리는 빈 메서드 추가
	- 함수의 내용을 `render()` 메서드 안으로 옮기기
	- `render()` 내용 안에 있는 `props`를 `this.props`로 변경
	- 남아있는 빈 함수 선언 삭제
	```react
	class Clock extends React.Component {
	render() {
		return (
			<div>
				<h1>Hello, world!</h1>
				<h2>It is {this.props.date.toLocaleTimeString()}.
				</h2>
			</div>
		);
		}
	}


- `Clock` 함수를 클래스로 변환
- `render`메서드는 업데이트가 발생할 때마다 호출되지만, 같은 DOM 노드로 `<Clock />`을 렌더링하는 경우 `Clock` 클래스의 단일 인스턴스만 사용
- 로컬 `state`와 생명주기 메서드와 같은 부가적인 기능을 사용할 수 있게 해줌



### 클래스에 로컬 State 추가하기
- `date`를 props에서 state로 이동 예시(3단계)
- 1. `render()` 메서드 안에 있는 `this.props.date`를 `this.state.date`로 변경

```react
class Clock extends React.Component {
	render() {
		return (
			<div>
				<h1>Hello, world!</h1>
				<h2>It is {this.state.date.toLocaleTimeString()}.
				</h2>
			</div>
		);
	}
}
```



- 2. 초기 `this.state`를 지정하는 class constructor를 추가
	- `constructor`
		- `constructor` 메서드는 class로 생성된 객체를 생성하고 초기화하기 위한 특수한 메서드
		- `constructor` 메서드는 클래스 안에 한 개만 존재할 수 있음
		- 여러 개 있을 경우 SyntaxError 발생
		- `constructor`는 부모 클래스의 `constructor`를 호출하기 위해 `super` 키워드를 사용할 수 있음
		```jsx
		class Clock extends React.Component {
		constructor(props) {
		super(props);
		this.state = {date: new Date()};
		}
		render() {
		return (
			<div>
		        <h1>Hello, world!</h1>
		        <h2>It is {this.state.date.toLocaleTimeString()}.
		        </h2>
		    </div>
		);
		}
		}

- 클래스 컴포넌트는 항상 `props`로 기본 constructor를 호출해야함

- 3. `<Clock />` 요소에서 `date` prop 삭제

    ```react
    ReactDOM.render(
    <Clock />,  
    document.getElementById('root')
    );
    ```

    

- 최종 결과

  ```react
  class Clock extends React.Component {
      constructor(props) {    
          super(props);    
          this.state = {date: new Date()};  
      }
  render() {
    return (
        <div>
        <h1>Hello, world!</h1>
        <h2>It is {this.state.date.toLocaleTimeString()}.
        </h2>      
        </div>
    );
  }
  }
  ReactDOM.render(
    <Clock />,  
    document.getElementById('root')
  );
  ```

  

  

### 생명주기 메서드를 클래스에 추가하기
> 많은 컴포넌트가 있는 애플리케이션에서 컴포넌트가 삭제될 때 해당 컴포넌트가 사용 중이던 리소스를 확보해야함

- `Clock`이 처음 DOM에 렌더링 될 때마다 타이머를 설정
- 이것을 React에서 Mounting 이라 함
- `Clock`에 의해 생성된 DOM이 삭제될 때마다 타이머를 해제하려고 함
- 컴포넌트 클래스에서 특별한 메서드를 선언하여 컴포넌트가 마운트 되거나 언마운트 될 때 일부 코드를 작동할 수 있음

  
#### 생명주기 메서드
- componentDidMount()
	- 컴포넌트 출력물이 DOM에 렌더링 된 후에 실행
	- 타이머 설정
	- Arrow Function ( => )
	- `this.props`가 React에 의해 스스로 설정되고 `this.state`가 특수한 의미가 있지만, 타이머 ID와 같이 데이터 흐름 안에 포함되지 않는 어떤 항목을 보관할 필요가 있다면 자유롭게 클래스에 수동으로 부가적인 필드 추가
	```jsx
	componentDidMount() {
  this.timerID = setInterval(      
  () => this.tick(),      
  1000    );  
	 }


- componentWillUnmount()

  ```react
  componentWillUnmount() {
    clearInterval(this.timerID);  }
  ```
  
  


- `Clock` 컴포넌트가 매초 작동하도록 하는 `tick()` 메서드 구현 => **컴포넌트 로컬 state 업데이트** 하기 위해 `this.setState()`를 사용

```react
tick() {    
	this.setState({      
	date: new Date()    
	});  
}
```




- 예시의 동작과정
	- `<Clock />`가  `ReactDOM.render()`로 전달되었을 때 React는  `Clock`  컴포넌트의 constructor를 호출합니다.  `Clock`이 현재 시각을 표시해야 하기 때문에 현재 시각이 포함된 객체로  `this.state`를 초기화합니다. 나중에 이 state를 업데이트할 것입니다.
	- React는  `Clock`  컴포넌트의  `render()`  메서드를 호출합니다. 이를 통해 React는 화면에 표시되어야 할 내용을 알게 됩니다. 그 다음 React는  `Clock`의 렌더링 출력값을 일치시키기 위해 DOM을 업데이트합니다.
	- `Clock`  출력값이 DOM에 삽입되면, React는  `componentDidMount()`  생명주기 메서드를 호출합니다. 그 안에서  `Clock`  컴포넌트는 매초 컴포넌트의  `tick()`  메서드를 호출하기 위한 타이머를 설정하도록 브라우저에 요청합니다.
	- 매초 브라우저가  `tick()`  메서드를 호출합니다. 그 안에서  `Clock`  컴포넌트는  `setState()`에 현재 시각을 포함하는 객체를 호출하면서 UI 업데이트를 진행합니다.  `setState()`  호출 덕분에 React는 state가 변경된 것을 인지하고 화면에 표시될 내용을 알아내기 위해  `render()`  메서드를 다시 호출합니다. 이 때  `render()`  메서드 안의  `this.state.date`가 달라지고 렌더링 출력값은 업데이트된 시각을 포함합니다. React는 이에 따라 DOM을 업데이트합니다.
	-  `Clock`  컴포넌트가 DOM으로부터 한 번이라도 삭제된 적이 있다면 React는 타이머를 멈추기 위해  `componentWillUnmount()`  생명주기 메서드를 호출합니다.
	
	


#### State 주의점
- 직접 State를 수정하지 말 것
	- `this.state`를 지정할 수 있는 유일한 공간은 **constructor**
	- 대신에 `setState()`를 사용
	```jsx
	// Wrong
	this.state.comment = 'Hello';
	// Correct
	this.setState({comment: 'Hello'});



- State 업데이트는 비동기적일 수 있음
	
	- React는 성능을 위해 여러 setState() 호출을 단일 업데이트로 한꺼번에 처리할 수도 있다.
	- `this.props`와 `this.state`가 비동기적으로 업데이트될 수 있기 때문에 다음 state를 계산할 때 해당 값에 의존X
	- Arrow Function (일반 함수도 가능)
	```jsx
	// Wrong
  this.setState({
	counter: this.state.counter + this.props.increment,
	});
	// Correct
	this.setState((state, props) => ({
	  counter: state.counter + props.increment
	}));
	
	
	// Correct
	this.setState(function(state, props) {
	  return {
	    counter: state.counter + props.increment
	  };
	});




- State 업데이트는 병합됨
	- `setState()` 호출할 때 React는 제공한 객체를 현재 state로 병합
	- 병합은 얕게 이루어짐
		- `this.setState({comments})`는 `this.state.posts`에 영향을 주진 않지만 `this.state.comments`는 완전히 대체
  	```jsx
  	 constructor(props) {
    super(props);
    this.state = {
      posts: [],      
  	  comments: []    
  	};
  	}
  	componentDidMount() {
  	  fetchPosts().then(response => {
  	    this.setState({
  	      posts: response.posts      });
  	  });
  	
  	  fetchComments().then(response => {
  	    this.setState({
  	      comments: response.comments      });
  	  });
  	}
  
  


#### 데이터는 아래로 흐름(단방향)
- state는 로컬 또는 캡슐화라 불림(**React의 state = Vue의 데이터**)

- state가 소유하고 설정한 컴포넌트 이외에는 어떠한 컴포넌트에도 접근할 수 없음

- 컴포넌트는 자신의 state를 자식 컴포넌트에 props로 전달할 수 있음

  ```react
  <FormattedDate date={this.state.date} />
  
  function FormattedDate(props) {
    return <h2>It is {props.date.toLocaleTimeString()}.</h2>;
  }
  ```

  

