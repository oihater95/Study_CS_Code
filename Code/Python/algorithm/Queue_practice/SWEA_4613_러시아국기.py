# def perm(idx, row_sum):  # sub_sum으로 가지치기
#     global ans
#
#     if N < row_sum:  # 각 색깔이 차지하는 줄 수의 합이 N보다 크면 제외
#         return
#
#     if idx == 3:  # 흰파빨 모두 할당, row_sum = sel[0] + sel[1] + sel[2]
#         if row_sum < N:  # 모두 할당되었는데 줄 수 모자른 경우 제외
#             return
#
#         if row_sum == N:  # 흰파빨 줄 수의 합이 N일 때 색칠
#             cnt = 0  # 색칠 횟수
#             for i in range(sel[0]):  # 흰색 칠하기 (0번째 row부터 sel[0]만큼)
#                 for j in range(M):
#                     if arr[i][j] != 'W':
#                         cnt += 1
#
#             for i in range(sel[0], sel[0] + sel[1]):  # 흰색 칠하기 (sel[0]번째 row부터 sel[1]만큼)
#                 for j in range(M):
#                     if arr[i][j] != 'B':
#                         cnt += 1
#
#             for i in range(sel[0] + sel[1], N):  # 흰색 칠하기 (sel[0]+sel[1]번째 row부터 끝까지)
#                 for j in range(M):
#                     if arr[i][j] != 'R':
#                         cnt += 1
#
#             if ans > cnt:  # 최소 색칠 횟수
#                 ans = cnt
#         return
#
#     for i in range(1, N-1):  # 최소 한 줄 씩 필요하기 때문에 최소: 1,  최대: N-2
#         sel[idx] = i  # [1, 1, 1] ~ [N-1, N-1, N-1]
#         perm(idx + 1, row_sum + i)
#
#
# for tc in range(1, int(input())+1):
#     N, M = map(int, input().split())  # N x M
#     arr = []
#     sel = [0] * 3  # 흰파빨 각각 몇 줄인지 중복순열 응용
#     ans = 987654321
#     for i in range(N):
#         arr.append(list(input()))
#
#     perm(0, 0)
#     print('#{} {}'.format(tc, ans))



###########################################################
# 순열없이 반복문으로 풀기
for tc in range(1, int(input())+1):
    N, M = map(int, input().split())  # N x M
    arr = []
    ans = 99999999
    for i in range(N):
        arr.append(list(input()))

    # 각 row마다 해당 색이 아닌 칸 수 count
    not_w = [0] * N
    not_b = [0] * N
    not_r = [0] * N

    for i in range(N):
        for j in range(M):
            if arr[i][j] != 'W':
                not_w[i] += 1
            if arr[i][j] != 'B':
                not_b[i] += 1
            if arr[i][j] != 'R':
                not_r[i] += 1


    for i in range(N-2):  # 흰색 줄 최대 N-3번째줄까지 가능, 0번째 row부터 시작
        for j in range(i+1, N-1):  # 파란색 줄 i+1번째 부터 N-2번째까지 가능
            cnt = 0  # 색칠 횟수
            for k in range(i+1):
                cnt += not_w[k]
            for k in range(i+1, j+1):
                cnt += not_b[k]
            for k in range(j+1, N):
                cnt += not_r[k]

            if ans > cnt:
                ans = cnt
    print('#{} {}'.format(tc, ans))

