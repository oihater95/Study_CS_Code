# Algorithm_Stack

## Stack

- 선형구조: 1대1, stack
- 비선형구조: 1대N, 트리, 그래프(cycle)
- 자료를 삽입하거나 꺼낼 수 있다.
- 후입선출 (LIFO: Last In First Out)
- 예시: 실행취소, 브라우저 뒤로가기



### 연산

- top(): 스택에서 마지막에 삽입된 원소 위치
- push(): 삽입 (List append)
- pop(): 삭제
- isEmpty(): 공백확인, 비어있으면 True 아니면 False
- peek(): top에 있는 item(원소)반환 => 꺼내지 않고 값만 확인

```python
# 리스트의 경우(크기 지정 x)
def push(item):  # 삽입
    s.append(item)


def pop():
    if len(s) == 0:  # 공백검사, underflow
        return
    else:
        return s.pop()  # s.pop(-1), pop의 경우 default가 맨 마지막 값

s = []
#######################################################################
# 배열의 경우 (크기 지정 o)
class Stack:
    def __init__(self, n):
        self.top = -1  # top 위치
        self.stack = [0]*n  # 스택 크기 지정

    def push(self, data):
        if self.top == len(self.stack) - 1:  # 꽉 차면 push 안함
            return None
        self.top += 1  # top 1 증가시킨 후 top위치에 추가
        self.stack[self.top] = data
        print(self.stack)

    def pop(self):
        if self.top == 0:  # 비어있다면 pop안함
            return None
        self.top -= 1  # top 1 감소시킨 후 이 전 top을 0으로 함
        p = self.stack[self.top+1]  # 리턴하는 위치
        self.stack[self.top+1] = 0
        print(self.stack)
        return p




my_stack = Stack(5)
my_stack.push(1)
my_stack.push(2)
my_stack.push(3)
print(my_stack.top)
print(my_stack.pop())
print(my_stack.pop())
>>>
[1, 0, 0, 0, 0]
[1, 2, 0, 0, 0]
[1, 2, 3, 0, 0]
2
[1, 2, 0, 0, 0]
3
[1, 0, 0, 0, 0]
2
```



### 예제

#### 괄호검사

- (),{},[],<> 짝이 맞는지 검사
  - (((({}{()}<<[()(){{{}}}]>>)))) 가능
  - ( { ( } [ ) ] ) 불가능

```python
for test_case in range(1, 11):
    N = int(input())
    arr = list(input())
    s = []  # stack
    answer = 0  # 짝이 맞는지 안 맞는지
    # 첫번째 원소 삽입
    if arr[0] == '(' or '{' or '[' or '<':
        s.append(arr[0])

    # 원소 삽입, 짝이 맞으면 pop
    for i in range(1, N):
        # push
        if arr[i] in '({[<':
            s.append(arr[i])

        # stack의 top과 짝이 맞으면 pop
        elif arr[i] == ')' and s[len(s)-1] == '(':
            s.pop()
        elif arr[i] == '}' and s[len(s)-1] == '{':
            s.pop()
        elif arr[i] == ']' and s[len(s)-1] == '[':
            s.pop()
        elif arr[i] == '>' and s[len(s)-1] == '<':
            s.pop()
        # 규칙에 맞지 않는 경우 break, 0 출력
        else:
            break

    if len(s) == 0:
        answer = 1

    print('#{} {}'.format(test_case, answer))
```





## Recursive 재귀

- 중복되는 연산이 많아 느리다

```python
def fibo(n):
    if n < 2:
        return n
    else:
        return fibo(n-1) + fibo(n-2)


print(fibo(10))
```



## DP 동적계획법

### 예제

#### 피보나치

- recursive => 중복되는 연산 제거

```python
# 피보나치 DP (Memoization), recursive
# 리스트 길이 미리 할당 X
# fibo(n)값을 계산하자마자 저장 실행시간 O(n)
# memo를 위한 배열 할당, 모두 0으로 초기화
# memo[0] = 0, memo[1] = 1  => 0과 1은 구하지 않음

def fibo_memo(n):
    global memo
    if n >= 2 and len(memo) <= n:  # len(memo) > n => 이미 값이 구해져있다
        memo.append(fibo_memo(n-1) + fibo_memo(n-2))
    return memo[n]

memo = [0, 1]

print(fibo_memo(40))
```



- iterative

```python
# 피보나치 DP2, iterative
# 배열 크기 미리 할당
memo2 = [-1] * 21
memo2[0] = 0
memo2[1] = 1


def fibo_memo2(n):
    if memo2[n] == -1:  # 아직 안 구했다면
        memo2[n] = fibo_memo2(n-1) + fibo_memo2(n-2)

    return memo2[n]  # 이미 구해져있다면


print(fibo_memo2(10))
```





