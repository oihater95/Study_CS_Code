# 0118 Data Container

>Container
>
>여러 개의 값을 저장할 수 있는 것(~~객체~~) => 모든 명사

- 시퀀스(Sequence)형: 순서가 있는(ordered) 데이터
- 비 시퀀스(Non-sequence)형: 순서가 없는(unordered) 데이터 => {}
- 정의는 '[]', '{}' 등 여러가지이지만 접근은 항상 '[]'



## Sequence형 Container

`시퀀스`는 데이터가 순서대로 나열된(ordered) 형식을 나타냅니다.

- **주의! 순서대로 나열된 것이 `정렬되었다(sorted)`라는 뜻은 아니다.**

- 특징
  - 순서를 가질 수 있다.
  - **특정 위치의 데이터를 가리킬 수 있다.** (index 접근 가능 == 순서가 있다)
- 종류
  - 리스트(list) : mutable
  - 튜플(tuple) : immutable
  - 레인지(range) : immutable
  - 문자형(string) : immutable
  - 바이너리(binary)

### List

> 상자의 연속체
>
> [value1, value2, value3 ... ]




![image-20210119224313234](05_0118_Data_Container.assets/image-20210119224313234.png)

- 리스트는 대괄호`[]` 및 `list()` 를 통해 만들 수 있습니다.

  값에 대한 접근은 `list[i]`를 통해 합니다.

```python
my_list = []  # Literal 생성=> [], {}, '' 상징기호같은 것
'''
Literal
'' == str()
{} == dict()
[] == set()
() == tuple()
set, range => 없음
'''
another_list = list()  # 표준 생성
print(type(my_list))
print(type(another_list))
>>>
<class 'list'>
<class 'list'>
```

```python
# 인덱스 접근
sushi_menus = ['광어', '연어', '방어', '참치']
sushi_menus[0]
>>> '광어'
```

```python
print([range(3)])  #리스트의 원소로 하나의 range를 넣는다
print(list(range(3)))  # range(3)을 list로 형변환한다
>>>
[range(0, 3)]
[0, 1, 2]
```



### Tuple

> (value1, value2)

- 튜플은 리스트와 유사하지만, `()`로 묶어서 표현합니다.
-  tuple은 수정 불가능(불변, immutable)하고, 읽을 수 밖에 없습니다.
- 직접 사용하기 보다는 파이썬 내부에서 다양한 용도로 활용되고 있습니다.

```python
# 튜플 생성
my_tuple = (1, 2)
print(type(my_tuple))
>>> <class 'tuple'>

another_tuple = 1, 2
print(another_tuple)
print(type(another_tuple))
>>>
(1, 2)
<class 'tuple'>

# 파이썬 내부에서는 다음과 같이 활용됩니다.
x, y = 1, 2
print(x, y)
>>> 1 2

# 변수의 값을 swap하는 코드 역시 tuple을 활용하고 있습니다. 
x = 1
y = 100
x, y = y, x
print(x, y)
>>> 100 1

# 빈 튜플은 빈 괄호 쌍으로 만들어집니다.
empty = ()  # Literal 생성
print(type(empty))
print(len(empty))
>>>
<class 'tuple'>
0
```

```python
tuple1 = ('hello')
type(tuple1)
>>> str

# 하나의 요소를 튜플로 만드려면 요소 뒤에 ,를 붙여줘야함
single_tuple = ('hello',)  
print(type(single_tuple))
print(len(single_tuple))
>>> 
<class 'tuple'>
1
```

```python
# 리스트는 특정 원소 변경 가능
my_list = [1, 3]
my_list[0] = '첫번째'
print(my_list)
>>> ['첫번째', 3]

# 튜플은 수정 불가
my_tuple = (1, 3)
my_tuple[0] = '첫번째'
>>> TypeError: 'tuple' object does not support item assignment
```



### Range

> `range` 는 숫자의 시퀀스를 나타내기 위해 사용됩니다.
>
> (이상, 미만, 스텝)
>
> 스텝의 default는 1

- 기본형 : `range(n)` == `range(0, n, 1)`
  - 0부터 n-1까지 값을 가짐

- 범위 지정 : `range(n, m)`
  - n부터 m-1까지 값을 가짐

- 범위 및 스텝 지정 : `range(n, m, s)`
  - n부터 m-1까지 +s만큼 증가한다

```python
# range 생성
range(3)
>>> range(0, 3)

type(range(3))
>>> range

# range에 담긴 것을 list로 형변환
list(range(3))
>>> [0, 1, 2]

# 0부터 -9까지 담긴 range 생성
print(list(range(0, -10, 1)))
>>> []

print(list(range(0, -10, -1)))
>>> [0, -1, -2, -3, -4, -5, -6, -7, -8, -9]
```



