T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    arr = [[0 for i in range(N)] for j in range(N)]
    num = 1
    direction = 0

    while num < N**2 + 1:
        if direction % 4 == 0:  # right
            for i in range(direction//4, N - (direction//4)):
                arr[direction//4][i] = num
                num += 1

        elif direction % 4 == 1:  # down
            for i in range((direction//4 + 1), N - (direction//4)):
                arr[i][N - 1 - direction//4] = num
                num += 1

        elif direction % 4 == 2:  # left
            for i in range(N - 2 - (direction//4), (direction//4) - 1, -1):
                arr[N - 1 - direction//4][i] = num
                num += 1

        elif direction % 4 == 3:  # up
            for i in range(N - 2 - (direction//4), (direction//4), -1):
                arr[i][direction//4] = num
                num += 1

        direction += 1

    print('#{}'.format(test_case))
    for i in range(N):
        print(' '.join(map(str, arr[i])))