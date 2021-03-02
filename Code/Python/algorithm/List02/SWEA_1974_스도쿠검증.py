T = int(input())

for test_case in range(1, T+1):
    arr = [list(map(int, input().split())) for _ in range(9)]
    row = [[0] * 9 for _ in range(9)]  # 가로 검사
    col = [[0] * 9 for _ in range(9)]  # 세로 검사
    square = [[0] * 9 for _ in range(9)]  # 사각형 검사
    ans = 1

    for i in range(9):  # 스도쿠 가로 검사 & 세로 검사, 각 숫자가 1개씩 있는지
        for j in range(9):
            row[i][arr[i][j]-1] += 1
            col[i][arr[j][i]-1] += 1

    for i in range(9):  # 스도쿠 square 검사, 각 3*3상자에 숫자가 1개씩 있는지
        for j in range(3):
            for k in range(3):
                square[i][arr[(3*(i//3)) + j][k]-1] += 1

    for i in range(9):  # 각 검사를 순회하며 1~9까지 숫자가 1개가 아닌 것이 있으면 0
        for j in range(9):
            if row[i][j] != 1:
                ans = 0
            if col[i][j] != 1:
                ans = 0
            if square[i][j] != 1:
                ans = 0

    print('#{} {}'.format(test_case, ans))