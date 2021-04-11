def cctv(r, c, d):
    for i in d:
        nr = r + dr[i]
        nc = c + dc[i]

        while 0 <= nr < N and 0 <= nc < M and arr[nr][nc] != 6:
            if arr[nr][nc] == 0:
                arr[nr][nc] = 7

            nr += dr[i]
            nc += dc[i]
    return arr


def check(r, c, v):
    max_cnt = 0

    if v == 1:
        direction = [0]
        for i in range(4):
            cnt = 0
            nr = r + dr[i]
            nc = c + dc[i]
            while 0 <= nr < N and 0 <= nc < M and arr[nr][nc] != 6:
                nr += dr[i]
                nc += dc[i]
                cnt += 1

            if max_cnt < cnt:
                max_cnt = cnt
                direction[0] = i  # 방향
        return cctv(r, c, direction)

    elif v == 2:
        direction = [0, 0]
        for i in range(2):
            cnt = 0
            nr1 = r + dr[i]
            nc1 = c + dc[i]
            nr2 = r + dr[i+2]
            nc2 = c + dc[i+2]

            while 0 <= nr1 < N and 0 <= nc1 < M and arr[nr1][nc1] != 6:
                if arr[nr1][nc1] == 0:
                    cnt += 1
                nr1 += dr[i]
                nc1 += dc[i]


            while 0 <= nr2 < N and 0 <= nc2 < M and arr[nr2][nc2] != 6:
                if arr[nr2][nc2] == 0:
                    cnt += 1
                nr2 += dr[i+2]
                nc2 += dc[i+2]

            if max_cnt < cnt:
                max_cnt = cnt
                direction[0] = i  # 방향
                direction[1] = i+2

        return cctv(r, c, direction)

    elif v == 3:
        direction = [0, 0]
        for i in range(4):
            cnt = 0
            nr1 = r + dr[i % 4]
            nc1 = c + dc[i % 4]
            nr2 = r + dr[(i + 1) % 4]
            nc2 = c + dc[(i + 1) % 4]

            while 0 <= nr1 < N and 0 <= nc1 < M and arr[nr1][nc1] != 6:
                if arr[nr1][nc1] == 0:
                    cnt += 1
                nr1 += dr[i % 4]
                nc1 += dc[i % 4]

            while 0 <= nr2 < N and 0 <= nc2 < M and arr[nr2][nc2] != 6:
                if arr[nr2][nc2] == 0:
                    cnt += 1
                nr2 += dr[(i + 1) % 4]
                nc2 += dc[(i + 1) % 4]

            if max_cnt < cnt:
                max_cnt = cnt
                direction[0] = i%4  # 방향
                direction[1] = (i+1)%4

        return cctv(r, c, direction)

    elif v == 4:
        direction = [0, 0, 0]
        for i in range(4):
            cnt = 0
            nr1 = r + dr[i % 4]
            nc1 = c + dc[i % 4]
            nr2 = r + dr[(i + 1) % 4]
            nc2 = c + dc[(i + 1) % 4]
            nr3 = r + dr[(i + 2) % 4]
            nc3 = c + dc[(i + 2) % 4]

            while 0 <= nr1 < N and 0 <= nc1 < M and arr[nr1][nc1] != 6:
                if arr[nr1][nc1] == 0:
                    cnt += 1
                nr1 += dr[i % 4]
                nc1 += dc[i % 4]

            while 0 <= nr2 < N and 0 <= nc2 < M and arr[nr2][nc2] != 6:
                if arr[nr2][nc2] == 0:
                    cnt += 1
                nr2 += dr[(i + 1) % 4]
                nc2 += dc[(i + 1) % 4]

            while 0 <= nr3 < N and 0 <= nc3 < M and arr[nr3][nc3] != 6:
                if arr[nr3][nc3] == 0:
                    cnt += 1
                nr3 += dr[(i + 2) % 4]
                nc3 += dc[(i + 2) % 4]

            if max_cnt < cnt:
                max_cnt = cnt
                direction[0] = i % 4  # 방향
                direction[1] = (i + 1) % 4
                direction[2] = (i + 2) % 4

        return cctv(r, c, direction)

    elif v == 5:
        direction = [0, 1, 2, 3]
        return cctv(r, c, direction)


N, M = map(int, input().split())
ans = 0
arr = []
for i in range(N):
    arr.append(list(map(int, input().split())))

# 우하좌상
dr = [0, 1, 0 , -1]
dc = [1, 0, -1, 0]

for i in range(N):
    for j in range(M):
        if 0 < arr[i][j] < 6:
            row = i
            col = j
            version = arr[i][j]
            arr = check(row, col, version)


for i in range(N):
    for j in range(M):
        if arr[i][j] == 0:
            ans += 1

for i in arr:
    print(*i)
print(ans)
