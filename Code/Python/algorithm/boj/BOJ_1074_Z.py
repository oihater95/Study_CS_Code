# 2차원 배열에 생성해서 숫자 넣으면 메모리초과
# jump 필요 => 시간 초과 방지

def dc(num, row, col):
    global cnt
    if row == r and col == c:
        print(cnt)
        exit(0)

    if num == 1:
        cnt += 1
        return

    # jump => 탐색 범위 안에 없으면 다음 탐색 범위로
    if not(row <= r < row+num and col <= c < col+num):
        cnt += num**2
        return

    n = num // 2
    dc(n, row, col)
    dc(n, row, col+n)
    dc(n, row+n, col)
    dc(n, row+n, col+n)


N, r, c = map(int, input().split())
cnt = 0
dc(2**N, 0, 0)
