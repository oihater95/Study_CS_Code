import sys
from copy import deepcopy

sys.setrecursionlimit(300000)

# DFS
def puyo_count(r, c, color, cnt):  # 한 턴에 몇 뿌요인지 세는 함수
    arr_copy2[r][c] = '0'

    for i in range(4):
        nr, nc = r + dr[i], c + dc[i]
        if 0 <= nr < 12 and 0 <= nc < 6 and arr_copy2[nr][nc] == color:
            cnt = puyo_count(nr, nc, color, cnt + 1)

    return cnt


def puyo(r, c, color):  # 뿌요된 블럭 터뜨리기
    arr_copy[r][c] = '0'

    for i in range(4):
        nr, nc = r + dr[i], c + dc[i]
        if 0 <= nr < 12 and 0 <= nc < 6 and arr_copy[nr][nc] == color:
            puyo(nr, nc, color)


def gravity():  # 빈 공간에 중력 작용
    for j in range(6):
        for i in range(12):
            if arr_copy[i][j] == '0':
                up = arr_copy[0][j]
                # i번째 전까지 세로배열을 한 줄씩 아래로 밀고 i번째 원소는 0이기에 맨위로 보내서 . 처리
                for k in range(i):
                    down = arr_copy[k + 1][j]
                    arr_copy[k + 1][j] = up
                    up = down
                arr_copy[0][j] = '.'

# M x N
M = 12
N = 6
arr = [list(input()) for _ in range(M)]
arr_copy = deepcopy(arr)
combo = 0
# 상우하좌 델타이동
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

while True:
    arr_copy2, check = deepcopy(arr_copy), 0
    for i in range(M):
        for j in range(N):
            if arr_copy[i][j] in 'RGBPY':
                if puyo_count(i, j, arr_copy[i][j], 1) >= 4:
                    # 4 뿌요 이상이면 블럭들 터뜨리고 check = 1
                    puyo(i, j, arr_copy[i][j])
                    check = 1
    gravity()
    if check == 0:
        break
    combo += 1

print(combo)