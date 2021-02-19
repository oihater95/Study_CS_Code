T = int(input())

for test_case in range(1, T+1):
    N, K = map(int, input().split())
    puzzle = [list(map(int, input().split())) for _ in range(N)]
    ans = 0

    for i in range(N):
        cnt = 0
        # 행 검사
        for j in range(N):
            if puzzle[i][j] == 1:
                cnt += 1
            if puzzle[i][j] == 0 or j == N-1:  # else로 두면 j = N-1일 때 카운트가 안됨
                # 벽을 만났을 때 그 동안 쌓아온 cnt값이 K이면 들어갈 수 있다.
                if cnt == K:
                    ans += 1
                cnt = 0

        # 열 검사
        for j in range(N):
            if puzzle[j][i] == 1:
                cnt += 1
            if puzzle[j][i] == 0 or j == N-1:
                if cnt == K:
                    ans += 1
                cnt = 0

    print('#{} {}'.format(test_case, ans))


######################################################################
# padding 활용 => j == N-1일 때 예외조건 안써도 됨

T = int(input())

for test_case in range(1, T + 1):
    N, K = map(int, input().split())
    puzzle = [list(map(int, input().split())) + [0] for _ in range(N)]  # 0으로 padding
    puzzle.append([0] * (N+1))
    ans = 0

    for i in range(N):
        cnt = 0
        # 행 검사
        for j in range(N+1):  # padding이 생겨 범위 늘림
            if puzzle[i][j]:
                cnt += 1
            else:  # padding이 있어 else써도 j == N-1 카운트
                # 벽을 만났을 때 그 동안 쌓아온 cnt값이 K이면 들어갈 수 있다.
                if cnt == K:
                    ans += 1
                cnt = 0

        # 열 검사
        for j in range(N):
            if puzzle[j][i]:
                cnt += 1
            else:
                if cnt == K:
                    ans += 1
                cnt = 0

    print('#{} {}'.format(test_case, ans))
