T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    coord = [[0 for i in range(10)] for j in range(10)]  # 10 X 10 좌표
    cnt = 0  # 보라색 칸 수

    # 좌표 색칠
    for i in range(N):
        color = list(map(int, input().split()))
        for row in range(color[0], color[2] + 1):
            for col in range(color[1], color[3] + 1):
                if color[4] == 1:  # 빨간색
                    if coord[row][col] == 0:  # 색칠 안되어있으면 빨간색으로 색칠
                        coord[row][col] = 1
                    elif coord[row][col] == 2:  # 파란색 색칠되어있으면 보라색으로
                        coord[row][col] = 3
                else:
                    if coord[row][col] == 0:  # 색칠 안되어있으면 파란색으로 색칠
                        coord[row][col] = 2
                    elif coord[row][col] == 1:  # 빨간색 색칠되어있으면 보라색으로
                        coord[row][col] = 3

    # 전체를 순회하며 보라색 칸 수 세기
    for i in range(10):
        for j in range(10):
            if coord[i][j] == 3:
                cnt += 1
    print('#{} {}'.format(test_case, cnt))