### Sequence에서 활용할 수 있는 연산자/함수

| operation    | 설명             |
| ------------ | ---------------- |
| x `in` s     | containment test |
| x `not in` s | containment test |
| s1 `+` s2    | concatenation    |
|s `*` n|n번만큼 반복하여 더하기|
|`s[i]`|indexing|
|`s[i:j]`|slicing|
|`s[i:j:k`]|k간격으로 slicing|
|len(s)|길이|
|min(s)|최솟값|
|max(s)|최댓값|
|s.count(x)|x의 개수|

```python
s = 'string'
print('a' in s)
>>> False
```

```python
# 인덱스 접근
s = 'string'
print(s[0], s[2], s[-1])
>>> s r g
```

```python
# concatenation(연결, 연쇄)
print('안녕,' + '하세요')
print((1, 2) + (5, 6))
print([1, 2] + [5, 6])
>>>
안녕,하세요
(1, 2, 5, 6)
[1, 2, 5, 6]
```

```python
# 숫자 0이 6개 있는 list
my_list = [0, 0, 0, 0, 0, 0]
print(my_list)
>>> [0, 0, 0, 0, 0, 0]

print([0] * 6)
>>> [0, 0, 0, 0, 0, 0]
```

```python
# Indexing & Slicing
location = ['서울', '대구', '부산', '광주', ' 제주',]
print(location[1], location[2])
>>> 대구 부산

# range처럼 인덱스 [이상:미만]으로 보면 됨
print(location[1:3])
>>> 대구 부산
```

```python
# 0부터 30까지의 숫자를 3씩 증가시킨 리스트
# range(n, m)범위에서 1씩 증가하는 시퀀스, step이 float형일 수는 없다
sample_list = list(range(0, 31, 3))
sample_list
>>> [0, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30]

# slicing
sample_list2 = list(range(0, 31))
# ::는 전체를 뜻함, 0부터 끝까지, step = 3, 
# == sample_list2[0:len(sample_list2):3]
sample_list2[0::3]  
>>> [0, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30]

sample_list2[-1::-3]
>>> [30, 27, 24, 21, 18, 15, 12, 9, 6, 3, 0]

print(min(sample_list), max(sample_list))
>>> 0 30

# 리스트 내 1 갯수 세기
samples = [1, 11, 1, 2, 22, 3,]
samples.count(1)
>>> 2

# index 확인
samples =  [1, 11, 1, 2, 22, 3,]
samples.index(11)
>> 1
```

```python
# 인덱스 접근 가능 => Sequence형
print(
    [1, 2, 3][0],
    (1, 2, 3)[0],
    '123'[0],
    range(10, 20)[0]
)
>>> 1 1 1 10
```



## Non-Sequence형 Container

- 셋(set) : mutable
- 딕셔너리(dictionary) : mutable



### Set

> `set`은 순서가 없는 자료구조입니다.
>
> {value1, value2, value3}

- `set`은 수학에서의 집합과 동일하게 처리된다.
- `set`은 중괄호`{}`를 통해 만들며, **순서가 없고 중복된 값이 없다.**
- 빈 집합을 만들려면 `set()`을 사용해야 합니다. (`{}`로 사용 불가능.)

```python
set_a = {1, 2, 3,}
print(set_a)
set_b = {3, 6, 9,}
print(set_b)  
>>>
{1, 2, 3}
{9, 3, 6}

# 순서대로 나열 x, 순서대로 나와도 그냥 랜덤에서 걸린거, 순서가 보장되어 있지 않음
```

```python
set_a = {1, 2, 3,}
set_b = {3, 6, 9,}
# 차집합
set_a - set_b
>>>
{1, 2}

# 합집합
# +를 쓰면 중복되는 것이 생길 수 있기 때문에 불가, set은 중복 불가
set_a | set_b  
>>> {1, 2, 3, 6, 9}

# 교집합
set_a & set_b
>>> {3}
```

```python
set_c = {1, 2, 2, 3, 6, 5, 4,}
print(set_c)  # 중복되는 요소 없애고 출력
>>> {1, 2, 3, 4, 5, 6}

list_1=[1, 2, 3, 1, 2, 3, 1, 2, 3,]
set_1 = set(list_1)
set_1
>>> {1, 2, 3}

list(set(list_1))
>>> [1, 2, 3]
```



### Dictionary

> `dictionary`는 `key`와 `value`가 쌍으로 이뤄져있으며, 궁극의 자료구조이다.
>
> 이름표가 붙은 박스
>
> {Key1:Value1, Key2:Value2, Key3:Value3, ...}

![image-20210119230804537](05_0118_Data_Container.assets/image-20210119230804537.png)

