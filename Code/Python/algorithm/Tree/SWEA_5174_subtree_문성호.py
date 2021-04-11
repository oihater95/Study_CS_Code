def preorder(num):  # 전위 순회
    global cnt
    if num > 0:
        cnt += 1  # V 방문시 카운트
        preorder(left[num])
        preorder(right[num])


for tc in range(1, int(input())+1):
    E, N = map(int, input().split()) # 간선 수, 루트 노드 번호
    V = E + 1  # 정점 수
    tree = list(map(int, input().split()))
    left = [0] * (V+1)  # 왼쪽 자식 노드 번호, 인덱스 = 부모 노드
    right = [0] * (V+1)  # 오른쪽 자식 노드 번호, 인덱스 = 부모 노드
    cnt = 0  # 노드 개수 세기

    for i in range(E):
        p, c = tree[2*i], tree[2*i+1]
        if left[p] == 0:
            left[p] = c
        else:
            right[p] = c

    preorder(N)
    print('#{} {}'.format(tc, cnt))
