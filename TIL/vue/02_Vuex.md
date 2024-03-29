# Vuex

- 상태 관리 패턴 + 라이브러리 관리
- 상태를 전역저장소로 관리할 수 있도록 지원하는 라이브러리
  - state가 예측 가능한 방식으로만 변경될 수 있도록 보장하는 규칙 설정
  - 애플리케이션의 모든 컴포넌트에 대한 **중앙 집중식 저장소** 역할
- 공유된 상태 관리 처리하는데 유용하지만 시작하는 비용 큼
  - 앱이 단순하다면 Vuex 안쓰는게 더 효율적, 그러나 중대형 규모의 SPA를 구축하는 경우 Vuex는 자연스러운 선택



## State

- 상태는 data이며, 해당 애플리케이션의 핵심이 되는 요소
- 각 컴포넌트에서 관리
  - .html의 경우 new Vue({})
  - SFC에서는 .vue에 해당
- DOM은 data(state)에 반응하여 DOM을 렌더링



## Pass props & Emit event

![image-20210512092041062](02_Vuex.assets/image-20210512092041062.png)

- 각 컴포넌트는 독립적으로 데이터를 관리
- 데이터는 단방향 흐름, 부모 => 자식 간의 전달만 가능하며 반대의 경우 이벤트를 통해 전달
- 장점: 데이터의 흐름을 직관적으로 파악 가능
- 단점: 컴포넌트 중첩이 깊어지는 경우 동위 관계의 컴포넌트로의 데이터 전달 불편(위로 올려서 내려보내야함)
- In Vuex
  - 중앙 저장소에서 state를 모아놓고 관리
  - 규모가 큰(컴포넌트 중첩이 깊은) 프로젝트에 편리
  - 각 컴포넌트에서는 중앙 집중 저장소의 state만 신경쓰면 됨
  - 이를 공유하는 컴포넌트는 알아서 동기화



## 단방향 데이터 흐름

<img src="02_Vuex.assets/image-20210512092151658.png" alt="image-20210512092151658" style="zoom: 80%;" />

- 상태(state)는 앱을 작동하는 원본 소스 (data)
- 뷰(view)는 상태의 선언적 매핑
- 액션(action)은 뷰에서 사용자 입력에 대해 반응적으로 상태를 바꾸는 방법(methods)
- 단점
  - 공통의 상태를 공유하는 여러 컴포넌트가 있는 경우 빠르게 복잡해짐
  - 예시: 지나치게 중첩된 컴포넌트를 통과하는 props



## 상태 관리 패턴

- 컴포넌트의 공유된 상태를 추출, 전역에서 관리
- 컴포넌트는 커다란 뷰가 되며 모든 컴포넌트는 트리에 상관없이 상태에 액세스 하거나 동작을 트리거함
- 상태 관리 및 특정 규칙 적용과 관련된 개념을 정의하고 분리 => 코드의 구조와 유지 관리 기능 향상



## Vuex 구성 요소

![image-20210512092522972](02_Vuex.assets/image-20210512092522972.png)

- State
- Actions
- Mutations
- Getters
- 4가지가 store 역할



### State

- **중앙에서 관리하는 모든 상태 정보**(**data**)
- **Mutations에 정의된 메서드에 의해 변경**
- 여러 컴포넌트 내부에 있는 특정 state를 중앙에서 관리
  - 이전 방식은 state를 찾기 위해 각 컴포넌트를 직접 확인
  - Vuex를 활용하는 방식은 Vuex Store에서 컴포넌트에서 사용하는 state를 한 눈에 파악 가능
- state가 변화하면 해당 **state를 공유하는 컴포넌트의 DOM은 알아서 렌더링**
- 컴포넌트는 Vuex Store에서 state 정보를 가져와 사용
- **dispatch()**를 사용하여 Actions 내부의 메서드를 호출 
  - Component가 dispatch()로 Actions 호출



### Actions

- 컴포넌트에서 **dispatch()** 메서드에 의해 호출
- Backend API와 통신하며 **Data Fetching 등의 작업 수행**
  - **동기적인 작업 뿐만 아니라 비동기적인 작업을 포함 가능**
- 항상 **context**가 인자로 넘어옴
  - store.js 파일 내에 있는 모든 요소에 접근해서 속성 접근 & 메서드 호출이 가능
  - 단, **state를 직접 변경하지 않음**(가능은 함)
  - **mutations에 정의된 메서드를 호출해서 변경**