## DFS

- 비선형 구조인 그래프 구조는 그래프로 표현된 **모든 자료를 빠짐없이 검색**
- 시작 정점의 한 방향으로 갈 수 있는 경로가 있는 곳까지 쭉 깊이 탐색
- 더 이상 갈 곳이 없게 되면 가장 마지막(최근)에 만났던 갈림길이 있는 정점으로 되돌아와 다른 방향의 정점으로 탐색 반복
- 가장 마지막에 만났던 갈림길의 정점으로 되돌아감



### 알고리즘

1. 시작 정점 v 결정, 방문
2. 방문하지 않은 정점 w있으면 정점 v를 스택에 push, w방문
3. w를 v로 갱신
4. 방문하지 않은 정점 없으면 탐색 방향 전환 => 스택에 pop
5. 가장 마지막 정점을 v로 설정
6. 스택이 빌 때까지 반복



### 예제

```python
# 백준 알고리즘 2583_영역구하기
def dfs(row, col):  #
    global area
    area += 1  # dfs 한 층 내려갈 때마다 넓이(빈 영역 1칸) + 1
    arr[row][col] = 1  # 카운트한 영역은 1로 갱신

    for i in range(4):
        nr = row + dr[i]
        nc = col + dc[i]
        if 0 <= nr < M and 0 <= nc < N and arr[nr][nc] == 0:
            dfs(nr, nc)

M, N, K = map(int,input().split())
arr = [[0 for _ in range(N)] for i in range(M)]
ans = []  # 각 영역 넓이 리스트

for i in range(K):
    min_col, min_row, max_col, max_row = map(int, input().split())
    for j in range(min_row, max_row):
        for k in range(min_col, max_col):
            arr[j][k] = 1

# 상하좌우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

for i in range(M):
    for j in range(N):
        if arr[i][j] == 0:
            area = 0
            dfs(i, j)
            ans.append(area)

ans = sorted(ans)
print(len(ans))
for area_elem in ans:
    print(area_elem, end = ' ')
```





## 백트래킹

- 해를 찾는 도중에 막히면(해가 아니면) 되돌아가서 해를 찾는 기법
- 최적화(optimization)문제와 결정(decision) 문제를 해결할 수 있다.
- 결정(decision) 문제: 문제의 조건을 만족하는 해가 존재하는지의 여부를 Yes or No 답하는 문제
  - 미로찾기
  - n-Queen
  - Map coloring
  - 부분 집합의 해
- 어떤 노드의 유망성을 점검한 후에 유망하지 않다고 결정되면 그 노드의 부모로 되돌아가 다음 자식 노드를 탐색(Backtracking)
- 어떤 노드를 방문했을 때 그 노드를 포함한 경로가 해답이 될 수 없으면 그 노드를 유망하지 않다고 판단, 해답 가능성 있으면 유망하다고 판단
- 가지치기(Prunning): 유망하지 않는 노드가 포함되는 경로는 더 이상 고려하지 않음

### Backtracking과 DFS와의 차이

- 어떤 노드에서 출발하는 경로가 해결책으로 이어질 것 같지 않으면 더 이상 그 경로를 탐색하지 않음. (Prunning 가지치기)
- 그에 비해 깊이우선탐색(DFS)는 모든 경로를 추적함
- DFS는 경우의 수가 너무나 많지만 백트래킹 알고리즘 또한 최악의 경우에는 지수함수 시간(Expoenetial Time)을 요함



### 알고리즘

1. 상태 공간 트리의 깊이 우선 검색을 실시한다.
2. 각 노드가 유망한지 점검한다.
3. 만일 그 노드가 유망하지 않으면, 그 노드의 부모 노드로 돌아가서 검색을 계속한다



### 예제

#### 부분집합

```python
# 백트래킹
N = 3

arr = [1, 2, 3]  # 활용할 데이터

sel = [0] * N  # a 리스트 (내가 해당 원소를 뽑았는지 체크)

def powerset(idx):
    if idx == N:
        print(sel, ':', end = ' ')
        for i in range(N):
            if sel[i]:
                print(arr[i], end = ' ')
        print()

        return  # 호출한 곳으로 돌아감 (return이 none)

    # idx 자리를 안 뽑고 간다
    sel[idx] = 0
    powerset(idx + 1)
    # idx 자리의 원소를 뽑고 간다
    sel[idx] = 1
    powerset(idx + 1)


powerset(0)
```



