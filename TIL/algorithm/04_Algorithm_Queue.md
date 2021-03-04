# Algorithm Queue

## Queue

- FIFO (First In First Out) 구조, 선입선출



### 연산

- enQueue(item) : 큐 뒤쪽(rear 뒤)에 삽입
- deQueue():  큐 앞쪽(front)에서 원소 삭제하고 반환
- createQueue(): 공백 상태의 큐 생성
- isEmpty(): 큐가 공백상태인지 확인하는 연산
- isFull(): 큐가 포화 상태인지 확인하는 연산
- Qpeek(): 큐 앞쪽(front)에서 원소를 반환(삭제X)



### Linear Queue

- 1차원 배열을 이용한 큐
- 큐의 크기 = 배열의 크기
- front: 마지막에 꺼내진 원소의 인덱스
- rear: 저장된 마지막 원소의 인덱스
- 초기상태: front = rear = -1
- 공백상태: front = rear
- 포화상태: rear = n - 1 (n: 큐의 크기)
- 잘못된 포화상태 인식 => 앞에 공간이 있지만 포화상태로 인식
  - 해결방법1: 삽입, 삭제시마다 저장된 원소들 위치를 조정 => 비효율적
  - 해결방법2: 원형 큐 사용
- enQueue => rear += 1, deQueue => front += 1

```python
# 선형 큐
class Queue:
    def __init__(self, n):
        self.front = -1
        self.rear = -1
        self.queue = [0] * n

    def enQueue(self, item):
        if self.isFull(): print('Queue_Full')
        else:
            self.rear += 1
            self.queue[self.rear] = item
            print(self.queue)

    def deQueue(self):
        if self.isEmpty(): print('Queue_Empty')
        else:
            self.front += 1
            elem = self.queue[self.front]
            self.queue[self.front] = 0
            print(self.queue)
            return elem

    def isEmpty(self):
        if self.front == self.rear:
            return True
        else:
            return False

    def isFull(self):
        if self.rear == len(self.queue) - 1:
            return True
        else:
            return False

    def Qpeek(self):
        if self.isEmpty(): print('Queue_Empty')
        else:
            return self.queue[self.front+1]

my_queue = Queue(3)
my_queue.enQueue(1)
my_queue.enQueue(2)
my_queue.enQueue(3)
print('front is ',my_queue.Qpeek())
print('Full? ', my_queue.isFull())
my_queue.deQueue()
my_queue.deQueue()
my_queue.deQueue()
print('Empty? ', my_queue.isEmpty())
# 앞 공간 있지만 Full로 인식 => 해결하려면 큐를 앞으로 당겨와야함(비효율적)
my_queue.enQueue(1)
my_queue.enQueue(2)
>>>
[1, 0, 0]
[1, 2, 0]
[1, 2, 3]
front is  1
Full?  True
[0, 2, 3]
[0, 0, 3]
[0, 0, 0]
Empty?  True
Queue_Full
Queue_Full
```



### Circular Queue

- front = rear = 0 으로 초기화
- Index 순환
  - front, rear가 마지막 인덱스 n-1을 가리킨 후 다음에는 인덱스 0을 가리킴(나머지 연산 활용)
- front는 항상 비워둠 => 공백상태와 포화상태 구분
- 공백상태: front = rear
- 포화상태: rear + 1 = front

```python
# 원형큐
class CircularQueue:
    def __init__(self, n):
        self.front = 0
        self.rear = 0
        self.queue = [0] * n

    def enQueue(self, item):
        if self.isFull(): print('Queue_Full')
        else:
            self.rear = (self.rear + 1) % len(self.queue)
            self.queue[self.rear] = item
            print(self.queue)

    def deQueue(self):
        if self.isEmpty(): print('Queue_Empty')
        else:
            self.front = (self.front + 1) % len(self.queue)
            elem = self.queue[self.front]
            self.queue[self.front] = 0
            print(self.queue)
            return elem

    def isEmpty(self):
        if self.front == self.rear:
            return True
        else:
            return False

    def isFull(self):
        if (self.rear + 1) % len(self.queue) == self.front:
            return True
        else:
            return False

    def Qpeek(self):
        if self.isEmpty(): print('Queue_Empty')
        else:
            return self.queue[self.front+1]

my_queue = CircularQueue(3)
my_queue.enQueue(1)
my_queue.enQueue(2)
my_queue.enQueue(3)
print('front is ',my_queue.Qpeek())
print('Full? ', my_queue.isFull())
my_queue.deQueue()
my_queue.deQueue()
my_queue.deQueue()
print('Empty? ', my_queue.isEmpty())
# 원형 큐는 index가 범위 넘어가면 다시 처음으로 돌아옴(선형 큐와의 차이점)
my_queue.enQueue(1)
my_queue.enQueue(2)
>>>
[0, 1, 0]
[0, 1, 2]
Queue_Full
front is  1
Full?  True
[0, 0, 2]
[0, 0, 0]
Queue_Empty
Empty?  True
[1, 0, 0]
[1, 2, 0]
```



