# 0120 Function

## 함수

- 특정한 기능(function)을 하는 코드의 묶음

- 함수를 쓰는 이유

  - 높은 가독성: 짧아짐
  - 재사용성:
  - 유지보수: 코드의 기능별 분화

- 함수의 선언과 호출

  - 함수 선언은 `def`로 시작하여 `:`으로 끝나고, 다음은 `4spaces 들여쓰기`로 코드 블록을 만든다.
- 함수는 `매개변수(parameter)`를 넘겨줄 수도 있다.
  - 함수는 동작후에 `return`을 통해 결과값을 전달 할 수도 있다. (`return` 값이 없으면, `None`을 반환한다.)
- 함수는 호출을 `func()` / `func(val1, val2)`와 같이 한다.

```python
# Built-in 함수목록
dir(__builtin__)

# 아스키코드
# 문자 -> 숫자
ord('A')
>>> 65

# 숫자 -> 문자
chr(65)
>>> 'A'
```

```python
# 직사각형 넓이
def rectangle(w, h):
    return w * h, 2 * (w + h)

print(rectangle(30, 20))
print(rectangle(50, 70))
>>>
(600, 100)
(3500, 240)
```



## 함수의 Output

### 함수의 `return`

앞서 설명한 것과 마찬가지로 함수는 반환되는 값이 있으며, 이는 어떠한 종류(~~의 객체~~)라도 상관없습니다.

단, **오직 한 개의 객체**만 반환됩니다.

함수가 return 되거나 종료되면, 함수를 호출한 곳으로 돌아갑니다.

- 아무것도 리턴하지 않으면 None이 리턴된다.
- **오직 하나만 반환**
- 만약, return 없으면 => `None`
- 만약, 여러개를 반환하면 ,로 이어서 return => **하나의 `tuple`**

```python
# 함수 return 과 print 차이
def cube_return(n):  # 세제곱 함수
    result = n**3
    return result

def cube_print(n):
    result = n**3
    print(result)
    
# vs code에서는 출력값 없음 -> print하지 않아서 notebook 환경에서는 print아니더라도 마지막 줄 내용 보여줌
# 옆에 Out이 붙는다.
# return값이 있어 할당 가능
a = cube_return(2)
print(2 * a)
>>> 16

# return은 None
# 할당 불가
aa = cube_print(2)  # cube_print()함수의 return은 None이기 때문에 할당이 안됨, return 값 없으면 None을 반환
print(aa)
print(2 * aa)
>>>
8
None
```

```python
# sort vs sorted
my_list = [5, 1, 3, 2, 4]
print(my_list)
>>>
[5, 1, 3, 2, 4]

# sort => 원본을 바꿔버리고 return 값 없음 -> None
my_list = [5, 1, 3, 2, 4]
a = my_list.sort()
print(a, type(a))
print(my_list)
>>>
None <class 'NoneType'>
[1, 2, 3, 4, 5]

# sorted => 원본은 no touch, return으로 정렬된 리스트를 반환 (입력으로 튜플 넣어도 리턴은 리스트 타입)
my_list = [5, 1, 3, 2, 4]
b = sorted(my_list)
print(b, type(b))
print(my_list)
>>>
[1, 2, 3, 4, 5] <class 'list'>
[5, 1, 3, 2, 4]
```



## 함수의 Input

### 매개변수(parameter) & 인자(argument)

- 매개변수(parameter)
  - `x` 는 매개변수(parameter)
  - 입력을 받아 함수 내부에서 활용할 `변수`라고 생각하면 된다.
  - 함수의 정의 부분에서 볼 수 있다.

```python
def func(x):
	return x + 2
```



- 전달인자(argument)

  ```python
  func(2)
  ```

  - `2` 는 (전달)인자(argument)
  - 실제로 전달되는 `입력값`이라고 생각하면 된다.
  - 함수를 호출하는 부분에서 볼 수 있다.

- parameter와 argument 구분 필요



### 함수의 인자

함수는 입력값(input)으로 `인자(argument)`를 넘겨줄 수 있습니다



#### 위치 인자 (Positional Argument)

- 함수는 기본적으로 인자를 위치로 판단합니다.

```python
from math import pi
def cylinder(r, h):
    return r**2 * pi * h
    
print(cylinder(5,2))  # 순서 바꾸면 다른 값 반환
print(cylinder(2,5))
>>>
157.07963267948966
62.83185307179586
```



#### 기본 인자 값 (Default Argument Values)

- 함수가 호출될 때, 인자를 지정하지 않아도 기본 값을 설정할 수 있습니다
- ***주의\* 단, 기본 인자값(Default Argument Value)을 가지는 인자 다음에 기본 값이 없는 인자를 사용할 수는 없습니다.**