#### 순열

```python
# 재귀
# nPr

arr2 = [1, 2, 3, 4, 5]
N2 = len(arr2)
sel2 = [0] * 3  # 5P3
check2 = [0] * N2

def permutation2(idx):
    if idx == 3:  # 5P3
        print(sel2)

    else:
        for i in range(N2):
            if check2[i] == 0:  # i번째 자리 아직 안썼다면 사용
                sel2[idx] = arr2[i]
                check2[i] = 1  # 사용했다는 표시
                permutation2(idx+1)
                check2[i] = 0  # 다음 반복문을 위해 원상복구

permutation2(0)
```

```python
# swap
arr = [1, 2, 3, 4, 5]
N = 5

def permutation(idx):
    if idx == N:
        print(arr)

    else:
        for i in range(idx, N):
            arr[idx], arr[i] = arr[i], arr[idx]
            permutation(idx + 1)
            arr[idx], arr[i] = arr[i], arr[idx]  # 다음 인덱스에서 사용하기 위해 원상복구

permutation(0)
```

```python
# 비트연산자
arr = [1, 2, 3]
N = 3
sel = [0] * N  # 뽑은 결과를 적음

# check => 10진수 정수
def permutation(idx, check):
    if idx == N:
        print(sel)
        return

    for j in range(N):
        if check & (1 << j): continue  # j번째 원소 사용했다면 다음 index로

        sel[idx] = arr[j]
        print((1<<j), check, check | (1<<j))
        permutation(idx+1, check | (1<<j))  # 일회성 사용이므로 원상복구가 필요없다

permutation(0, 0)

##########################################################################
arr = [1, 2, 3]
N = 3
sel = [0] * N  # 뽑은 결과 받기

def perm(idx, check):
    if idx == N:
        print(sel)

    for j in range(N):
        if check & (1 << j): continue  # 000 & 001 = 000 False

        else:
            sel[idx] = arr[j]
            # check = check | (i << j) 로 저장해버리면 원상복구하는 과정 필요
            perm(idx + 1, check|(1 << j))  # 000 | 001 = 001

perm(0, 0)  # check: 000부터

```



#### N-Queen



## 분할 정복

- 분할: 해결할 문제를 여러 개의 작은 부분으로 나눈다.
- 정복: 나눈 작은 문제를 각각 해결한다.
- 통합: (필요하다면) 해결된 해답을 모은다.



### 예제

#### 거듭제곱

```python
# 반복문 사용한 선형시간 O(n)

def iteraive_power(x, n):  # 2^8 => 7번 연산
    result = 1

    for i in range(1, n+1):
        result *= x

        return result

# 분할 정복 거듭제곱 O(logn)
def Recursive_power(x, n):  # 2^8 => 2*2*2*2 * 2*2 * 2 * 2  => 4번연산?
    if n == 1: return x
    if n % 2 == 0:
        y = Recursive_power(x, n//2)
        return y * y
    else:
        y = Recursive_power(x, (n-1) // 2)
        return y * y * x
```



#### 퀵 정렬(Quick Sort)

- 주어진 배열을 두개로 분할하고 각각 정렬한다.
- 합병 정렬과의 차이점
  - 합병정렬은 그냥 두 부분으로 나누는 반면, 퀵정렬은 분할 할 때 기준 아이템(pivot item)중심으로, 이보다 작은 것은 왼편, 큰 것은 오른편에 위치시킴
  - 각 부분 정렬이 끝난 후 합병정렬은 "합병"이라는 후처리가 필요하지만 퀵정렬은 필요로 하지 않음.

```python
# 호어 파티션
def partition(a, begin, end):
    pivot = (begin + end) // 2  # pivot = 가운데
    L = begin
    R = end
    while L < R:
        while(a[L] < a[pivot] and L < R): L += 1  # L: 오른쪽으로 이동하며 피봇보다 크거나 같은 원소 찾기
        while (a[R] >= a[pivot] and L < R): R -= 1  # R: 왼쪽으로 이동하며 피봇보다 작은 원소 찾기

        if L < R:
            if L == pivot:
                pivot = R
            a[L], a[R] = a[R], a[L]

    a[pivot], a[R] = a[R], a[pivot]  # 피봇 위치 확정

    return R

def quickSort(a, begin, end):
    if begin < end:
        p = partition(a, begin, end)
        quickSort(a, begin, p-1)  # 왼쪽 부분 집합 정렬
        quickSort(a, p+1, end)  # 오른쪽 부분 집합 정렬
```