- state는 오로지 mutations 메서드를 통해서만 조작
  - 명확한 역할 분담을 통해 서비스 규모가 커져도 state를 올바르게 관리하기 위함

- mutations에 정의된 메서드를 **commit()** 메서드로 호출

  

### Mutations

- Actions에서 **commit()** **메서드에 의해 호출**
- **state를 변경하는 로직**
- 비동기적으로 동작하면 state가 변화하는 시점이 달라질 수 있기 때문에 **동기적인 코드만 작성**
- mutations에 정의하는 **메서드의 첫번째 인자로 state가 넘어옴**



### Getters

- state를 변경하지 않고 활용하여 계산을 수행 (**computed와 유사**)
  - 실제 계산된 값을 사용하는 것처럼 getters는 **저장소의 상태(state)를 기준으로 계산**
  - 예시: state에 todo list의 해야할 일 목록의 경우 todo가 완료된 목록만 필터링해서 보여줘야 하는 경우
    - 리스트를 필터링(계산)해서 보여준 것, state가 바뀐 것은 아님
  - getters에서 completed의 값이 true인 요소가 필터링해서 계산된 값을 담아 놓을 수 있음
- **getters 자체가 state 자체를 변경하지 않음** (**실제 상태를 변경하지 않음**)
  - state를 **특정한 조건에 따라 구분(계산)만**
  - 계산된 값을 가져옴



### Modules

- store 자체가 커져 모듈화 할 때 사용



## vscode에서 시작 시

- `vue add vuex`

- 컴포넌트에서 `dispatch`를 활용해 actions 호출
- action에 정의된 메서드는 `commit`을 활용해 mutations를 호출
- mutations에 정의된 메서드는 `state`를 조작



### mapState

- computed와 state 매핑
- 객체 전개 연산자

```vue
<script>
import { mapState } from 'vuex'
```

```vue
<script>
  computed: {  // 호출해서 사용 X, 계산된 값만 사용하기 때문에 return 필수
    todos: function() {
      return this.$store.state.todos
    }
  }
  
      
      
</script>
```





### mapGetters

- computed와 getters 매핑



### mapActions

- computed와 actions 매핑



## Example

> Todolist

- Vuex 사용한다고 해서 props를 안쓰는건 아니다
- Vuex 사용한다고 해서 모든 data를 state에 쓰는건 아니다 => 한 컴포넌트에서만 쓰고 처리하는거면 해당 컴포넌트의 data에 씀



### 구조

- App: 최상단 컴포넌트
  - TodoForm: Todo 입력 (App의 하위 컴포넌트)
  - TodoList: Todo 목록 출력 (App의 하위 컴포넌트)
    - TodoListItem: TodoList 개별 요소 (TodoList의 하위 컴포넌트)



### store

- **index.js**에 **state, mutations, actions, getters, modules** 모두 있음
- devtools에서 Ctrl+2 Base State에서 state 확인 가능
- state
  - todos 데이터(배열)
- mutations
  - state 변경
  - actions의 commit에 의해 호출됨
  - 첫번째 인자로 항상 state받음
  - methods처럼 작성 but 대문자로 써서 methods와 구분하여 헷갈리지 않게함(권장사항)
  - this안쓰고 state바로 접근 가능(store내에서는 가능)
- actions
  - context를 인자로 받음
  - context안에 commit 있음 => `context.commit('mutations의 함수', payload)`로 mutations 호출
- getters
  - computed와 유사
  - 첫번째 인자는 state => 상태값을 기준으로 계산하기 때문에
  - 완료된 todo 개수, 진행중인 todo 개수 => todo 변경 사항이 없다면 미리 계산해두는 게 나음



### Flow

- 컴포넌트에서 `dispatch`를 활용해 `actions`를 호출
- `actions`에 정의된 메서드는 `commit`을 활용해 `mutations`를 호출
- `mutations`에 정의된 메서드는 `state`를 조작한다.



### TodoList



### 새로고침해도 데이터 없어지지 않게하기

- createdPersistedState => 브라우저의 로컬스토리지에 저장

- 설치

```bash
$ npm install --save vuex-persistedstate
```



- store index.js
```vue
import Vue from 'vue'
import Vuex from 'vuex'
import createdPersistedState from 'vuex-persistedstate'

Vue.use(Vuex)

export default new Vuex.Store({
  plugins: [
    createdPersistedState(),
  ],
  state: {
    todos: [],
  }, ...
```

