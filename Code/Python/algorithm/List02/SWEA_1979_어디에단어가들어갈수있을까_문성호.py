T = int(input())

for test_case in range(1, T+1):
    N, K = map(int, input().split())
    arr = []
    cnt = 0  # K칸이 들어갈 수 있는 자리 수

    for i in range(N):
        arr.append(list(map(int, input().split())))  # 퍼즐

    for i in range(N):
        cnt_row = 0  # 가로 몇 칸인지 카운트
        cnt_col = 0  # 세로 몇 칸인지 카운트

        for j in range(N):
            # 행 순회
            if arr[i][j]:  
                cnt_row += 1  # 해당 칸 1이면 칸 수 +1
                if j == N-1 and cnt_row == K:  # 해당 행의 끝 칸이고 칸 수 = K이면 자리 수 +1
                    cnt += 1
            else:  # 해당 칸 0
                if cnt_row == K:  # 이전 칸에서 칸 수 = K이면 자리 수 +1 
                    cnt += 1
                cnt_row = 0  # 해당 칸 0 -> 칸 수 0으로 갱신
            # 열 순회
            if arr[j][i]:
                cnt_col += 1  # 해당 칸 1이면 칸 수 +1
                if j == N-1 and cnt_col == K:  # 해당 열의 끝 칸이고 칸 수 = K이면 자리 수 +1
                    cnt += 1
            else:  # 해당 칸 0
                if cnt_col == K:  # 이전 칸에서 칸 수 = K이면 자리 수 +1
                    cnt += 1
                cnt_col = 0  # 해당 칸 0 -> 칸 수 0으로 갱신

    print('#{} {}'.format(test_case, cnt))