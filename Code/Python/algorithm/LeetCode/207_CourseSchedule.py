# numCourses = 2
# prerequisites = [[1,0]]

numCourses = 2
prerequisites = [[1,0],[0,1]]

from collections import deque

# 위상 정렬 => 위상 정렬하려면 사이클이 없어야 함, 사이클 존재하면 false
# 모든 노드를 방문하기 전에 큐가 비어 있어 있을 때 사이클 존재 => 사이클이 존재하여 더 이상 진행 불가
# 강의가 노드, 전제 조건이 간선 정보가 된다.
'''
위상 정렬 구현 로직
1. 진입 차수가 0인 노드를 큐에 삽입
2. 큐에서 원소를 꺼내며 해당 원소와 연결된 노드의 진입 차수 - 1
3. 새롭게 진입 차수가 0이 된 노드를 큐에 삽입
사이클이 존재할 경우 모든 노드 방문 전에 큐가 비게 됨(진입 차수가 모두 0이 되기 전에 큐가 비게 됨)
'''

q = deque()
indegree = [0] * numCourses  # 진입 차수
graph = [[] for _ in range((numCourses))]  # 그래프

for i in range(len(prerequisites)):
    graph[prerequisites[i][1]].append(prerequisites[i][0])  # prerequisites[i][1]에서 prerequisites[i][0] 이동
    indegree[prerequisites[i][0]] += 1  # 진입 차수 + 1

# 위상 정렬 구현
# 진입 차수가 0인 노드 큐에 삽입
for i in range(numCourses):
    if indegree[i] == 0:
        q.append(i)

if len(q) == 0 and sum(indegree) != 0:
    print(False)
    exit(0)

while q:
    # 큐에서 원소 빼고 해당 노드와 연결된 노드의 진입 차수 - 1
    currNode = q.popleft()
    for i in graph[currNode]:
        indegree[i] -= 1

        # 진입 차수가 0이 된 노드 큐에 삽입
        if indegree[i] == 0:
            q.append(i)

    if len(q) == 0 and sum(indegree) != 0:
        print(False)
        exit(0)

print(True)


# 참고
# https://freedeveloper.tistory.com/390
# https://spongeb0b.tistory.com/215