# Algorithm_Stack

## Stack

- 선형구조 (일대일)
- 자료를 삽입하거나 꺼낼 수 있다.
- 후입선출 (LIFO: Last In First Out)



### 연산

- top(): 스택에서 마지막에 삽입된 원소 위치

- push(): 삽입 (List append)
- pop(): 삭제
- isEmpty(): 공백확인, 비어있으면 True 아니면 False
- peek(): top에 있는 item(원소)반환 => 꺼내지 않고 값만 확인



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