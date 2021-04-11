# 실패
# .은 빈공간이고 R은 빨강, G는 초록, B는 파랑, P는 보라, Y는 노랑
# 입력으로 주어진 필드는 전부 아래로 떨어진 상태

def puyo(r, c, color, check):  # DFS
    global cnt
    cnt += 1
    visited[r][c] = 1

    for i in range(4):  # 4방향 탐색
        nr = r + dr[i]
        nc = c + dc[i]

        if 0 <= nr < N and 0 <= nc < M and visited[nr][nc] == 0:  # 범위 안
            if arr[nr][nc] == color:
                puyo(nr, nc, color, check)

                if cnt >= 4:  # 연결된 블록 4개 이상
                    # 각 색깔별로 터졌는지 체크
                    if color == 'R':
                        check[0] = 1
                    elif color == 'G':
                        check[1] = 1
                    elif color == 'B':
                        check[2] = 1
                    elif color == 'P':
                        check[3] = 1
                    elif color == 'Y':
                        check[4] = 1
                    # 터진 블록 체크
                    arr[nr][nc] = '0'
                    arr[row][col] = '0'


def gravity(a):
    arr_transpose = [[0 for r in range(N)] for c in range(M)]

    for i in range(N):
        for j in range(M):
            arr_transpose[j][i] = a[i][j]

    for i in range(M):
        for j in range(N):
            if arr_transpose[i][j] == '0':
                arr_transpose[i].pop(j)
                arr_transpose[i].insert(0, '.')

    for i in range(N):
        for j in range(M):
            a[i][j] = arr_transpose[j][i]

    return a



arr = []
combo = 0
# 위에서 부터 시계방향
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]
for i in range(12):
    arr.append(list(input()))
N, M = len(arr), len(arr[0])  # 행, 열

# 시작점
flag = True
while flag:  # 어떤색이든 터졌으면 계속 순회
    visited = [[0] * M for _ in range(N)]  # visited 갱신
    check = [0] * 5  # 색깔별로 터지는지, 동시에 터져도 콤보는 하나 쌓이기 때문에 리스트 사용
    for i in range(N):
        for j in range(M):
            row, col = i, j
            cnt = 0
            if arr[i][j] == 'R':
                puyo(i, j, 'R', check)
            elif arr[i][j] == 'G':
                puyo(i, j, 'G', check)
            elif arr[i][j] == 'B':
                puyo(i, j, 'B', check)
            elif arr[i][j] == 'P':
                puyo(i, j, 'P', check)
            elif arr[i][j] == 'Y':
                puyo(i, j, 'Y', check)

    if 1 in check:  # 어떤색이든 터졌으면 콤보 +1
        combo += 1
    else:
        break

    arr = gravity(arr)

print(combo)