```python
# name이 없을 경우 name = '익명' (초기값 설정, 기본 인자)
def greeting(name = '익명'):  
    print(f'{name}, 안녕?')
    
print(greeting('길동'))
print(greeting())
>>>
길동, 안녕?
None
익명, 안녕?
None
```

```python
# 기본 인자 뒤에 기본 인자아닌 인자가 오면 SyntaxError
def my_sum(a = 0, b):
    return a + b

print(my_sum(5))
>>> SyntaxError

# 기본 인자는 마지막에
def my_sum(a, b = 0):
    return a + b

print(my_sum(5))
>>> 5
```



#### 키워드 인자 (Keyword Argument)

- 키워드 인자는 직접 변수의 이름으로 특정 인자를 전달할 수 있습니다.

- **단 아래와 같이 `키워드 인자`를 활용한 다음에 `위치 인자`를 활용할 수는 없습니다.** 
- 키워드 인자는 위치 인자 뒤에 와야합니다.

```python
def greeting(age, name = '익명'):
    print(f'안녕? 난 {name}, {age}살 이야')
greeting(name = '길동', age = 1000) 
# 모두 키워드 인자로 입력하면 순서 상관 없음
>>> 
안녕? 난 길동, 1000살 이야
```

```python
# 위치인자가 키워드 인자 뒤에 옴 => SyntaxError , 키워드 인자는 위치 인자 뒤에 와야함
greeting(age = 3000, '곰')
>>> SyntaxError
```



#### 가변 인자 리스트 (Arbitrary Argument Lists)

-  `print()`처럼 개수가 정해지지 않은 임의의 인자를 받기 위해서는 가변 인자 리스트`*args`를 활용합니다.
- 가변 인자 리스트는 `tuple` 형태로 처리가 되며, 매개변수에 `*`로 표현합니다.

```python
print('hi')
print('hi', 'hello')
print('hi', 'hello', '안녕')
>>>
hi
hi hello
hi hello 안녕
```

```python
def students(*args):  # *을 붙이면 인자를 가변적으로 받을 수 있고 tuple로 처리()
    print(args)
    print(type(args))
    return(args)  # *빼고 쓸 것 => tuple은 immutable해야하기 때문

students()  # 가변 인자에서는 0개도 가능
>>>
()
<class 'tuple'>
()

students('철수', '영희', '유리')
>>>
('철수', '영희', '유리')
<class 'tuple'>
('철수', '영희', '유리')
```

```python
def students(*args, prof):
    for student in args:
        print(student)
    print(f'존경하는 교수님 {prof}')
    
# 마지막이 prof 자동으로 처리? => Nope, 마지막인자가 prof인지 *args인자인지 모른다
students('희은', '태영', ' 탁희')
>>> TypeError

# 가변 이후 변수는 직접 키워드 인자로 활용하면 가능
students('희은', '태영', prof = '탁희')
>>> 
희은
태영
존경하는 교수님 탁희
```



#### 가변 키워드 인자 (Arbitrary Keyword Arguments)

- 정해지지 않은 키워드 인자들은 **`dict`** 형태로 처리가 되며, `**`로 표현합니다.
- 보통 `kwagrs`라는 이름을 사용하며, `**kwargs`를 통해 인자를 받아 처리할 수 있습니다.

```python
dict(name = '홍길동', age = '1000')
>>>
{'name': '홍길동', 'age': '1000'}
# 키워드 한글도 가능
```

```
# 주의사항
# 식별자는 숫자만으로는 이루어질 수가 없다.(키워드인자로 넘기면 함수 안에서 식별자로 쓰이기 때문)
dict(1 = '1', 2 = '2')
>>> SyntaxError

# 위의 경우 다음과 같이 사용해야 한다.
dict(((1, 1), (2, 1)))
>>>
{1: 1, 2: 1}
```

```python
def my_dict(**kwargs):
    print(kwargs)
    print(type(kwargs))
    return kwargs

my_dict(한국어='안녕', 영어='hi', 독일어='Guten Tag')
>>>
{'한국어': '안녕', '영어': 'hi', '독일어': 'Guten Tag'}
<class 'dict'>
{'한국어': '안녕', '영어': 'hi', '독일어': 'Guten Tag'}
```

```python
def my_func(*args, **kwargs):  # 혼용 가능, return은 튜플로 묶임
    
    return args, kwargs

my_func(1,2,3, name = 'abc', etc = '기타')
>>>
((1, 2, 3), {'name': 'abc', 'etc': '기타'})
```

- URL 생성기 (가변키워드 인자 사용)

