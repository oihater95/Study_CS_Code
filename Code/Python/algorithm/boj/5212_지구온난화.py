from copy import deepcopy

def check(row, col, cnt):
    global flag

    for i in range(4):
        nr = row + dr[i]
        nc = col + dc[i]

        if 0 <= nr < R and 0 <= nc < C:
            if current_map[nr][nc] == '.':
                cnt += 1
        else:
            # 지도 밖 영역은 모두 바다
            cnt += 1

    if cnt >= 3:
        flag = True




R, C = map(int, input().split())
current_map = [ list(input()) for _ in range(R)]
copy_map = deepcopy(current_map)
locations_x = []
locations_y = []

# 델타 이동
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

for i in range(R):
    for j in range(C):
        if current_map[i][j] == 'X':
            flag = False
            check(i, j, 0)
            if flag == True:
                copy_map[i][j] = '.'
            else:
                locations_y.append(i)
                locations_x.append(j)

# 육지가 있는 최소 사각형 출력
for i in range(min(locations_y), max(locations_y)+1):
    for j in range(min(locations_x), max(locations_x)+1):
        print(copy_map[i][j], end='')
    print()
