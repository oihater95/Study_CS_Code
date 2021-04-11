# 시간 초과
V = int(input())
par = [0] * (V+1)
nodes = list(range(1, V+1))
leaves = []
cnt = 0  # 말 움직인 횟수
# 부모-자식 관계
for i in range(V-1):
    a, b = map(int, input().split())

    if a == 1 or b == 1:  # 루트 노드 주어질 때
        if a == 1:
            par[b] = 1
        elif b == 1:
            par[a] = 1

    else:  # 루트 노드가 아닌 노드들
        if par[a] != 0:
            par[b] = a
        elif par[b] != 0:
            par[a] = b

# 리프 노드 찾기
for i in range(len(nodes)):
    if nodes[i] not in par:
        leaves.append(nodes[i])

while leaves:
    node_num = leaves.pop()  # 말 움직일 노드 번호
    while node_num != 1:  # 루트 노드에 도착할 때 까지
        node_num = par[node_num]  # 부모 노드로 이동
        cnt += 1  # 이동 횟수 갱신

if cnt % 2:
    print('Yes')
else:
    print('No')

#############################################################
# 메모리 초과
def dfs(n):
    global cnt
    if n == 1:
        return
    else:
        cnt += 1
        for i in range(1, len(arr)):
            if arr[n][i] == 1:
                arr[n][i] = 1
                n = i
                dfs(n)
                break

V = int(input())
arr = [[0 for _ in range(V+1)] for a in range(V+1)]
cnt = 0
leaves = []
# 인접행렬 -> 인접리스트로 바꿔보기
for i in range(V-1):
    a, b = map(int, input().split())
    arr[a][b] = 1
    arr[b][a] = 1

# 리프 노드 찾기
for i in range(V+1):
    node_cnt = 0
    for j in range(V+1):
        if arr[i][j] == 1:
            node_cnt += 1

    if node_cnt == 1:
        leaves.append(i)

for leaf in leaves:
    dfs(leaf)

if cnt % 2:
    print('Yes')
else:
    print('No')