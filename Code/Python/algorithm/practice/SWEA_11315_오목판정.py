def check():
    for i in range(N):
        for j in range(N):
            # 현재위치
            if omok[i][j] == 'o':
                for k in range(4):
                    nr = i
                    nc = j
                    cnt = 1
                # 범위안에 들어가는지, 다음 돌도 o인지 확인
                    while nr + dr[k] >= 0 and nr + dr[k] < N and nc + dc[k] >= 0 and nc + dc[k] < N and omok[nr+dr[k]][nc+dc[k]] == 'o':
                        cnt += 1
                        nr += dr[k]
                        nc += dc[k]

                        if cnt >= 5:
                            return 'YES'

    return 'NO'
# 우부터 시계방향(우, 우하, 하, 좌하만 나머지는 겹칩)
# 델타이동
dr = [0, 1, 1, 1]  # x축 방향
dc = [1, 1, 0, -1]  # y축 방향

T = int(input())

for test_case in range(1, T+1):
    N = int(input())  # 오목판 크기
    omok = [input() for _ in range(N)]
    print('#{} {}'.format(test_case, check()))