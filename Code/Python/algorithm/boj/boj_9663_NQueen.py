def check(x):  # cnt번째 여왕까지 서로 안 겹치는 지 확인
    for i in range(x):  # cnt번째 여왕까지 확인, 그 뒤는 아직 안 놓았음
        # queens[i] == queens[x] => 열 겹치는 지 확인, 행은 겹칠 일 없음 하나의 idx에 하나의 value만 가지니까
        # abs(queens[x] - queens[i])(열 차이) == x - i(행 차이) => 대각선 y = x(음수), y = -x(양수) 확인
        if queens[i] == queens[x] or abs(queens[x] - queens[i]) == x - i:
            return False
    return True


def dfs(cnt):  # cnt = 여왕 수
    global result

    if cnt == n:
        result += 1

    else:
        for i in range(n):
            queens[cnt] = i  # cnt 행, i 열에 cnt번째 여왕 놓기

            if check(cnt):  # cnt번째 여왕까지 확인
                dfs(cnt + 1)  # 다음 여왕 놓기


n = int(input())
result = 0
queens = [0] * n  # idx가 row, value가 col
dfs(0)
print(result)