- `{}`를 통해 만들며, `dict()`로 만들 수도 있다.
- `key`는 **변경 불가능(immutable)한 데이터**만 가능하다. (immutable : string, integer, float, boolean, tuple, range)
- `value`는 `list`, `dictionary`를 포함한 모든 것이 가능하다.

```python
# 비어있는 중괄호{}는 set이 아닌 dictionary로 인식
dict_a = {}  
print(dict_a, type(dict_a))
dict_b = dict()
print(dict_b)
>>>
{} <class 'dict'>
{}
```

```python
# dictionary는 중복된 key는 존재할 수가 없습니다.
my_dict = {'김준호': '남', '김준호': '여', '홍길동': '남'}
my_dict  # 최근 값으로 바뀜
>>> {'김준호': '여', '홍길동': '남'}
```

```python
phone = {'서울': '02', '경기': '031'}

# key로 접근
phone['서울']
>>> '02'

phone.keys()  # duck typing
>>> dict_keys(['서울', '경기'])

# list처럼 보여도 list아니다. list로 바꾸려면 list()로 형변환해야됨
print(phone.values(), type(phone.values()))  
>>> dict_values(['02', '031']) <class 'dict_values'>

'''
딕셔너리의 .items() 메소드를 활용하여 key, value를 확인 해볼 수 있습니다.
dict.items()는 유사 list
list로 변경해서 볼 수 있다.
(key, value)가 튜플로 묶인 원소로 만들어진다
'''
print(phone.items(), type(phone.items()))
>>> 
dict_items([('서울', '02'), ('경기', '031')]) <class 'dict_items'>

# 튜플은 시퀀스형이라 인덱스로 접근 가능 but 수정은 불가
list(phone.items())[0]  
>>> ('서울', '02')

type(list(phone.items())[0])
>>> tuple
```



## Container형 형변환

![image-20210119231357134](05_0118_Data_Container.assets/image-20210119231357134.png)

- 어떤 자료형이든 range나 dictionary로 변경 불가
- dictionary를 다른 자료형으로 바꿀 때 key만 들어감

```python
# list 형변환 / 형변환 불가는 주석처리함
l = [1, 2, 3, 4]
# [1, 2, 3, 4] 를 range로 표현하면 range(1, 5)이지만 range(l)은 불가하다

print(str(l))
print(tuple(l))
print(set(l))
# 형변환 불가
# range(l)
# dict(l)
>>> 
[1, 2, 3, 4]
(1, 2, 3, 4)
{1, 2, 3, 4}
```

```python
# tuple
t = (1, 2, 3, 4)
print(str(t))
print(list(t))
print(set(t))
# # range(t)
# # dict(t)
>>>
(1, 2, 3, 4)
[1, 2, 3, 4]
{1, 2, 3, 4}
```

```python
# range
r = range(1, 5)
print(str(r))
print(list(r))
print(set(r))
print(tuple(r))
# # dict(r)
>>>
range(1, 5)
[1, 2, 3, 4]
{1, 2, 3, 4}
(1, 2, 3, 4)
```

```python
# set
s = {1, 2, 3, 4}
print(str(s))
print(list(s))
print(tuple(s))
# # range(s)
# # dict(s)
>>>
{1, 2, 3, 4}
[1, 2, 3, 4]
(1, 2, 3, 4)
```

```python
# dictionary
d = {'name': 'moon', 'year': 2020}
'''
list, tuple, set은 키만 모아서 바꾼다
dictionary는 key를 통해 value에 접근
value를 통해 key 접근은 불가
'''
print(str(d))
print(list(d))
print(tuple(d))
print(set(d))
# # range(d)
>>>
{'name': 'moon', 'year': 2020}
['name', 'year']
('name', 'year')
{'year', 'name'}
```



## 데이터 분류

> `mutable` vs. `immutable`



### 변경 불가능한(`immutable`) 데이터

- 리터럴(literal)
  - 숫자(Number)
  - 글자(String)
  - 참/거짓(Bool)
- range()
- tuple()
- ~~frozenset()~~

```python
t = (1, 3)
t[0] = 2  # 변경 불가
>>> TypeError: 'tuple' object does not support item assignment

name = '홍길동'
name[0] = '김'  # string형 문자열은 인덱스로 접근은 가능하지만 변경은 불가능하다.(immutable) => 할당 불가
>>> TypeError: 'str' object does not support item assignment
```

```python
# immutable 데이터의 복사는 어떻게 이루어질까?
num1 = 20
num2 = num1 
num2 = 10

print(num1, num2)
# 메모리상 num1 과 num2는 분리됨 num2만 변경됨 (주소 공유 x)
>>> 20 10

# int(10)자체에 메모리 할당
num3 = 10
num4 = 10
id(num3) == id(num4)
>>> True
```

