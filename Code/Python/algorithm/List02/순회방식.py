arr = [[1, 2, 3, 4],
       [5, 6, 7, 8],
       [9, 10, 11, 12]
       ]

N = 3  # 행의 길이
M = 4  # 열의 길이

# 마이너스 인덱스 지양
# 행 우선순회
for i in range(N):
    for j in range(M):
        print(arr[i][j])

# 열 우선순회
for j in range(M):
    for i in range(N):
        print(arr[i][j])

# 행 우선순회 역순
for i in range(N):
    for j in range(M-1, -1, -1):
        print(arr[i][j])

# 열 우선순회 역순
for j in range(M):
    for i in range(N-1, -1, -1):
        print(arr[i][j])


# 지그재그 순회
for i in range(N):
    for j in range(M):
        print(arr[i][j + (M-1-2*j) * (i%2)])

##############################################################333
# 상하좌우 델타 접근(4방향 탐색), 시작점은 행렬의 중심
arr2 = [[1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
        ]
r, c = 1, 1  # (r, c) => 행렬의 중심점
dr = [0, 0, -1, 1]  # dx, 좌우 이동
dc = [-1, 1, 0, 0]  # dy, 상하 이동

for i in range(4):
    nr = r + dr[i]  # next row
    nc = c + dc[i]  # next column

    print(arr2[nr][nc])  # 상하좌우 출력  2846

# 범위 벗어나도 파이썬은 마이너스 인덱스로 인식하여 에러가 안남
r2, c2 = 0, 1
for i in range(4):
    nr2 = r2 + dr[i]  # next row
    nc2 = c2 + dc[i]  # next column

    # 범위 벗어났을 경우 if문으로 아무것도 안하고 넘기기기
    # if nr2 < 0 or nr >= len(arr2) or nc < 0 or nc >= len(arr2[i]): continue
    print(arr2[nr2][nc2])  # 상하좌우 출력  8513


##################################################################
# 전치 행렬
arr3 = [[1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
        ]

for i in range(len(arr3)):
    for j in range(len(arr3[i])):
        if i < j:
            arr3[i][j], arr3[j][i] = arr3[j][i], arr3[i][j]