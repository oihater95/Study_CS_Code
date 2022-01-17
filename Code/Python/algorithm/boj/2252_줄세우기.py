# 위상정렬 풀이
from collections import deque

N, M = map(int, input().split())
# 몇 개의 노드로 부터 연결되어있는지
inDegree = [0] * (N+1)
inDegree[0] = -1
# 해당 인덱스 번호 노드는 어느 노드로 연결되는지
direct = [[] for _ in range(N+1)]
que = deque()

for i in range(M):
    A, B = map(int, input().split())
    inDegree[B] += 1
    direct[A].append(B)

for i in range(1, N+1):
    if inDegree[i] == 0:
        que.append(i)

while que:
    q = que.popleft()
    print(q, end=' ')
    # 인덱스 번호 노드로 부터 시작하는 간선 제거
    for d in direct[q]:
        inDegree[d] -= 1
        # 해당 번호 노드로 들어오는 간선 모두 제거된 노드를 큐에 추가
        if inDegree[d] == 0:
            que.append(d)