for tc in range(1, int(input())+1):
    # 상우하좌
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    control = list(input())
    now_dir = 0 # 위
    location = [0, 0]  # 현재위치 (x,y)
    trace = [location[:]]  # 자취
    for dir in control:
        if dir == 'F':
           location[0] += dx[now_dir]
           location[1] += dy[now_dir]

        elif dir == 'B':
            location[0] -= dx[now_dir]
            location[1] -= dy[now_dir]

        elif dir == 'L':
            if now_dir == 0:
                now_dir = 3
            else:
                now_dir -= 1

        elif dir =='R':
            if now_dir == 3:
                now_dir = 0
            else:
                now_dir += 1
        trace.append(location[:])

    sort_x = sorted(trace, key=lambda x: x[0])
    sort_y = sorted(trace, key=lambda x: x[1])
    width = sort_x[-1][0] - sort_x[0][0]
    height = sort_y[-1][1] - sort_y[0][1]
    print(width * height)