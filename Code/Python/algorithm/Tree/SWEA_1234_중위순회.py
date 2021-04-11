def inorder(n):  # 중위 순회 LVR
    if n > 0:
        inorder(left[n])  # L
        print(values[n], end='')  # V
        inorder(right[n])  # R


for tc in range(1, 11):
    V = int(input())  # 정점 수
    left = [0] * (V+1)  # 왼쪽 자식 번호, 인덱스 = 부모 노드 번호
    right = [0] * (V+1)  # 오른쪽 자식 번호, 인덱스 = 부모 노드 번호
    values = [0] * (V+1)  # 노드의 값
    for i in range(V):
        node = list(input().split())
        node[0] = int(node[0])
        values[node[0]] = node[1]  # 현재 노드의 값

        if len(node) == 4:  # 왼쪽 자식, 오른쪽 자식 모두 존재
            left[node[0]] = int(node[2])
            right[node[0]] = int(node[3])

        elif len(node) == 3:  # 왼쪽 자식만 존재
            left[node[0]] = int(node[2])

    print('#{}'.format(tc), end=' ')
    inorder(1)  # 루트 노드 번호 = 1
    print()