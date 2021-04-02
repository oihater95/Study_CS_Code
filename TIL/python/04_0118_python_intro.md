# 0118 Python Python Intro

## PEP, Syntax

### 주석 (comment)

- 한 줄 주석은 `#`, 여러 줄은 `'''` 또는 `"""`
- 큰 따옴표`""` 보다는 작은 따옴표`''`를 사용



### 코드 라인

- string의 경우 `''`사이에 줄바꿈이 들어가면 에러 발생
- 줄 바꿈이 필요한 경우 `\n` 사용
- `[]`, `()`, `{}` 는 `\`없이 여러 줄로 사용 가능

```python
# List 이름은 복수형으로
# 마지막 요소 뒤에도 , 찍기 => 나중에 추가 시 빠뜨리지 않기 위해서
lunch_menus = [
    '짜장면',
    '짬뽕',
    '탕수육',
    '군만두',
    '물만두',
    '왕만두',
]
print(lunch_menus)
>>> ['짜장면', '짬뽕', '탕수육', '군만두', '물만두', '왕만두']
```



- PEP에 따르면 여러줄의 문자열은 아래와 같이 사용

```python
print('''hello
world''')
>>> hello
	world
```



## Variable 변수

> 변수는 박스 역할



### 할당 연산자 `=`

- 변수는 `=`을 통해 할당된다.
- 해당 데이터 타입을 확인하기 위해서는 `type()` 사용
- 해당 값의 메모리 주소를 확인하기 위해서는 `id()`사용

```python
dust = 60
print(dust, type(dust), id(dust))
>>> 60 <class 'int'> 140721078865424
```



- 같은 값을 동시에 할당하는 경우 오른쪽에서 왼쪽으로 넣는다고 생각

```python
x = y = 10
print(x, y)
>>> 10 10
```



- 다른 값을 동시에 할당도 가능

```python
# x, y = 1, 10 == (x, y) = (1, 10) 소괄호 생략되어 있는 것 (1:1 할당)
# 이 경우 (x, y) 튜플 형식으로 들어감
x, y = 1, 10
print(x, y)
>>> 1 10
```



- 변수 갯수와 값 갯수가 다른 경우 에러 발생

```
1) x, y, z = 1, 2
2) x, y = 1
3) x, y = 1, 2, 3

세 가지 모두 에러 발생
1) ValueError: not enough values to unpack (expected 3, got 2)
2) TypeError: cannot unpack non-iterable int object
(하나의 값으로 두개의 변수 할당 불가, 각각 하나씩 할당해야함)
3) ValueError: too many values to unpack (expected 2)
```



### swap

- 파이썬 외 언어에서 일반적인 방법, 임시 변수 생성

```python
  x = 10
  y = 100
  temp = x  # 임시 변수
  x = y
  y = temp
  print(x, y)
  >>> 100 10
