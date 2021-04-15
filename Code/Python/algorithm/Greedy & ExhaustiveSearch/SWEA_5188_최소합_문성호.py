# 우하
dr = [0, 1]
dc = [1, 0]


def dfs(r, c, result):  # 매개변수로 result을 써서 이전 단계의 result값 활용가능
    global min_value

    if r == N-1 and c == N-1:  # 마지막 위치에 도달
        result += arr[r][c]
        if result < min_value:  # 최소값 갱신
            min_value = result
        return

    if result > min_value:  # 경로의 합이 최소값을 넘으면 더 이상 탐색할 필요 없음
        return

    else:
        for i in range(2):
            nr = r + dr[i]
            nc = c + dc[i]

            if 0 <= nr < N and 0 <= nc < N and arr[nr][nc] != 0:
                result += arr[r][c]
                temp = arr[r][c]
                arr[r][c] = 0  # visited True
                dfs(nr, nc, result)
                arr[r][c] = temp  # visited False
                result -= arr[r][c]  # 이전 값 복구


for tc in range(1, int(input())+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    min_value = 987654321  # 최소값
    result = 0  # 경로 합
    dfs(0, 0, result)  # (0, 0) 시작

    print('#{} {}'.format(tc, min_value))