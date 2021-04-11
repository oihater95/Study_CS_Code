for tc in range(1, int(input())+1):
    N, M, L = map(int, input().split())  # 노드 개수, 리프 노드 개수, 찾을 노드 번호
    tree = [0] * (N+1)
    par = [0] * (N+1)  # 부모 노드 번호, 인덱스 = 자식 노드

    for i in range(M):  # 리프 노드 값 넣기
        node, value = map(int, input().split())
        tree[node] = value

    for i in range(1, N+1):
        par[i] = i//2  # 완전 이진 트리

    for i in range(N, 0, -1):  # 리프 노드부터 넣기 위해 역순으로
        tree[par[i]] += tree[i]  # 부모 노드에 자식 노드 값 더하기

    print('#{} {}'.format(tc, tree[L]))