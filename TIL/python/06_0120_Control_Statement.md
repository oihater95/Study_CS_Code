# 0120 Control Statement 제어문

## Conditional Statement 조건문

`if` 문은 반드시 **참/거짓을 판단할 수 있는 조건**과 함께 사용이 되어야한다.

### if 조건문

```python
if <조건식>:  # True일 경우 if 코드동작 / False의 경우 다음 블럭으로
	코드
elif <조건식>:  # True일 경우 코드 동작 / False면 넘어감
	코드
else:  # 나머지
	코드
```

```python
# 홀수/짝수 판별
if num % 2 == 0:
	print('짝수')
else:
    print('홀수')
    
=
if num % 2:  # num % 2 = 1 => if True:
    print('홀수')
else:
    print('짝수')
```



### Conditional Expression 조건표현식

- 조건 표현식은 일반적으로 조건에 따라 값을 정할 때 활용된다.
- **삼항 연산자(Ternary Operator)**라고 부르기도 한다.

```python
'''
우선 평가하고자 하는 expression을 먼저 쓴다 (ex: num > 0)
num > 0

expression 앞 뒤로 if와 else를 쓴다
if num > 0 else

if 왼쪽에는 if 만족 시 실행될 코드
else 오른쪽에는 else 만족 시 실행될 코드
print('양수') if num > 0 else print('음수')
'''
```

```python
# 절댓값 반환
num = int(input('숫자를 입력하세요 : '))

value = num if num >= 0 else -num
=

if num >= 0:
	value = num
else:
	value = -num
>>>
숫자를 입력하세요 : -3
3
```



## Loop Statement 반복문

### while 반복문

- `while` 문은 조건식이 참(`True`)인 경우 반복적으로 코드를 실행한다.

- **반드시 종료조건을 설정해야 한다.**

```python
while <조건식>:
    <코드 블럭>
```

```python
# 한 자리씩 출력
num = int(input())
while num > 0:
    print(num % 10)
    num //= 10
>>>
185
5
8
1
```



### for 반복문

- `for` 문은 시퀀스(string, tuple, list, range)나 다른 순회가능한 객체(iterable)의 요소들을 순회한다.

```python
for <임시변수> in <순회가능한데이터(iterable)>:
    <코드 블럭>
```

```python
for num in [1, 2, 3, 4, 5]:
    print(num)
print('끝')
print(num)  
>>>
1
2
3
4
5
끝
5
# python 환경에서는 num이 임시변수이지만 살아있음,  C++의 경우 null값
```



####  ### `enumerate()`

> enumerate(iterable, start=0)
>
> 열거 객체를 돌려줍니다. iterable은 시퀀스, 이터레이터 또는 이터레이션을 지원하는 다른 객체여야 합니다. enumerate()에 의해 반환된 이터레이터의 'next()' 메서드는 카운트(default=0 인 start부터)와 iterable을 이터레이션 해서 얻어지는 값을 포함하는 **튜플**을 반환합니다.

```python
# enumerate = index와 value를 tuple로 묶음
lunch = ['짜장면', '초밥', '피자', '햄버거']
for i in enumerate(lunch):
    print(i)
>>>
(0, '짜장면')
(1, '초밥')
(2, '피자')
(3, '햄버거')

for i, menu in enumerate(lunch):
    print(i, menu)
>>>
0 짜장면
1 초밥
2 피자
3 햄버거

list(enumerate(lunch))
>>>
[(0, '짜장면'), (1, '초밥'), (2, '피자'), (3, '햄버거')]
```

```python
classroom = ['Kim', 'Hong', 'Kang']
for i in enumerate(classroom, start = 1):
    print(i)
>>>
(1, 'Kim')
(2, 'Hong')
(3, 'Kang')
```

```python
classroom = ['Kim', 'Hong', 'Kang']
for i, menu in enumerate(classroom, start = 1):
    print(i, menu)
>>>
1 Kim
2 Hong
3 Kang
```



### 반복제어

#### break

- 반복문을 종료한다. (`for`나 `while`문에서 빠져나간다.)

```python
rice = ['보리', '보리', '보리', '쌀', '보리']
for i in rice:
    print(i)
    if i == '쌀':
        print('잡았다!')
        break
>>>
보리
보리
보리
쌀
잡았다!
```



#### continue

- `continue`문은 continue 이후의 코드를 수행하지 않고 *다음 요소부터 계속(continue)하여* 반복을 수행한다.

```python
ages = [10, 23, 8, 30, 25, 31]
for i in ages:
    if i < 20:
        continue
    else:
        print(i, '살은 성인입니다.')
>>> 23 살은 성인입니다.
30 살은 성인입니다.
25 살은 성인입니다.
31 살은 성인입니다.
```



#### else

- 끝까지 반복문을 실행한 이후에 실행된다.

- 반복에서 리스트의 소진이나 (`for` 의 경우) 조건이 거짓이 돼서 (`while` 의 경우) 종료할 때 실행된다.
- 하지만 반복문이 **`break` 문으로 종료될 때는 실행되지 않는다.** (즉, `break`를 통해 중간에 종료되지 않은 경우만 실행)

```python
# numbers 리스트에 4가 있을 경우 True를 출력하고, 없을 경우 False를 출력한다.
numbers = [1, 3, 7, 9]
for num in numbers:
    if num == 4:
        print(True)
        break
else:
    print(False)
>>>
False
```



#### pass

- 아무것도 하지 않는다.

- 문법적으로 문장이 필요하지만, 프로그램이 특별히 할 일이 없을 때 자리를 채우는 용도로 사용할 수 있다.

```python
# pass 와 continue 차이
numbers = [1, 2, 3, 4, 5, 6, 7]

# pass => 말 그대로 그냥 흘려보냄
for num in numbers:
    if num == 5:
        pass
    print(num)
>>>
1
2
3
4
5
6
7

# continue => 바로 다음 step으로 넘김
for num in numbers:
    if num == 5:
        continue
    print(num)
>>>
1
2
3
4
6
7
```