### Linked List (연결 큐)

- 데이터 + 다음 값을 참조하고 있는 주소
- 맨 끝 데이터는 주소 대신 None(Null)을 들고있음
- front: 첫번째 노드를 가리키는 링크
- rear: 마지막 노드를 가리키는 링크
- 초기상태: front = rear = None(Null)
- 공백상태: front = rear = None(Null)
- 포화개념 없음, 시스템이 허용하는 한 삽입가능
- 메모리상 공간활용도 높음, 단방향
- 큐의 원소 = 단순 연결 리스트의 노드
- 큐 원소의 순서 = 노드 연결 순서



### Priority Queue (우선순위 큐)

- 우선순위를 가진 항목들을 저장하는 큐
- FIFO 구조 X, 우선순위 높은 순서대로 Out
- 원소 삽입 시 우선 순위를 비교하여 적절한 위치에 삽입
- 가장 앞 (front, [0])이 최고 우선 순위
- 문제점: 삽입이나 삭제 연산 시 원소 재배치로 인한 시간, 메모리 효율성 낮음
- 활용: 버퍼
  - 버퍼: 데이터 전송 시 일시적으로 데이터 보관하는 메모리 영역



##  BFS(Breadth First Search) 너비 우선 탐색

- 인접한 정점들을 먼저 차례로 방문한 후 방문한 정점을 시작점으로 하여 다시 인접한 정점들을 차례적으로 방문
- FIFO, Queue 구조 이용

```python
'''
입력
8 7
1 2
1 3
2 4
2 5
3 7
4 6
5 6
6 7
'''
# pop한 후 visited 갱신
def BFS(v):  # v => 탐색 시작점
    queue.append(v)
    while queue:
        print('queue: ', queue)
        temp = queue.pop(0)
        if not visited[temp]:
            visited[temp] = True
        path.append(temp)
        print('visited: ', visited)
        print('path: ', path)

        for i in range(1, N+1):
            if arr[temp][i] and not visited[i] and (i not in queue):  # 인접해있고 아직 방문하지 않은 노드
                queue.append(i)

        print()


G, N = map(int, input().split())  # 간선 수, 노드 수
arr = [[0]*(N+1) for _ in range(N+1)]  # 노드 번호가 1부터 시작
visited = [False] * (N+1)
queue = []
path = []  # 경로

# 인접행렬
for i in range(G):
    A, B = map(int, input().split())
    arr[A][B], arr[B][A] = 1, 1

BFS(1)  # 탐색 시작점: 1
>>>
queue:  [1]
visited:  [False, True, False, False, False, False, False, False]
path:  [1]

queue:  [2, 3]
visited:  [False, True, True, False, False, False, False, False]
path:  [1, 2]

queue:  [3, 4, 5]
visited:  [False, True, True, True, False, False, False, False]
path:  [1, 2, 3]

queue:  [4, 5, 7]
visited:  [False, True, True, True, True, False, False, False]
path:  [1, 2, 3, 4]

queue:  [5, 7, 6]
visited:  [False, True, True, True, True, True, False, False]
path:  [1, 2, 3, 4, 5]

queue:  [7, 6]
visited:  [False, True, True, True, True, True, False, True]
path:  [1, 2, 3, 4, 5, 7]

queue:  [6]
visited:  [False, True, True, True, True, True, True, True]
path:  [1, 2, 3, 4, 5, 7, 6]
```

