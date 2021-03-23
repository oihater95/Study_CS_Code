for tc in range(1, int(input())+1):
    N, M = map(int, input().split())  # 큐의 크기, M번 회전
    queue = list(map(int, input().split()))  # 숫자 큐

    for i in range(M):
        queue.append(queue.pop(0))

    print('#{} {}'.format(tc, queue[0]))

    # M = M % N
    # print(queue[M])