```


- python에서 일반적인 방법

```py
x = 10
y = 100
x, y = y, x
print(x, y)
>>> 100 10
```



- 수식을 활용한 방법

```python
x = 10
y = 100
x = x + y
y = x - y
x = x - y
print(x, y)
>>> 100 10
```



### Identifiers 식별자

> 파이썬에서 식별자는 변수, 함수, 모듈, 클래스 등을 식별하는데 사용되는 이름
>
> - 식별자의 이름은 영문알파벳(대문자와 소문자), 밑줄(_), 숫자로 구성된다.
> - 첫 글자에 숫자가 올 수 없다.
> - 길이에 제한이 없다.
> - 대소문자(case)를 구별한다.
> - 아래의 키워드는 사용할 수 없다.

- 키워드

```python
import keyword
print(keyword.kwlist)
>>> ['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
```



- 키워드나 내장함수를 변수이름으로 사용하면 해당 키워드의 기능을 잃어버리기 때문에 사용하지 않는다

```python
'''
print은 이제 'hi'라는 값으로 인식되기 때문에 이전의 기능을 수행하지 못합니다.
keyword는 변수이름으로 설정 X
변수 이름 짓는 법: 숫자 먼저 올 수 없다
print에 string문자열이 덮어씌워져서 불러오는()는 사용할 수 없다. -> string은 call 불가
'''
print = 'hi'
print(5)
>>> TypeError: 'str' object is not callable
```



- 만약 사용한 경우 del 함수로 해당 키워드에 덮어씌워진 값을 삭제

```python
'''
덮어씌워졌던 'hi' 삭제되고 원래 내장함수 print랑 연결되어 출력 가능
del print를 한번 더하면 print 내장함수도 지워짐
''' 
del print
print(5)
>>> 5
```



## Data Type

### 숫자(Number) 타입

#### int (Integer, 정수)

> 모든 정수는 `int`로 표현됩니다.
>
> 파이썬 3.x 버전에서는 `long` 타입은 없고 모두 `int` 타입으로 표기 됩니다.
>
> 8진수 : `0o` / 2진수 : `0b` / 16진수: `0x` 로도 표현 가능합니다.

```python
num = 100
print(num, type(num))
>>> 100 <class 'int'>
```

```python
# 아무리 큰 수라도 python에서는 int, ** = 지수
b = 100**100
print(b, type(b))
>>> 100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 <class 'int'>
```



> 파이썬은 기존 C 계열 프로그래밍 언어와 다르게 임의 정밀도 산술(arbitrary-precision arithmetic)을 사용하기 때문에 정수 자료형(integer)에서 오버플로우가 없다.

- **오버플로우(overflow)**

  - 데이터 타입 별로 사용할 수 있는 메모리의 크기가 제한되어 있다.
  - 표현할 수 있는 수의 범위를 넘어가는 연산을 하게 되면, 기대했던 값이 출력되지 않는 현상, 즉 메모리가 차고 넘쳐 흐르는 현상

  

- **임의 정밀도 산술(arbitrary-precision arithmetic)**

  - 사용할 수 있는 메모리양이 정해져 있는 기존의 방식과 달리, 현재 남아있는 만큼의 가용 메모리를 모두 수 표현에 끌어다 쓸 수 있는 형태
  - 특정 값을 나타내는데 4바이트가 부족하다면 5바이트, 더 부족하면 6바이트까지 사용할 수 있게 유동적으로 운용

```python
import sys
max_int = sys.maxsize
# sys.maxsize 의 값은 2**63 - 1 => 64비트에서 부호비트를 뺀 63개의 최대치
print(max_int)
super_max = sys.maxsize * sys.maxsize
print(super_max)
>>> 9223372036854775807
85070591730234615847396907784232501249
```



- n진수

```python
binary_number = 0b10
octal_number = 0o10
decimal_number = 10
hexadecimal_number = 0x10  # 색표현 또는 메모리 주소 표현

print(f"""
2진수 : {binary_number}
8진수 : {octal_number}
10진수 : {decimal_number}
16진수 : {hexadecimal_number}
""")

>>> 
2진수 : 2
8진수 : 8
10진수 : 10
16진수 : 16
```



#### float (Floating point number, 부동소수점, 실수)

> 실수는 `float`로 표현됩니다.
>
> 다만, 실수를 컴퓨터가 표현하는 과정에서 부동소수점을 사용하며, 항상 같은 값으로 일치되지 않습니다. (floating point rounding error)
>
> 이는 컴퓨터가 2진수(비트)를 통해 숫자를 표현하는 과정에서 생기는 오류이며, 대부분의 경우는 중요하지 않으나 값을 같은지 비교하는 과정에서 문제가 발생할 수 있습니다.

```python
c = 3.5
print(c, type(c))
>>> 3.5 <class 'float'>
```

```python
# 컴퓨터식 지수 표현 방식
pi = 314e-2
print(pi, type(pi))
>>> 3.14 <class 'float'>
```



- 실수 연산

  > 실수의 경우 실제로 값을 처리하기 위해서는 조심할 필요가 있다.

```python
3.5 - 3.12
>>>
0.3799999999999999
# 원하는 연산 값은 0.38
```

```python
# 반올림 round(number, n) => 소수 n+1번째 자리에서 반올림
round(3.5 - 3.12, 2)
>>> 0.38
```

```python
3.15 - 3.12 == 3.8
>>> False
(3.5 - 3.12) == round(3.5 - 3.12, 2)
>>> False
```



> 처리방법

```python
a = 3.5 -3.12
b = 0.38
abs(a - b) <= 1e-10
>>> True
```

```python
# `epsilon` 은 부동소수점 연산에서 반올림을 함으로써 발생하는 오차 상환
import sys
abs(a - b) <= sys.float_info.epsilon
>>> True
```

```python
# 주로 사용
import math
math.isclose(a, b)
>>> True
```



#### complex (복소수)

> 각각 실수로 표현되는 실수부와 허수부를 가집니다.
>
> 복소수는 허수부를 `j`로 표현합니다.

```python
a = 3 - 4j
type(a)
>>> complex
print(a.real)
print(a.imag)
>>> 3.0
	-4.0
```

```python
complex('1+2j')
>>> (1+2j)
```

```python
# 문자열을 변환할 때, 문자열은 중앙의 + 또는 - 연산자 주위에 
# 공백을 포함해서는 안 됩니다. => 형변환 불가
complex('1 + 2j') # ValueError
```



### 글자(String) 타입

> 문자열은 Single quotes(`'`)나 Double quotes(`"`)을 활용하여 표현 가능하다.
>
> C나 Java와 달리 char형은 없다.

```python
# 문자열은 + 연산자로 이어붙이고, * 연산자로 반복시킬 수 있습니다. 변수화도 가능
'hi' * 10
>>> 'hihihihihihihihihihi'

'hi' + 'moon'
>>> 'himoon'

a = 'hi'
b = ', moon'
a + b
>>> 'hi, moon'
```



- **이스케이프 시퀀스**

| 예약문자 |    내용(의미)     |
| :------: | :---------------: |
|    \n    |      줄 바꿈      |
|    \t    |        탭         |
|    \r    |    캐리지리턴     |
|    \0    |     널(Null)      |
|    \\    |        `\`        |
|    \'    | 단일인용부호(`'`) |
|    \"    | 이중인용부호(`"`) |



> `print()` 함수를 한 번만 사용하여 다음 문장을 출력하시오.

"파일은 c:\Windows\Users\내문서\Python에 저장이 되었습니다."
나는 생각했다. 'cd를 써서 git bash로 들어가 봐야지.'

```python
print('\"파일은 C:\\Windows\\Users\\내문서\\Python에 저장이 되었습니다.\"\n 나는 생각했다. \'cd를 써서 git bash로 들어가 봐야지.\'')

>>>
"파일은 C:\Windows\Users\내문서\Python에 저장이 되었습니다."
 나는 생각했다. 'cd를 써서 git bash로 들어가 봐야지.'
```



- end 옵션 (default = `\n`)

```python
print('내용을 띄워서 출력하고 싶으면?', end='\t')
print('옆으로 띄워짐')
>>> 내용을 띄워서 출력하고 싶으면?	옆으로 띄워짐

print('개행 문자 말고도 가능합니다', end='!')
print('진짜로', end='!')
print('알고보면 print는 기본이 \\n', end='!')
>>> 개행 문자 말고도 가능합니다!진짜로!알고보면 print는 기본이 \n!

print('hi', end = '')  # 자동 줄바꿈 제거
print('hi!!')
>>> hihi!!
```



- **String Interpolation**

  - `%-formatting`
    - `%d` : 정수
    - `%f` : 실수
    - `%s` : 문자열

  ```python
  print('Hello, %s' % name) # string
  print('내 성적은 %d' % score) # int
  print('내 성적은 %f' % score) # float
  >>>
  Hello, Kim
  내 성적은 4
  내 성적은 4.500000
  ```

  

  - [`str.format()`](https://pyformat.info/)

  ```python
  print('Hello, {}. 내 성적은 {}'.format(name, score))
  >>> Hello, Kim. 내 성적은 4.5
  ```

  

  - [`f-strings`](https://www.python.org/dev/peps/pep-0498/) : 파이썬 3.6 이후 버전에서 지원

  ```python
  print(f'Hello, {name}. 내 성적은 {score}')
  >>> Hello, Kim. 내 성적은 4.5
  ```

  ```python
  # 연산도 가능
  pi = 3.141592
  f'원주율은 {pi:.4}. 반지름이 2일때 원의 넓이는 {pi*2*2}'
  >>> '원주율은 3.142. 반지름이 2일때 원의 넓이는 12.566368'
  ```

  ```python
  # 모듈 활용
  import datetime
  today = datetime.datetime.now()
  print(today)
  >>> 2021-01-18 13:46:56.048882
  
  f'오늘은 {today:%y}년 {today:%m}월 {today:%d}일 {today:%A}' 
  >>> '오늘은 21년 01월 18일 Monday'
  ```

  


### 참/거짓(Boolean) 타입

> 파이썬에는 `True`와 `False`로 이뤄진 `bool` 타입이 있습니다.
>
> 비교/논리 연산을 수행 등에서 활용됩니다.
>
> 다음은 `False`로 변환됩니다.
>
> 
> 0, 0.0, (), [], {}, '', None
> 

```python
bool(0.1)
>>> True

bool([])
>>> False

bool({})
>>> False

bool(0)
>>> False

bool(None)
>>> False

bool(1)
>>> True

bool('0')  # '0' 문자열 채워져 있으므로 True
>>> True

bool('')  # bool 비어 있으면 False
>>> False

'' in 'abcd'  # ''빈 문자열은 어느 문자열에도 속한다고 판단 => True
>>> True
```



- `**None** 타입

> 파이썬에서는 값이 없음을 표현하기 위해 `None` 타입이 존재합니다.

```python
print(type(None))
>>> <class 'NoneType'>
```

```python
a = ''  # 비어있지만 추후에 추가할 가능성 있음
a = None  # 아예 비워놓을 생각
print(a)
>>> None
```

### 형변환 (Type Conversion)

#### 암시적 형변환 (Implicit Type Conversion)

> 사용자가 의도하지 않았지만, 파이썬 내부적으로 자동으로 형변환 하는 경우입니다. 아래의 상황에서만 가능합니다.

- bool
- Numbers (int, float, complex)

```python
True + 5
>>> 6

int_number = 3
float_number = 5.0
complex_number = 3+5j

result = int_number + float_number
print(result, type(result))  
# int 보다 float이 더 넓은 범위라서 float으로 형변환 
>>> 8.0 <class 'float'>

result = int_number + complex_number
print(result, type(result))
>>> (6+5j) <class 'complex'>
```



- string <==> float, int 가능하지만 예외가 있다.

```python
int('3.5')
>>> ValueError: invalid literal for int() with base 10: '3.5'

'''
해당 경우는 '3.5'문자열을 int형으로 변환할 수 없어 생긴 에러
한 번에 여러 스텝을 뛰어넘어 에러 발생
int(float('3.5'))로 쓰면 에러 발생하지 않음
'''
```



#### 명시적 형변환

> 위의 상황을 제외하고는 모두 명시적으로 형 변환을 해주어야합니다.
>
> - string -> intger : 형식에 맞는 숫자만 가능
> - integer -> string : 모두 가능
>
> 암시적 형변환이 되는 모든 경우도 명시적으로 형변환이 가능합니다.
>
> - `int()` : string, float를 int로 변환
> - `float()` : string, int를 float로 변환
> - `str()` : int, float, list, tuple, dictionary를 문자열로 변환



- 문자열 특정 숫자 형식 => 그 형식으로 가능
- 모든 문자, 숫자는 문자열 형식으로 변환 가능
- float => int 처럼 큰 범위에서 작은 범위로 변환 시 버리는 부분 발생

```py
1 + '등'  # 암시적 형변환 불가, 명시적 형변환 필요
>>> TypeError: unsupported operand type(s) for +: 'int' and 'str'

str(1) + '등'
>>> '1등'
```



## Operator 연산자

### **산술 연산자**

| 연산자 |   내용   |
| :----: | :------: |
|   +    |   덧셈   |
|   -    |   뺄셈   |
|   *    |   곱셈   |
|   /    |  나눗셈  |
|   //   |    몫    |
|   %    |  나머지  |
|   **   | 거듭제곱 |

>  나눗셈 (`/`) 은 항상 float를 돌려준다.
>
> 정수 나눗셈 으로 (소수부 없이) 정수 결과를 얻으려면 `//` 연산자를 사용한다.



### **비교 연산자**

> `=` 은 항상 뒤에

| 연산자 |                내용                |
| :----: | :--------------------------------: |
|   <    |                미만                |
|   <=   |                이하                |
|   >    |                초과                |
|   >=   |                이상                |
|   ==   |                같음                |
|   !=   |             같지 않음              |
|   is   |  객체 아이덴티티 (같은 객체인지)   |
| is not | 부정된 객체 아이덴티티 (다른 객체) |



> 문자열 비교 (대소문자 구분)

```python
'hi' == 'Hi' 
>>> False
```



### **논리 연산자**

|  연산자   |             내용             |
| :-------: | :--------------------------: |
| a `and` b | a와 b 모두 True일 때만 True  |
| a `or` b  | a와 b중 하나라도 True면 True |
|  `not` a  | True -> False, False -> True |

- `and`

```python
print(True and True)
print(True and False)
print(False and True)
print(False and False)
>>>
True
False
False
False
```



- `or`

```python
print(True or True)
print(True or False)
print(False or True)
print(False or False)
>>>
True
True
True
False
```



- `not`

```python
print(not True)
print(not 0)
print(not 1)
>>>
False
True
False
```



- **단축평가**

  > - 첫 번째 값이 확실할 때, 두 번째 값은 확인 하지 않음
  > - 조건문에서 뒷 부분을 판단하지 않아도 되기 때문에 속도 향상
  > - 연산 결과는 어디까지 봤는지

  ```python
  # 첫번째 값 'a' 확인(값 존재) => True => 'b'값도 확인, 
  #'a'가 True라고 해서 'a'를 True로 바꾸는건 아니다.
  
  'a' and 'b'
  >> 'b'
  ```

  ```python
  # 'c'까지 True, ''를 읽었을 때 False라 'd'까지 확인할 필요없음 
  # => 연산 결과: '' => ''까지만 읽었기 때문
  
  'a' and 'b' and 'c' and '' and 'd'
  >>> ''
  ```

  ```python
  # 'a'값을 읽음 (값 존재) => True 이기 때문에 뒤는 읽지 않음
  # => 'a'까지만 확인했기 때문에 'a'를 출력
  'a' or 'b'
  >>> 'a'
  ```

  ```python
  vowels = 'aeiou'
  
  ('a' and 'b') in vowels  # == 'b' in vowels
  >>> False
  
  ('b' and 'a') in vowels  # == 'a' in vowels
  >>> True
  
  ('a' or 'b') in vowels  # == 'a' in vowels
  >>> True
  
  ('b' or 'a') in vowels  # == 'b' in vowels
  >>> False
  
  ('b' and '') in vowels  # '' 빈 문자열은 어느 문자열에도 속한다고 판단
  >>> True
  ```

  

  > `and`

  - `and` 는 둘 다 True일 경우만 True이기 때문에 첫번째 값이 True라도 두번째 값을 확인해야 하기 때문에 'b'가 반환된다.
  - 앞이 True이면 뒤 쪽도 확인
  - 앞이 False이면 뒤는 확인 안하고 False

  

  > `or`

  - `or` 는 하나만 True라도 True이기 때문에 True를 만나면 해당 값을 바로 반환한다.
  - 앞이 True이면 뒤 쪽 확인 안하고 True
  - 앞이 False이면 뒤 쪽도 확인



- 복합 연산자

  > python은 C++, Java와 달리 ++, -- 연산자는 없다.

  | 연산자  |    내용    |
  | :-----: | :--------: |
  | a += b  | a = a + b  |
  | a -= b  | a = a - b  |
  | a *= b  | a = a * b  |
  | a /= b  | a = a / b  |
  | a //= b | a = a // b |
  | a %= b  | a = a % b  |
  | a **= b | a = a ** b |

  

### 기타 주요 연산자

#### Concatenation

- 숫자가 아닌 자료형은 `+` 연산자를 통해 합칠 수 있습니다.

```python
'abc' + 'efg'
>>> 'abcefg'

[1, 2, 3] + [4, 5, 6]
>>> [1, 2, 3, 4, 5, 6]
```



#### Containment Test

- `in` 연산자를 통해 요소가 속해있는지 여부를 확인할 수 있습니다.

```python
5 in range(1, 5)
>>> False

# range(1, 5) => 1, 2, 3, 4
```



#### Identity

- `is` 연산자를 통해 동일한 object인지 확인할 수 있습니다. 

- python에서 -5 부터 256 까지의 id는 동일합니다.

```python
a = []
b = []

# a == b는 값 비교
# a is b는 객체 비교

# 값은 같지만 주소는 다름(실제 object는 다르다, 메모리상 위치가 다르다)
print(a == b, a is b)  
>>> True False

print(id(a), id(b))
>>>
2176614993472 2176615894592
```

```python
# 의도적으로 공백없는 알파벳 문자열은 같게 본다. (주소 같음, 메모리상 위치 같다)
a = 'hi'
b = 'hi'
print(a is b)
print(id(a), id(b))

>>> True
2176575806512 2176575806512
```

```python
# 특수문자가 들어가면 다르게 본다. (주소가 달라짐, 메모리상 위치 다름)
a = 'hi!'
b = 'hi!'
print(a is b)
print(id(a), id(b))

>>> False
2176614910576 2176614910192
```

```python
# 의도적으로 특정 범위의 숫자도 같게 본다. 
# (Object Interning, 빠른 searching을 위해 의도적으로 하는 것)
a = 1
b = 1
print(a is b)
print(id(a), id(b))

>>> True
140721078863536 140721078863536
```

```python
# 257 이상의 숫자는 id 다릅니다.
# 특정 범위: -5 ~ 256

a = 257
b = 257
print(a is b)
print(id(a), id(b))

>>> False
2176616072528 2176616072400
```



#### Indexing / Slicing

- `[]`를 통한 값을 접근하고, `[:]`을 통해 리스트를 슬라이싱할 수 있습니다.

```python
# indexing -> 0부터 시작
a = 'index'
a[0]
>>> 'i'
```

```python
# slicing
a[0:2]  # 0이상 2미만 (0과 1인덱스만)
>> 'in'
```



#### 연산자 우선순위

1. `()`을 통한 grouping
2. Slicing
3. Indexing
4. 제곱연산자 `**`
5. 단항연산자 `+`, `-` (음수/양수 부호)
6. 산술연산자 `*`, `/`, `%`
7. 산술연산자 `+`, `-`
8. 비교연산자, `in`, `is`
9. `not`
10. `and`
11. `or`



#### Expression 표현식 & Statement 문장

##### 표현식 Expression

>  표현식 => `evaluate` => 값

- 하나의 값(value)으로 환원(reduce)될 수 있는 문장
- `식별자`, `값`(리터럴), `연산자`로 구성됩니다.
- 표현식을 만드는 문법(syntax)은 일반적인 (중위표기) 수식의 규칙과 유사합니다.

```python
('a' and 'b') in vowels  # ('a' and 'b') 는 표현식
```

```python
# 하나의 값(value)도 표현식(expression)이 될 수 있습니다.
'hello'
```

```python
'''
표현식은 하나의 값으로 평가(evaluate)될 수 있어야 합니다. 
그러면 할당문(assignment statement)은 표현식일까요?
'''
# 연산자 표현식이다
radius = 10
```

```python
# 식별자가 값이 할당되어 있는 경우 수식의 일부가 될 수 있습니다.
3.14 * (radius - 5) ** 2
```

```python
'''
표현식을 만드는 문법(syntax)은 일반적인 (중위표기) 수식의 규칙과 유사합니다. 아래와 같은 문장은 표현식이 될 수 없습니다.
''' 
4 + 
```



##### 문장 Statement

> 파이썬이 실행 가능한 최소한의 코드 단위 (a syntatic unit of programming)

```python
# 하나의 값(value)도 문장이 될 수 있습니다.
'state'
```

```python
# 표현식(expression)도 문장이 될 수 있습니다.
5 * 21 - 4 
```

```python
# 실행 가능(executable)해야 하기 때문에 아래의 코드는 문장이 될 수 없습니다.
name = '
```



> 문장과 표현식의 관계

![image-20210119213853800](04_0118_intro_container.assets/image-20210119213853800.png)

## Summary

![image-20210119214104829](04_0118_intro_container.assets/image-20210119214104829.png)