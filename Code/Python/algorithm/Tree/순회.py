'''
5 4
2 1 2 4 4 3 4 5
'''
# 전위 순회
def preorder(n):
    if n > 0:
        print(n, end=' ')
        preorder(left[n])
        preorder(right[n])


V, E = map(int, input().split())  # 정점, 간선
edge = list(map(int, input().split()))

left = [0] * (V + 1)  # 부모를 인덱스로 왼쪽 자식 번호 저장
right = [0] * (V + 1)  # 부모를 인덱스로 오른쪽 자식 번호 저장
par = [0] * (V + 1)  # 자식을 인덱스로 부모 번호 저장
root = 0

for i in range(E):
    n1, n2 = edge[i * 2], edge[i * 2 + 1]  # n1 부모, n2 자식 노드
    if left[n1] == 0:  # 왼쪽 자식 없으면
        left[n1] = n2  # 부모를 인덱스로 자식 번호 저장
    else:  # 왼쪽 자식 있으면
        right[n1] = n2  # 부모를 인덱스로 자식 번호 저장
    par[n2] = n1  # 자식을 인덱스로 부모를 저장

# 루트 찾기
for i in range(1, V+1):
    if par[i] == 0:  # 부모노드 없으면 루트
        root = i
        break

preorder(root)