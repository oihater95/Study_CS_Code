import sys
# 재귀깊이 해제
sys.setrecursionlimit(10 ** 9)

def dfs(x, store):
    # 친구 관계인 정점 리턴(친구 무리 찾기)
    visited[x] = True

    # x와 friends[x]는 친구 관계
    for i in friends[x]:
        if visited[i] == False:
            store.append(i)
            dfs(i, store)

    return store


N, M, k = map(int, input().split())
costs = list(map(int, input().split()))
friends = [[] * N for _ in range(N)]  # 인접리스트
visited = [False] * N  # 방문 확인
ans = []

# 인접리스트 생성
for i in range(M):
    v, w = map(int, input().split())
    friends[v-1].append(w-1)
    friends[w-1].append(v-1)

for i in range(N):
    # 아직 방문하지 않았다면 연결 요소 확인
    if visited[i] == False:
        each = dfs(i, [i])
        temp = 987654321

        # 친구 무리를 사는 최소 비용 찾기
        for j in each:
            if temp > costs[j]:
                temp = costs[j]

        ans.append(temp)  # 각 최소 비용 append

if sum(ans) <= k:
    print(sum(ans))
else:
    print('Oh no')