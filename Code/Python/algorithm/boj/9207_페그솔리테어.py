import copy
# 델타이동 상우하좌
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]


def dfs(arr, count):
    global min_cnt, min_o
    canGo = False  # flag False => 이동 불가

    for i in range(5):
        for j in range(9):
            if arr[i][j] == 'o':
                # 4방향 탐색
                for k in range(4):
                    # 인접한 칸
                    nr = i + dr[k]
                    nc = j + dc[k]

                    # 인접한 칸의 다음칸 (점프해서 도착하는 칸)
                    nnr = i + dr[k] * 2
                    nnc = j + dc[k] * 2

                    # 점프해서 도착할 칸의 범위가 판 안쪽일 때
                    if 0 <= nnr <= 4 and 0 <= nnc <= 8:
                        # 점프해서 도착할 칸이 점프가능한 칸 일때
                        if arr[nr][nc] == 'o' and arr[nnr][nnc] == '.':
                            canGo = True  # flag True => 이동 가능
                            # 얕은 복사 주의!! arr 원본은 바뀌면 안됨
                            temp_arr = copy.deepcopy(arr)
                            # 핀 이동
                            temp_arr[i][j] = '.'
                            temp_arr[nr][nc] = '.'
                            temp_arr[nnr][nnc] = 'o'
                            dfs(temp_arr, count + 1)  # 1회 이동
    # 더 이상 이동 불가
    if canGo == False:
        o_cnt = 0  # o개수 세기
        for i in range(5):
            for j in range(9):
                if arr[i][j] == 'o':
                    o_cnt += 1
        # 최소 o 일 때 갱신
        if min_o > o_cnt:
            min_o = o_cnt
            min_cnt = count

        # o개수 같지만 최소 이동 횟수일 때 갱신
        elif min_o == o_cnt and min_cnt > count:
            min_cnt = count

    return


n = int(input())
for tc in range(n):
    min_cnt = 9876541321  # 최소 이동 횟수
    min_o = 8  # 최소 o 개수
    adj = [list(input()) for _ in range(5)]

    if tc == n-1:
        pass
    elif tc != n-1 and input() == '\n':
        pass

    dfs(adj, 0)  # 이동 횟수를 파라미터로 넣어줌(백트래킹)
    print(min_o, min_cnt)

