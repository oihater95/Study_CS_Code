def heap_push(value):
    global heap_size
    heap_size += 1
    heap[heap_size] = value

    c = heap_size
    p = heap_size // 2

    while p and heap[p] > heap[c]:
        heap[p], heap[c] = heap[c], heap[p]
        c = p
        p = c // 2


for tc in range(1, int(input())+1):
    N = int(input())  # 노드의 개수
    heap = [0]  # 인덱스와 노드번호 맞추기
    heap_size = 0
    arr = list(map(int, input().split()))  # 입력
    ans = 0  # 마지막 노드의 조상노드 합

    for v in arr:
        heap_push(v)

    node = N // 2

    while node:
        ans += heap[node]
        node //= 2

    print('#{} {}'.format(tc, ans))
