# 시간초과
# def dfs(q):
#     global ans
#
#     if q == N:
#         ans += 1
#         return
#
#     for i in range(N):
#         if visited[i] == 0:  # 퀸 존재 확인
#             queens[q] = i  # q번째 row, i번째 col에 퀸 놓기
#             flag = True
#
#             for j in range(q):  # 퀸 놓은 갯수만큼만 확인
#                 # 대각선 체크
#                 if abs(queens[q] - queens[j]) == abs(q - j):
#                     flag = False
#                     break
#             if flag:
#                 visited[i] = 1
#                 dfs(q+1)
#                 visited[i] = 0
#
# N = int(input())
# queens = [0] * N  # 퀸은 1줄에 하나, 인덱스가 row, 값이 col
# visited = [0] * N
# ans = 0
# dfs(0)
# print(ans)

def check(num):
    global ans

    if num == N:  # 퀸 배치 완료
        ans += 1
        return

    for i in range(N):
        if check_col[i] and check_diag1[i+num] and check_diag2[num-i+N-1]:
            check_col[i] = False
            check_diag1[i+num] = False
            check_diag2[num-i+N-1] = False
            check(num+1)
            check_col[i] = True
            check_diag1[i + num] = True
            check_diag2[num - i + N - 1] = True


N = int(input())
check_col = [True] * N  # 열 확인, (행은 인덱스로 나뉘어져 확인할 필요 없음)
check_diag1 = [True] * (N * 2 - 1)  # 대각선 확인 (y = x)
check_diag2 = [True] * (N * 2 - 1)  # 대각선 확인 (y = -x)
ans = 0

check(0)
print(ans)

