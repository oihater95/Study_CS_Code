def inorder(n, num):  # n 노드 번호, num 노드의 값
    if n * 2 <= N:
        num = inorder(n*2, num)
    tree[n] = num
    num += 1
    if n * 2 + 1 <= N:
        num = inorder(n*2+1, num)
        return num  # 다시 올라갈 때 num 값을 들고감
        # num = inorder( , num)으로 돌아가서 num = return num으로 num 값 갱신


for tc in range(1, int(input())+1):
    N = int(input())
    tree = [0] * (N+1)  # 부모 노드 번호, 인덱스 = 자식 노드
    # 노드 값 순서 = 중위 순회 순서
    inorder(1, 1)

    print('#{} {} {}'.format(tc, tree[1], tree[N//2]))
