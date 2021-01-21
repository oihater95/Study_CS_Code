# Error_Exception

## Error

### Syntax Error 문법에러

> 문법 에러가 있는 프로그램은 실행되지 않는다.

```python
if True:
    print('참')
else
    print('거짓')
# SyntaxError = 문법 오류
>>>
 File "<ipython-input-1-04c4e0453d50>", line 3
    else
        ^
SyntaxError: invalid syntax
```

```python
print('hi)
>>>
File "<ipython-input-2-8878a92e9096>", line 1
    print('hi)
              ^
SyntaxError: EOL while scanning string literal
```



### Exception 예외

> 실행 도중 예상하지 못한 상황(exception)을 맞이하면, 프로그램 실행을 멈춤

- 문법적으로는 옳지만, 실행시 발생하는 에러

- *아래 제시된 모든 에러는 `Exception`을 상속받아 이뤄진다.*



- `ZeroDivisionError`

```python
# 0으로 나눌수는 없습니다.
10 * (1/0)
>>>
ZeroDivisionError: division by zero
```



- `NameError`

```python
# 지역 혹은 전역 이름 공간내에서 유효하지 않는 이름
# 즉 정의되지 않은 변수를 호출 하였을 경우
print(abc)
>>>
NameError: name 'abc' is not defined
```



- `TypeError`

```python
# 자료형에 대한 타입 자체가 잘못 되었을 경우
# 지원하지 않는 연산(int + str)
'''
함수 호출과정에서도 발생 
필수 argument 누락
argument 개수 다름
'''
1 + '1'
>>>
TypeError: unsupported operand type(s) for +: 'int' and 'str'
```



- `ValueError`

```python
# 자료형에 대한 타입은 올바르나 값이 적절하지 않는 경우
int('3.5')
>>>
ValueError: invalid literal for int() with base 10: '3.5'
```



- `IndexError`

```python
# 존재하지 않는 index로 조회할 경우
empty_list = []
empty_list[1]
>>>
IndexError: list index out of range
```



- `KeyError`

```python
# 딕셔너리에서 Key가 없는 경우 
songs = {'sia': 'candy cane lane'}
songs['queen']
>>>
KeyError: 'queen'
```



- ModuleNotFoundError

```python
# 모듈을 찾을 수 없는 경우
import reque
>>>
ModuleNotFoundError: No module named 'reque'
```



- `ImportError`

```python
# 모듈을 찾았으나 가져오는 과정에서 실패하는 경우 (존재하지 않는 클래스/함수 호출)
from random import sampl
>>>
ImportError: cannot import name 'sampl' from 'random' (c:\users\oihater\appdata\local\programs\python\python38\lib\random.py)

```



- `KeyboardInterrupt`

```python
# 주피터 노트북에서는 정지 버튼이지만, 실제로 우리가 돌릴 때는 ctrl+c를 통해 종료하였을 때 발생한다.
while True:
    continue
>>>
KeyboardInterrupt: 
```





## Exception Handling 예외 처리

### try-except

- `try` 아래의 코드블럭(code block)이 실행된다.
- 예외가 발생되지 않으면, **`except`없이 실행이 종료 된다.**
- 예외가 발생하면, **남은 부분을 수행하지 않고**, `except`가 실행된다.

```python
try:
    <코드 블럭 1>
except (예외):
    <코드 블럭 2>
```

```python
try: 
    num = input('값을 입력하시오 : ')
    print(int(num))
except ValueError:  # 에러를 특정할 수 있음
    print('숫자를 입력하라니까!!')
    
    
try:
    empty_list = []
    print(empty_list[-1])
except IndexError as err:  # 메세지 설정 가능
    print(f'{err}, 오류가 발생했습니다.')
```

```python
# 복수의 예외 처리
try:
    <코드 블럭 1>
except 예외1:
    <코드 블럭 2>
except 예외2:
    <코드 블럭 3>
```



### else

- 에러가 발생하지 않는 경우 수행되는 문장은 `else`를 이용한다.
- 모든 except 절 뒤에와야 한다.
- try 절이 예외를 일으키지 않을 때 실행되어야만 하는 코드에 적절하다.

```python
try:
    <코드 블럭 1>
except 예외:
    <코드 블럭 2>
else:
    <코드 블럭 3>
```



### finally

- 반드시 수행해야하는 문장은 `finally`를 활용한다.
- 즉, 모든 상황에 실행되어야만 하는 코드를 정의하는데 활용한다.
- 예외의 발생 여부과 관계없이 try 문을 떠날 때 항상 실행한다.

```python
try:
    <코드 블럭 1>
except 예외:
    <코드 블럭 2>
finally:
    <코드 블럭 3>
```



### Exception Raising 예외 발생 시키기

#### raise

- `raise`를 통해 예외를 강제로 발생시킬 수 있습니다.

```python
raise <에러>('메시지')
```

```python
raise ZeroDivisionError('0으로 나누지마라')
>>> ZeroDivisionError: 0으로 나누지마라
```



#### assert

- 보통 **상태를 검증하는데 사용**되며 무조건 `AssertionError`가 발생한다.

```python
assert Boolean expression, error message

assert len([1, 2]) == 1, '길이가 1이 아닙니다.'
>>>
AssertionError: 길이가 1이 아닙니다
```



## Summary

```python
try:
    실행할 코드
except:
    예외가 발생했을 때 처리하는 코드
else:
    예외가 발생하지 않았을 때 실행할 코드
finally:
    예외 발생 여부와 상관없이 항상 실행할 코드
    
raise <에러>('메시지')

assert Boolean expression, error message
```

