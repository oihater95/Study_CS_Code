def perm(idx, sub_sum):  # 인덱스와 중간합
    global ans
    # 유망성 검사 아래의 조건문에 걸리게 되면 이후 작업은 의미 없음
    if sub_sum > N:
        return

    if idx == 3:
        if sub_sum == N:
            cnt = 0
            start = sel[0]
            start2 = start + sel[1]

            # 흰색 칠하기, cnt = 색깔 칠한 횟수
            for i in arr[:start]:
                for j in i:
                    if j != 'W':
                        cnt += 1
            # 파란색
            for i in arr[start:start2]:
                for j in i:
                    if j != 'B':
                        cnt += 1
            # 빨간색
            for i in arr[start2:]:
                for j in i:
                    if j != 'R':
                        cnt += 1

            if ans > cnt:
                ans = cnt
        return

    # 중복순열 응용
    for i in range(1, N-1):  # 각각 1줄씩은 보장
        sel[idx] = i
        perm(idx+1, sub_sum + i)


for tc in range(1, int(input())+1):
    N, M = map(int, input().split())  # N x M
    arr = []
    sel = [0] * 3  # 흰 파 빨 몇 줄인지, 중복순열
    ans = 987654321
    for i in range(N):
        arr.append(list(input()))

    perm(0, 0)
    print('#{} {}'.format(tc, ans))

###############################################################
# W, B, R 아닌 갯수를 세기 => 각 라인별로 각각의 색이 아닌 것이 몇 칸인지 (누적합 이용)
# 예시 첫번째 줄 W: 2, B: 5, R: 3 => 흰색 아닌 칸이 2칸, 파랑 아닌 칸 5칸, 빨강 아닌 칸 3칸





for tc in range(1, int(input())+1):
    N, M = map(int, input().split())  # N x M
    flag = [input() for _ in range(N)]  # 리스트 조회만 할 것이기 때문에 input()째로 받음
    W = [0] * N  # 흰색과 다른 색 카운트
    B = [0] * N  # 파란색과 다른 색 카운트
    R = [0] * N  # 빨간색과 다른 색 카운트

    # 행을 보면서 다른 색깔의 수를 카운팅
    for i in range(N):
        for j in range(N):
            # 각 줄마다 모든 색 카운트를 해야하기 때문에 if만 사용
            if flag[i][j] != 'W':
                W[i] += 1
            if flag[i][j] != 'B':
                W[i] += 1
            if flag[i][j] != 'R':
                W[i] += 1

    # 누적합
    for i in range(1, N):
        W[i] += W[i-1]
        B[i] += B[i-1]
        R[i] += R[i-1]

    ans = 987654321

    # 각각의 색별로 한줄 이상은 확보해야하기 때문에 N-2까지만
    for i in range(N-2):
        for j in range(i+1, N-1):
            w_cnt = W[i]
            b_cnt = B[j] - B[i]  # i까지는 흰색이 칠해져있음
            r_cnt = R[N-1] - B[j]  # j까지는 파란색 칠해져있음

            if ans > w_cnt + b_cnt + r_cnt:
                ans = w_cnt + b_cnt + r_cnt

    print('#{} {}'.format(tc, ans))

################################################################