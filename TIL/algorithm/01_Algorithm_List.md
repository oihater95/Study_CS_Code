# Algorithm & List 01

## 입출력

### 입력

- `input()`: string 자료형으로 입력 받음
- `split()`:  default = 공백, ()기준으로 나눔
- `map()`: 자료형 변환해서 받음

```python
# 문자열 입력
S = input()

# 다수 입력
A, B = input().split()

# 정수 입력
num = int(input())

# 다수의 정수 입력
num1, num2 = map(int, input().split())

# 리스트로 받기
arr = list(map(int, input().split()))

```



### 출력

- `.format()`: fstring과 동일
- `''.join()`: str형 을 ''기준으로 합침 

```python
# fstring 대신 format
print('{} {}'.format(a, b))

# join
a = ['1', '2', '3', '4']
' '.join(a)
>>> 1 2 3 4 

a = [1, 2, 3, 4]  # join은 str만 가능 => map으로 str
' '.join(map(str, a))
```



## 알고리즘

> 어떤 문제를 해결하기 위한 절차

- 표현
  - 슈더코드(의사 코드): 어떤 의도인지 보여주기 위함(문법적으로는 맞지 않음)
  - 순서도
- 좋은 알고리즘이란?
  - 정확성 => 완전탐색
  - 작업량(시간 복잡도)
  - 메모리
  - 단순성
  - 최적성

- 시간 복잡도(O)
  - 시간 복잡도 함수 중 가장 큰 영향력 주는 n에 대한 항만 표시
  - 계수 생략
  - O(logn) < O(n) < O(nlogn) < O(n^2) < O(2^n)
  - n개의 데이터 입력받아 저장 후 각 데이터에 1씩 증가 시킨 후 각 데이터를 출력하는 알고리즘의 시간복잡도는?
    - Ans: O(n)



## 배열

> 일정한 자료형의 변수들을 하나의 이름으로 열거하여 사용하는 자료구조

- 여러 개의 변수 필요할 때 효율적

- 1차원 배열 선언

```python
arr = list()
arr = []
arr = [0] * 5  # [0, 0, 0, 0, 0]
```



- 1차원 배열 접근

```python
arr[idx]  # 배열 arr의 idx번째 원소
```



- 예제

```python

```







## 정렬 (추후 추가)

- key: 자료 정렬하는 기준이 되는 특정 값 ex) 카드 번호
- 종류
  - 버블 정렬
  - 카운팅 정렬
  - 선택 정렬
  - 퀵 정렬
  - 삽입 정렬
  - 병합 정렬



### 버블 정렬

> 인접한 두개의 원소를 비교하며 자리를 계속 교환

- 첫번째 원소부터 인접한 원소끼리 계속 자리를 교환하면서 맨 마지막 자리까지 교환
- 한 cycle 끝나면 가장 큰 원소가 마지막 자리로 정렬
- 시간 복잡도: O(n^2)
- 가장 쉽고 정확 but 시간 오래걸림

```python
nums = [55, 7, 78, 12, 42]

for i in range(len(nums)):
    for j in range(len(nums)-1):  # 정렬된 뒷 부분도 확인
        if nums[j] > nums[j+1]:
            nums[j], nums[j+1] = nums[j+1], nums[j]
            nums
print(nums)
>>> [7, 12, 42, 55, 78]

arr = [55, 7, 78, 12, 42]
for i in range(len(arr)-1, 0, -1):
    for j in range(i):  # 정렬된 뒷 부분은 제외
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]

print(arr)
>>> [7, 12, 42, 55, 78]
```



### 카운팅 정렬

> 항목들의 순서를 결정하기 위해 집합에 각 항목이 몇 개씩 있는지 세는 작업 수행

- 제한 사항
  - 정수나 정수로 표현할 수 있는 자료만 적용 가능
  - 집합 내 가장 큰 정수를 알아야 한다.
- 시간 복잡도: O(n+k)
- 단점: 리스트 길이가 길거나 원소 수는 적은데 최댓값이 큰 경우 비효율적이다.
- 뒤에서 부터 정렬 => 동일한 값이 있을 때 순서 유지(안정 정렬)
- Flow
  - 각 요소 갯수를 카운트한 count 리스트 생성(각 요소의 값 = count 리스트의 인덱스)
  - count 리스트를 누적합으로 변환
  - 원본 리스트의 끝에서 부터 정렬 시작
  - 원본 리스트의 가장 마지막 인덱스의 요소값을 count 리스트의 인덱스로 하여 접근
  - 해당 count리스트 인덱스의 요소값에 -1 => -1하는 이유 인덱스 맞추기 위해
  - -1한 값을 인덱스로 하는 새로운 리스트 temp 해당 인덱스에 요소값을 원본 리스트의 요소값으로 삽입

```python
arr = [0, 4, 1, 3, 1, 2, 4, 1]
cnt = [0] * (max(arr)+1)  # 카운트 리스트

for num in arr:  # 카운트
    cnt[num] += 1

for i in range(1, len(cnt)):  # 누적합
    cnt[i] = cnt[i-1] + cnt[i]

temp = [0] * len(arr)  # 정렬된 리스트

for i in range(len(arr)-1, -1, -1):
    temp[cnt[arr[i]]-1] = arr[i]
    cnt[arr[i]] -= 1

print(temp)
>>> [0, 1, 1, 1, 2, 3, 4, 4]
```



## 완전 검색(완전 탐색)

> 문제 해법으로 생각할 수 있는 모든 경우의 수를 나열해보고 확인

- Brute-force, Generate-and-Test
- 느리지만 답은 찾을 수 있다.

- 순열 

```python
# Baby-gin => 완전 탐색, 순열 사용 => 추후 추가
# 모든 경우의 수를 구해 앞 3자리 뒤 3자리 나누어 tri인지 run인지 
nums = [2, 3, 5, 7, 7, 7]
new_nums = list(list())

for i in nums[:3]:
     for j in nums[:3]:
         if j != i:
             for k in nums[:3]:
                 if k != i and k != j:
                     new_nums.append([i, j, k])
```





## Greedy(탐욕) 알고리즘

> 최적해를 구하는데 사용되는 근시안적 방법

- 여러 경우 중 하나 결정할 때마다 그 순간에 최적이라고 생각되는 것을 선택
- 지역적으로 최적, 전체적으로는 최적X
- 떠오르는 생각을 검증없이 바로 구현

- Flow
  - 해 선택: 현 상태에서 부분 문제의 최적해를 구한 뒤 부분 해 집합에 추가
  - 실행 가능성 검사: 새로운 부분 해 집합 실행 가능한지 보고 제약 조건 체크
  - 해 검사: 새로운 부분 해 집합이 문제의 해가 되는 지 확인 아니라면 다시 해 선택으로

```python
# baby-gin
nums = [1, 2, 3, 5, 5, 5]
cnt = [0] * 10

for num in nums:
    cnt[num] += 1

run = False
tri = False

if cnt[0] >= 3:
    tri = True
    cnt[0] -= 3
elif cnt[len(cnt)-1] >= 3:
    tri = True
    cnt[len(cnt)-1] -= 3

for i in range(1, len(cnt)-1):
    # tri
    if cnt[i] >= 3:
        tri = True
        cnt[i] -= 3
    # run
    if cnt[i] == 1 and cnt[i-1] == 1 and cnt [i+1] == 1:
        run = True

if tri and run:
    print('baby-gin')
else:
    print('nope')
>>> baby-gin
```

