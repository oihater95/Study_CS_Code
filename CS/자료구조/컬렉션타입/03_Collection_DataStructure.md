# 03. Collection Data Structure

- 셋(set) 
- 딕셔너리(dictionary)

## Set

> `set`은 순서가 없는 자료구조
>
> {value1, value2, value3}

- `set`은 수학에서의 집합과 동일하게 처리된다.
- `set`은 중괄호`{}`를 통해 만든다.
- 빈 집합을 만들려면 `set()`을 사용 (`{}`로 사용 불가능.)
- **반복 가능(iterable), 가변적(mutable), 중복없고 정렬되지 않음(순서가 없다)**

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



### Frozen Set

- **불변(immutable)**인 set
- set의 일부 메서드 사용불가



### Method

#### 추가 및 삭제

- `.add(elem)`
  - elem을 세트에 추가

```python
a = {'사과', '바나나', '수박'}
a.add('포도')  # 하나 추가시, 원본 a를 바꿈
print(a)  # set은 순서가 없다
>>> {'바나나', '수박', '포도', '사과'}
```



- `.update(*others(iterable))`
  - 여러가지 값을 추가, 합집합
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



#### 집합연산

- 합집합:  `.update(*others(iterable))` or `|=`  but  `+`는 안됨
- 교집합: `.intersection(*others(iterable))` or `&`
- 차집합:  `.difference(*others(iterable))` or `-`



## Dictionary

> `dictionary`는 `key`와 `value`가 쌍으로 이루어짐
>
> 이름표가 붙은 박스
>
> {Key1:Value1, Key2:Value2, Key3:Value3, ...}

- **정렬되지 않아** 임의의 순서대로 항목을 순회 => 인덱스 위치 접근 및 슬라이싱 불가
- **변경가능(mutable), 순회가능(iterable)**
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


### Method
#### 조회

- `.setdefault()`
  
- 딕셔너리에서 key의 존재 여부 모른 채 접근할 경우 사용
  
- `.setdefault(key, value)`
    - key 존재하면 해당하는 value 반환
    - key 존재하지 않으면 새로운 key와 기본값 default가 딕셔너리에 저장

  ```python
temp = {1: 'a', 2: 'b', 3: 'c'}
print(temp.setdefault(1))
temp.setdefault(4)
print(temp)
  >>>
  a
  {1: 'a', 2: 'b', 3: 'c', 4: None}
  ```



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



- `.items()`
  - key와 value 반환

```python
temp = {1: 'a', 2: 'b', 3: 'c', 4: None}
print(temp.items())
>>>
dict_items([(1, 'a'), (2, 'b'), (3, 'c'), (4, None)])
```

- `.keys()`
  - key만 반환

```python
temp = {1: 'a', 2: 'b', 3: 'c', 4: None}
print(temp.keys())
>>>
dict_keys([1, 2, 3, 4])
```

- `.values()`
  - value만 반환

```python
temp = {1: 'a', 2: 'b', 3: 'c', 4: None}
print(temp.values())
>>>
dict_values(['a', 'b', 'c', None])
```





#### 추가 및 삭제

- `.pop(key[, default])`
  - key가 dict에 있으면 제거하고 그 **값(value)**을 반환
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

- `.popitem()`
  - 딕셔너리에 저장된 key와 value 쌍 랜덤 제거
  - 삭제한 (key, value) 반환

```python
temp = {1: 'a', 2: 'b', 3: 'c', 4: None}
print(temp.popitem())
print(temp.popitem())
print(temp)
>>>
(1, 'a')
(2, 'b')
{3: 'c', 4: None}
```



- `clear()`

```python
temp.clear()
print(temp)
>>> {}
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



#### 정렬

- `.sorted()`
  - items(), keys(), values() 기준

```python
tmp = {1: 20, 2: 10, 3: 30}
print(sorted(tmp.keys()))
print(sorted(tmp.values()))
print(sorted(tmp.items()))
>>>
[1, 2, 3]
[10, 20, 30]
[(1, 20), (2, 10), (3, 30)]
```



## Collection Type

### 기본 딕셔너리

> from collections import defaultdict

- 내장 딕셔너리 + 누락된 key 처리가능



### 정렬된 딕셔너리

> from collections import OrderedDict

- 내장 딕셔너리 + 순서를 가짐
- 삽입한 순서대로 추가됨

```python
from collections import OrderedDict
tasks = OrderedDict()
task[1000] = '백업'
task[3543] = '스캔'
task[12] = '빌드'
print(task)
>>>
OrderedDict([(1000, '백업'), (3543, '스캔'), (12, '빌드')])
```



### 카운터 딕셔너리

> from collectins import Counter

- 해시 가능한 객체를 카운팅

```python
from collections import Counter
seq = [1, 2 , 3, 5, 1, 2 , 5, 5, 2, 5, 1, 4]
seq_count = Counter(seq)
print(seq_count)
>>>
Counter({5: 4, 1: 3, 2: 3, 3: 1, 4: 1})
```