```python
%%html
<iframe width="800" height="500" frameborder="0" src="http://pythontutor.com/iframe-embed.html#code=a%20%3D%2020%0Ab%20%3D%20a%0Ab%20%3D%2010%0A%0Aprint%28a%29%0Aprint%28b%29&codeDivHeight=400&codeDivWidth=350&cumulative=false&curInstr=0&heapPrimitives=nevernest&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false"> </iframe>
```





### 변경 가능한(`mutable`) 데이터

- `list`
- `dict`
- `set`

```python
# mutable 데이터의 복사는 어떻게 이루어질까?
num1 = [1, 2, 3, 4]
num2 = num1
num2[0] = 100

print(num1)
print(num2)

# list의 데이터가 바뀐 이유 = list의 경우 객체를 공유(같은 곳을 가리킴)
>>>
[100, 2, 3, 4]
[100, 2, 3, 4]

num1 is num2
>>> True
```

```python
%%html
<iframe width="800" height="500" frameborder="0" src="http://pythontutor.com/iframe-embed.html#code=num1%20%3D%20%5B1,%202,%203,%204%5D%0Anum2%20%3D%20num1%0Anum2%5B0%5D%20%3D%20100%0A%0Aprint%28num1%29%0Aprint%28num2%29&codeDivHeight=400&codeDivWidth=350&cumulative=false&curInstr=0&heapPrimitives=nevernest&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false"> </iframe>
```

```python
num1 = [1, 2, 3, 4]
num2 = list(num1)  # num2 = num1이 아닌 새로운 리스트로 만들면 공유 안함
num2[0] = 100
print(num1)
print(num2)
>>>
[1, 2, 3, 4]
[100, 2, 3, 4]
```

```python
num1 is num2  # num1과 num2가 같은 리스트 참조하는지 -> 다른 리스트 참조: False
>>> False
```

```python
%%html  # 위 코드 넣어보기
<iframe width="800" height="500" frameborder="0" src="http://pythontutor.com/visualize.html#mode=display"> </iframe>
```

```python
# string => immutable -> 같은 주소 (객체는 아님)
str1 = 'asdf'
str2 = 'asdf'  # str1 과 str2 같은 주소
print(id(str1), id(str2))
print(id(str1) is id(str2))
print(str1 is str2)
# python에서는 True가 나오지만 notebook에서는 False 나옴 (notebook이 예외적)
>>>
2557563219440 2557563219440
False
True
```

```python
# list => mutable
list1 = [1, 2, 3]
list2 = [1, 2, 3]  # list1과 list2는 같은 값을 가졌지만 다른 객체
print(id(list1), id(list2))
print(id(list1) is id(list2))
# list1 = list2로 하면 둘은 같은 객체
>>>
2557563180800 2557563086272
False
```

```python
# tuple => immutable -> 같은 객체
tup1 = (1, 2, 3)
tup2 = (1, 2, 3)  # tup1과 tup2는 같은 객체
print(id(tup1), id(tup2))
print(id(tup1) is id(tup2))
# python에선 True, notebook에서는 False (notebook이 예외적)
>>>
2557532957440 2557532755648
False
```

```python
tup = (1, 2)
tup = (1, 2, 3)  # 다시 할당한 것
'''
tup = (1, 2) 가 없어진 것은 아니고 메모리상에 남아있기는 하지만 tup은 (1, 2)를 가리키지 않고 (1, 2, 3)을 가리킴, 덮어씌워진 것이 아님

또한 (1, 2) 가 중간에 바뀌거나 뒤에 추가될 수 없다.

즉, (1, 2)와 (1, 2, 3)은 아예 다른 것, 주소를 공유하지도 않음

이름이 없어진 (1, 2)는 나중에 garbage collecting을 통해 메모리상에서 지워진다.
'''
```

```python
str_1 = 'abc'
str_2 = 'def'
print(id(str_1))
str_1 = str_1 + str_2  # 이 때 str_1에 추가로 더해지는 것이 아니고 str_1이 새로 재할당 되는 것, id(str_1)이 달라짐
print(str_1, id(str_1))
>>>
2557490812464
abcdef 2557533897520
```

```python
ls1 = [1, 2, 3]
print(id(ls1))

ls1.append(4)
print(id(ls1))

ls1.append(5)
print(id(ls1))  # append의 경우 같은 객체에 더해주는 것

ls1 = ls1 + [6, 7]
print(id(ls1))  # concatenation의 경우 재할당하는 것

>>>>
2557533871488
2557533871488
2557533871488
2557533020416
```



## Summary

![image-20210119232657131](05_0118_Data_Container.assets/image-20210119232657131.png)