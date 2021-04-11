for tc in range(1, int(input())+1):
    N = int(input())  # 노드의 개수
    tree = [0]  # 인덱스와 노드번호 맞추기
    par = [0] * (N+1)
    arr = list(map(int, input().split()))  # 입력
    ans = 0  # 마지막 노드의 조상노드 합

    for i in range(1, N+1):
        par[i] = i//2  # 부모 노드 번호, 인덱스 = 자식 노드

    while arr:
        tree.append(arr.pop(0))  # 마지막 노드에 추가
        node_num = len(tree)-1  # 순서가 정해지지 않은 노드 번호
        while tree[node_num] < tree[par[node_num]]:  # 부모노드가 자식노드보다 클 경우 두 노드를 스위치
            tree[node_num], tree[par[node_num]] = tree[par[node_num]], tree[node_num]
            node_num = par[node_num]  # 노드 번호 갱신

    node = len(tree)-1  # 마지막 노드(현재)
    while tree[par[node]] != 0:  # 부모노드가 루트일때 까지
        ans += tree[par[node]]  # 현재 노드의 부모 노드 더하기
        node = par[node]  # 현재 노드를 부모 노드로 갱신

    print('#{} {}'.format(tc, ans))
