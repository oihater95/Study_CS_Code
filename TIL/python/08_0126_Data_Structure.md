# Data Structure

## String

> **변경할 수 없고(immutable), 순서가 있고(ordered), 순회 가능한(iterable)**
>
> immutable하다해서 return 없는 것은 아님

```python
# immutable => 바꾸려면 새로 할당해야함
h = 'hi'
h[0] = 'H'
>>>
TypeError: 'str' object does not support item assignment
```

```python
# iterabale
for char in h:
    print(char)
>>>
h
i
```



### 조회/탐색

- `.find(x)`
  - x의 **첫 번째 위치**를 반환합니다. 없으면,  **-1**을 반환

```python
a = 'apple'
a.find('a')
>>> 0

a.find('f')
>>> -1
```



- `.index(x)`
  - x의 **첫번째 위치**를 반환합니다. **없으면, 오류**가 발생

```python
a = 'apple'
a.index('p')
>>> 1

a.index('f')
>>> ValueError: substring not found
```



### 값 변경

- `.replace(old, new[, count])`
  - 바꿀 대상 글자를 새로운 글자로 바꿔서 **반환**
  - count를 지정하면 해당 갯수만큼만 시행 (default = 해당 문자 전부)
  - **원본은 그대로**

```python
z = 'zoo!yoyo!'
z.replace('o', '')  # 모든 o -> ''
>>> 'z!yy!'

z.replace('o', '', 2)  # 앞에 두 개의 o만 -> ''
>>> 'z!yoyo!'

print(z)  # 원본 그대로
>>> zoo!yoyo!
```



- `.strip([chars])`
  - 특정한 문자들을 지정하면, 양쪽을 제거하거나 왼쪽을 제거하거나(lstrip), 오른쪽을 제거(rstrip).
  - 지정하지 않으면 공백을 제거

```python
oh = '    oh!\n'
print(oh)
>>> '    oh!\n'

oh.strip()  # 양쪽 공백 제거
>>>     oh!

oh.lstrip()  # 왼쪽 공백 제거
>>> 'oh!'

oh.rstrip()  # 오른쪽 공백 제거
>>> '    oh!'

print(oh)  # 원본 그대로
>>> '    oh!\n'
```



- `.split()`
  - 문자열을 특정한 단위로 나누어 **리스트로 반환**

```python
csv = '1,홍길동,01012344567'
print(csv.split(','), type(csv.split(',')))
>>> ['1', '홍길동', '01012344567'] <class 'list'>

numbers = '1 5 6'
numbers.split()  # default는 공백을 기준으로 분리
>>> ['1', '5', '6']

x = '56487'
print(list(x))  # 붙어있는 경우에는 list로 쪼개기
>>> ['5', '6', '4', '8', '7']

x = '56489'
print(x.split(), type(x.split()))  # split은 붙어있는 경우에 불가
>>> ['56489'] <class 'list'>
```



- `'separator'.join(iterable)`
  - 특정한 문자열로 만들어 반환
  - 반복가능한(iterable) 컨테이너의 요소들을 separator를 구분자로 합쳐(`join()`) **문자열로 반환**

```python
word = '배고파'
words = ['안녕', 'hello']
print('!'.join(word), type('!'.join(word)))
>>> 배!고!파 <class 'str'>
```



### 문자 변형