```python
def my_url(**kwargs):
    url = 'https://api.go.kr?'
    print(kwargs.items())
    # kwargs : dictionary (인자를 **로 받으면 dictionary형으로 처리)
    # kwargs.items() : dict_items([(sidoname='서울'), (key='asdf')])
    
    # dictionary 반복문
    for name, value in kwargs.items():
        url += f'{name}={value}&'
    return url
    
my_url(sidoname = '서울', key = 'asdf')

>>>
dict_items([('sidoname', '서울'), ('key', 'asdf')])
'https://api.go.kr?sidoname=서울&key=asdf&'
```



## 함수와 스코프

- 함수는 코드 내부에 공간(scope)를 생성합니다. 함수로 생성된 공간은 `지역 스코프(local scope)`라고 불리며, 그 외의 공간인 `전역 스코프(global scope)`와 구분됩니다.

- **전역 스코프(`global scope`)**: 코드 어디에서든 참조할 수 있는 공간
- **지역 스코프(`local scope`)**: 함수가 만든 스코프로 함수 내부에서만 참조할 수 있는 공간

- **전역 변수(`global variable`)**: 전역 스코프에 정의된 변수
- **지역 변수(`local variable`)**: 로컬 스코프에 정의된 변수

```python
a = 10  # 전역 스코프에 정의된 전역 변수

def func(b):
    c = 20  # 지역 스코프에 정의된 지역 변수
    print('지역스코프입니다.')
    print(a)  # 10 => 전역 스코프에서 정의된 전역 변수이기 때문에 지역 스코프에서 불러올 수 있다.
    print(b)  # 5
    print(c)  # 20
    
func(5)
    
print('전역스코프입니다.')
print(a)  # 10
print(b)  # 에러 => b는 함수 안 지역 스코프에서 선언된 지역 변수이기 때문에 전역 스코프에서 불러올 수 없다. 
print(c)  # 에러 => c는 함수 안 지역 스코프에서 선언된 지역 변수이기 때문에 전역 스코프에서 불러올 수 없다. 
>>>
지역스코프입니다.
10
5
20
전역스코프입니다.
10
NameError
```



### 이름 검색 규칙

  `LEGB Rule` 이라고 부르며, 아래와 같은 순서로 이름을 찾아나갑니다.

- `L`ocal scope: 정의된 함수

- `E`nclosed scope: 상위 함수

- `G`lobal scope: 함수 밖의 변수 혹은 import된 모듈

- `B`uilt-in scope: 파이썬안에 내장되어 있는 함수 또는 속성

```python
# 함수 안에 함수 가능
a = 10  # Global
b = 20
def enclosed():
    a = 30  # local 함수 입장에서는 Enclosed
    def local():
        c = 40  # local
        print(a, b, c)  # a가 30 (L : 없음, E : 30)
    local()
    a = 50  # enclosed 함수 Local, local 함수 Enclosed
enclosed()
>>> 30 20 40
```

```python
# 전역변수 바꾸기
global_num = 3
def local_scope():
    # Local Scope
    global global_num  # global을 이용하여 적용할 수 있다.
    global_num = 5

local_scope()
print(global_num)
>>> 5
```



### 변수의 수명주기

- **빌트인 스코프`(built-in scope)`**: 파이썬이 실행된 이후부터 영원히 유지

- **전역 스코프`(global scope)`**: 모듈이 호출된 시점 이후 혹은 이름 선언된 이후부터 인터프리터가 끝날때 까지 유지

- **지역(함수) 스코프`(local scope)`**: 함수가 호출될 때 생성되고, 함수가 가 종료될 때까지 유지 (함수 내에서 처리되지 않는 예외를 일으킬 때 삭제됨)



## 재귀 함수 (Recursive Function)

> 함수 내부에서 자기 자신을 호출하는 함수

### 팩토리얼

```python
# 반복문를 이용한 팩토리얼 계산
def fact(n):
    result = 1
    while n > 1:
        result *= n
        n -= 1
    return result
    
fact(5)
>>> 120
```

```python
# 재귀함수를 이용한 팩토리얼 계산

def factorial(n):  # 함수 내부에서 함수 호출
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)
        
factorial(5)
>>> 120
```



### 피보나치 수열



### 반복문과 재귀 함수 차이

```python
# 재귀함수
import time

t0 = time.time()
fib(30)
t1 = time.time()

total = t1 - t0
print(total)

>>> 0.2693355083465576
```

```python
# 반복문
import time

t0 = time.time()
fib_loop(100000)
t1 = time.time()

total = t1 - t0
print(total)

>>>
0.14062118530273438
```

