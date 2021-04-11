def inorder(n):  # 중위 순회 LVR
    if n > 0:
        inorder(left[n])  # L
        order.append(n)  # V
        inorder(right[n])  # R


for tc in range(1, int(input())+1):
    N = int(input())
    par = [0] * (N+1)  # 부모 노드 번호, 인덱스 = 자식 노드
    left = [0] * (N+1)  # 왼쪽 자식 노드 번호, 인덱스 = 부모 노드
    right = [0] * (N+1)  # 오른쪽 자식 노드 번호, 인덱스 = 부모 노드
    order = []

    for i in range(1, N+1):  # 루트 노드만 있는 경우부터 시작
        par[i] = i//2  # 완전 이진 트리
        if i > 1:
            if i % 2 == 0:
                left[par[i]] = i
            else:
                right[par[i]] = i

    # 노드 값 순서 = 중위 순회 순서
    inorder(1)

    for i in range(len(order)):
        if order[i] == 1:
            root = i+1  # 1번 노드에 들어있는 값
        if order[i] == N//2:
            value = i+1  # N//2 번 노드에 들어있는 값

    print('#{} {} {}'.format(tc, root, value))