- `.capitalize()`, `.title()`, `.upper()`, `.lower()`, `swapcase()`
  - `.capitalize()` : 앞글자를 대문자로 만들어 반환
  - `.title()` : 어포스트로피(')나 공백 이후를 대문자로 만들어 반환
  - `.upper()` : 모두 대문자로 만들어 반환
  - `.lower()` : 모두 소문자로 만들어 반환
  - `swapcase()` : 대 <-> 소문자로 변경하여 반환

```python
a = 'hI! Everyone, I\'m kim'

# 앞글자는 대문자 나머지는 소문자
a.capitalize()
>>> "Hi! everyone, i'm kim"

# '나 공백 이후 대문자
a.title()
>>> "Hi! Everyone, I'M Kim"

# 다 대문자
a.upper()
>>> "HI! EVERYONE, I'M KIM"

# 다 소문자
a.lower()
>>> "hi! everyone, i'm kim"

# 대/소문자 바꾸기
a.swapcase()
>>> "Hi! eVERYONE, i'M KIM"
```



- 기타 문자열 관련 검증 메소드 : 참/거짓 반환

  - 
    .isalpha(), .isdecimal(), .isdigit(), .isnumeric(), .isspace(), .isupper(), .istitle(), .islower()
    

    





## List

> **변경 가능하고(mutable), 순서가 있고(ordered), 순회 가능한(iterable)**



### 값 추가 및 삭제

- `.append(x)`
  - 리스트에 값을 추가
  - 해당 list 자체를 바꾸고 return은 없음
  - 파이썬에서는 push 대신 append 사용
  - 요소 하나 추가 시 사용

```python
l = [1, 2, 3]
print(l.append(4), type(l.append(5)), l)
>>> None <class 'NoneType'> [1, 2, 3, 4, 5]
```



- `.extend(iterable)`
  - 리스트에 iterable(list, range, tuple, string**[주의]**) 값을 붙일 수가 있음
  - 요소 여러개 추가 시 사용
  - String의 경우 한 문자씩 추가

```python
cafe = ['starbucks', 'tomntoms', 'hollys']
print(cafe)
>>> ['starbucks', 'tomntoms', 'hollys']

cafe.extend(['dunkin, tigersugar'])
>>> ['starbucks', 'tomntoms', 'hollys', 'dunkin, tigersugar']

cafe.extend(['ediya'])  # 하나의 문자열을 넣을 때는 리스트에 넣어서 
print(cafe)
>>> ['starbucks', 'tomntoms', 'hollys', 'dunkin, tigersugar', 'ediya']

# 리스트에 안 넣고 문자열 넣으면 문자열 문자하나하나 따로 들어감
cafe.extend('ediya')  
print(cafe)
>>> 
['starbucks', 'tomntoms', 'hollys', 'dunkin, tigersugar', 'ediya', 'e', 'd', 'i', 'y', 'a']
```



- concatenation

```python
b = []
b += ['김밥천국', '김밥나라']
print(b)
>>> ['김밥천국', '김밥나라']
```



- `.insert(i, x)`
  - 정해진 위치 `i`에 값을 추가

```python
cafe.insert(0, 'hi')  # index
cafe.insert(-1, 'hello')  # -1로 설정하면 뒤에서 두번째
print(cafe)
>>>
['hi', 'starbucks', 'tomntoms', 'hollys', 'dunkin, tigersugar', 'ediya', 'e', 'd', 'i', 'y', 'hello', 'a']

cafe.insert(len(cafe), 'bye')  # 마지막에 넣을 땐 len활용
print(cafe)
>>> 
['hi', 'starbucks', 'tomntoms', 'hollys', 'dunkin, tigersugar', 'ediya', 'e', 'd', 'i', 'y', 'hello', 'a', 'bye']

# 리스트의 길이를 넘어서는 인덱스는 마지막에 아이템이 추가됩니다.
cafe.insert(20000, '이만안녕')
print(cafe)
>>>
['hi', 'starbucks', 'tomntoms', 'hollys', 'twosomeplace', 'ediya', 'gongcha', 'dunkin, tigersugar', 'e', 'd', 'i', 'y', 'hello', 'a', 'bye', '이만안녕']

```



- `.remove(x)`
  - 리스트에서 값이 x인 것을 하나 삭제
  - 원본이 바뀐다.
  - return은 없다.

```python
numbers = [1, 2, 3, 1, 2]

numbers.remove(1)
print(numbers)
>>> [2, 3, 1, 2]

# remove는 값이 없으면 오류가 발생합니다.
numbers.remove(7)
>>> ValueError: list.remove(x): x not in list
```



- `.pop(i)`
  - 정해진 위치 `i`에 있는 값을 삭제하며, 그 항목을 **반환**
  - `i`가 지정되지 않으면 마지막 항목을 삭제하고 되돌려줌. (default = 마지막)
  - Stack 구조 First In Last Out(FILO)

```python
a = [1, 2, 3, 4, 5, 6]

a.pop()  # default는 맨 마지막 인덱스
>>> 6

a.pop(0)
>>> 1

print(a.pop(), type(a.pop()))  # return 존재
>>> 5 <class 'int'>

print(a)
>>> [2, 3, 4]
```



- `.clear()`
  - 리스트의 모든 항목을 삭제

```python
a = [1, 2, 3, 4, 5]
a.clear()
print(a)
>>> []
```







### 탐색 및 정렬

- `.index()`
  - x 값을 찾아 해당 **index 값을 반환**

```python
a = [1, 2, 3, 4, 5]
a.index(1)  # 값의 위치를 인덱스로 출력
>>> 0

# index는 없을 시 오류가 발생합니다.
a.index(6)
>>> ValueError: 6 is not in list
```



- `.count()`
  - 원하는 값의 개수를 확인

```python
a = [1, 2, 5, 1, 5, 1]
a.count(1)
>>> 3
```



- `.sort()`
  - 정렬을 합니다.
  - 내장함수 `sorted()` 와는 다르게 **원본 list를 변형**시키고, **`None`**을 리턴
  - **sorted()**의 경우에는 **return 존재, 원본은 그대로**

```python
import random
lotto = random.sample(range(1, 46), 6)
print(lotto)
>>> [12, 18, 29, 6, 45, 2]

# sorted() 를 사용해봅시다. sorted는 정렬된 리스트를 새로 생성, 원래껀 그대로
print(sorted(lotto))
print(lotto)
>>> 
[2, 6, 12, 18, 29, 45]
[12, 18, 29, 6, 45, 2]

# sort()는 그 자체를 바꿈
lotto.sort()
print(lotto)
>>> [2, 6, 12, 18, 29, 45]
```



- `.reverse()`
  - 반대로 뒤집기 **(정렬 아님)**
  - 원본을 바꿈

```python
classroom = ['Tom', 'David', 'Justin']
print(classroom)
>>> ['Tom', 'David', 'Justin']

classroom.reverse()
print(classroom)
>>> ['Justin', 'David', 'Tom']
```



### 복사

- 같은 List 객체를 가리키는 경우

  - `list_2 = list_1`
  - 2차원 list shallow copy

  

- 다른 List 객체를 가리키는 경우

  - `list_2 = list_1[:]` slicing
  - `list_2 = list(list_1)` list()
  - `list_2 = copy.copy(list_1)` import copy
  - 2차원 list deep copy



```python
string = '12345'
string2 = string
string2 += '6'
print(string, string2)  # string은 immutable 값 복사, 다른 객체를 가리켜 값을 바꿔도 따라가지 않는다.
>>> 12345 123456

lst = [1, 2, 3]
lst2 = lst
lst2 += [4]
print(lst, lst2)  # list는 mutable, 주소 복사
# 같은 객체를 가리켜 값을 바꾸면 똑같이 바뀐다.
>>> [1, 2, 3, 4] [1, 2, 3, 4]
```

```python
a = [1, 2, 3, 4]
# 전체를 똑같이 잘라냄
b = a[:]  # 이 경우 b는 새로운 list객 체를 생성하여 다른 주소를 가리킴
b[0] = 100

print(a)
print(b)
>>>
[1, 2, 3, 4]
[100, 2, 3, 4]
```

```python
a = [1, 2, 3, 4]
# 전체를 똑같이 잘라냄
b = list(a)  # 이 경우 b는 새로운 list 객체를 생성하여 다른 주소를 가리킴
# b = a[:] => 다른 주소
# b = copy.copy(a) => 다른 주소

b[0] = 100

print(a)
print(b)
>>>
[1, 2, 3, 4]
[100, 2, 3, 4]
```

```python
a = [[1, 2, 3], 2, 3]  # 2차원의 경우 a = [[주소], 2, 3]의 경우라 b에서 새로운 list 객체로 생성해도 2차원 내부 리스트는 주소 복사가 됨
b = list(a)
print(a, b)
>>>
[[1, 2, 3], 2, 3] [[1, 2, 3], 2, 3]

b[0][0] = 100
print(a, b)
>>>
[[100, 2, 3], 2, 3] [[100, 2, 3], 2, 3]

b[1] = '원소'  # b[1]은 1차원이라 다른 위치 가리킴 python 튜터 참고
print(a, b)
>>>
[[100, 2, 3], 2, 3] [[100, 2, 3], '원소', 3]
```

```python
import copy
a = [[1, 2, 3], 2, 3]
b = copy.deepcopy(a)  # 모듈 사용해서 2차원 내부리스트도 다른 객체로 생성
print(a, b)
>>>
[[1, 2, 3], 2, 3] [[1, 2, 3], 2, 3]

b[0][0] = 100
print(a, b)
>>>
[[1, 2, 3], 2, 3] [[100, 2, 3], 2, 3]
```



### List Comprehension

- 표현식과 제어문을 통해 리스트 생성
- 여러 줄의 코드를 한 줄로 줄일 수 있다.

```python
[expression for 변수 in iterable]

list(expression for 변수 in iterable)

[expression for 변수 in iterable if 조건식]

[expression if 조건식 else 식 for 변수 in iterable]
```

```python
'''
주어진 조건(x < y < z < 50) 내에서 피타고라스 방정식의 해를 찾으세요.
'''

result = [(x, y, z) for x in range(1, 50) for y in range(x+1, 50) for z in range(y+1, 50) if z**2 == x**2 + y**2]
print(result)
>>>
[(3, 4, 5), (5, 12, 13), (6, 8, 10), (7, 24, 25), (8, 15, 17), (9, 12, 15), (9, 40, 41), (10, 24, 26), (12, 16, 20), (12, 35, 37), (15, 20, 25), (15, 36, 39), (16, 30, 34), (18, 24, 30), (20, 21, 29), (21, 28, 35), (24, 32, 40), (27, 36, 45)]
```



## Set

> **변경 가능하고(mutable), 순서가 없고(unordered), 순회 가능한(iterable)**



### 추가 및 삭제

- `.add(elem)`
  - elem을 세트에 추가

```python
a = {'사과', '바나나', '수박'}
a.add('포도')  # 하나 추가시, 원본 a를 바꿈
print(a)  # set은 순서가 없다
>>> {'바나나', '수박', '포도', '사과'}
```



- `.update(*others(iterable))`
  - 여러가지 값을 추가
  - 인자로는 반드시 iterable 데이터 구조를 전달

```python
a = {'사과', '바나나', '수박'}
a.update(('포도', '배', '복숭아'))  # 여러개 추가시
print(a)
>>>
{'포도', '수박', '사과', '바나나', '복숭아', '배'}
```



- `.remove(elem)`
  - elem을 삭제하고, 없으면 KeyError 발생

```python
a = {'사과', '바나나', '수박'}
a.remove('사과')
print(a)
>>> {'바나나', '수박'}

a.remove('자몽')
print(a) 
>>> KeyError: '자몽'
```



- `discard(elem)`
  - elem을 삭제하고 없어도 에러 발생하지 않음

```python
a = {'사과', '바나나', '수박'}
a.discard('사과')
print(a)
>>> {'바나나', '수박'}

a.discard('자몽')
print(a)  # 없어도 오류 발생안함
>>> {'바나나', '수박'}
```



- `.pop()`
  - **임의의 원소** 제거해 반환 (list의 pop()과의 차이)

```python
a = {'사과', '바나나', '수박', '아보카도'}  # 순서 없다
a.pop()
print(a)
>>> {'아보카도', '수박', '사과'}
```





## Dictionary

> Dictionary의 key는 immutable => key가 list 불가
>
> **변경 가능하고(mutable), 순서가 없고(unordered), 순회 가능한(iterable)**
>
> `Key: Value` 페어(pair)의 자료구조



### 조회

- `.get(key[, default])`
  - key를 통해 value를 가져옴
  - KeyError 발생하지 않음.
  - default는 None
  - dict안에 없을 경우 default인자로 들어간 것 출력

```python
my_dict = {'apple': '사과', 'banana': '바나나', 'melon': '멜론'}
my_dict['pineapple']
>>> KeyError: 'pineapple'

my_dict.get('pineapple')
>>> None

my_dict.get('pineapple', '없어')
>>> '없어'
```



### 추가 및 삭제

- `.pop(key[, default])`
  - key가 dict에 있으면 제거하고 그 값을 반환
  - 없으면 default 반환
  - default 없는 상태에서 dict에 없으면 KeyError

```python
my_dict = {'apple': '사과', 'banana': '바나나'}
my_dict.pop('apple')  # dict => mutable 삭제 가능
>>> '사과'

my_dict
>>> {'banana': '바나나'}

my_dict.pop('pine')
>>> KeyError: 'pine'
```



- `.update()`
  - 값을 제공하는 key, value로 덮어씀

```python
my_dict = {'apple': '사과', 'banana': '바나나', 'melon': '멜론'}
my_dict.update({'banana' : '버네너'})
my_dict
>>> {'apple': '사과', 'banana': '버네너', 'melon': '멜론'}

my_dict.update(melon = '메론')  # 키워드 인자
my_dict
>>> {'apple': '사과', 'banana': '버네너', 'melon': '메론'}
```



### Dictionary 순회 (반복문)

```python
book_title =  ['great', 'expectations', 'the', 'adventures', 'of', 'sherlock', 'holmes', 'the', 'great', 'gasby', 'hamlet', 'adventures', 'of', 'huckleberry', 'fin']

count = {}
for word in book_title:
    count[word] = count.get(word, 0) + 1  # get => 키 가지고 오되, 없으면 생성, 0으로 초기화

count
>>> {'great': 2,
 'expectations': 1,
 'the': 2,
 'adventures': 2,
 'of': 2,
 'sherlock': 1,
 'holmes': 1,
 'gasby': 1,
 'hamlet': 1,
 'huckleberry': 1,
 'fin': 1}
```



### Dictionary Comprehension

```python
blood_types = {'A': 40, 'B': 11, 'AB': 4, 'O': 45}
negative_blood_types = {'-' + key: value for key, value in blood_types.items()}
# negative_blood_types = {'-' + key: blood_types[key] for key in blood_types}
print(negative_blood_types)
>>> 
{'-A': 40, '-B': 11, '-AB': 4, '-O': 45}
```



## 데이터 분류 immutable vs mutable

### immutable

- 리터럴(literal)
  - 숫자(Number)
  - 글자(String)
  - 참/거짓(Bool)
- range()
- tuple()
- frozenset()

```python
# immutable 데이터의 복사는 어떻게 이루어질까?
a = 20
b = a
b = 10

# 다른 객체, 다른 주소
print(a)
print(b)
>>>
20
10
```



### mutable

- `list`
- `dict`
- `set`

```python
# mutable 데이터의 복사는 어떻게 이루어질까?
a = [1, 2, 3, 4]
b = a
b[0] = 100

# 같은 객체, 같은 주소
print(a)
print(b)
>>>
[100, 2, 3, 4]
[100, 2, 3, 4]
```







## 데이터 구조에 적용가능한 Bulit-in Function

### `map(funtion, iterable)`

- 순회가능한 데이터 구조(iterable)의 모든 요소에 function을 적용한 후 그 결과를 반환

- return은 `map_object` 형태

```python
numbers = [1, 2, 3]
m = list(map(str, [1, 2, 3]))  # list에 저장
list(m)
>>> ['1', '2', '3']

list(m)  # list에서 저장한 것은 여러번 가져다 쓸 수 있음
>>> ['1', '2', '3']
```

```python
# 반복을 통해 특정 함수를 적용한 결과
numbers = [1, 2, 3]
[str(i) for i in numbers]
print(map(str, numbers), type(map(str, numbers)))
>>> <map object at 0x000001A704BC5700> <class 'map'>
```



###  `filter(function, iterable)`

- iterable에서 function의 반환된 결과가 `True` 인 것들만 구성하여 반환

- `filter object` 를 반환

```python
# 홀수인 요소만 뽑아 new_numbers에 저장합니다.
numbers = [1, 2, 3]
new_numbers = list(filter(odd, numbers))
print(new_numbers)
>>> [1, 3]
```



### `zip(*iterables)`

- 복수의 iterable 객체를 모아(`zip()`)준다.

- 결과는 튜플의 모음으로 구성된 `zip object` 를 반환

```python
girls = ['jane', 'ashley', 'mary']
boys = ['justin', 'eric', 'david']
pair = list(zip(girls, boys))
print(pair)
>>>
[('jane', 'justin'), ('ashley', 'eric'), ('mary', 'david')]
```



## Generator

- 생성자
- 한번 쓰고 나면 사라짐 => 메모리에는 있음

```python
small_g = (i for i in range(100))  # generator
big_g = (i for i in range(1000000))  # generator
small_l = [i for i in range(100)]  # list
big_l = [i for i in range(1000000)]  # list

import sys
print(sys.getsizeof(small_g), sys.getsizeof(big_g))  # generator를 사용하기 전까지는 크기 같음
>>> 112 112

print(sys.getsizeof(small_l), sys.getsizeof(big_l))
>>> 904 8697456
```

