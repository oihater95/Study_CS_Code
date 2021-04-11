def permutation(idx):  # 순열
    if idx == N:
        p.append(sel[:])  # 깊은 복사로 해야함
        return

    for i in range(N):
        if check[i] == 0:  # i번째 자리 사용 했는지
            sel[idx] = col_index[i]  # idx번째 자리 수에 올 수
            check[i] = 1  # 사용한 것으로 갱신
            permutation(idx+1)  # 다음 자리수로
            check[i] = 0  # 다음 반복문 순회를 위해 원상복구


for tc in range(1, int(input())+1):
    N = int(input())
    arr = []
    check = [0] * N
    sel = [0] * N
    col_index = list(range(N))
    p = []  # col 순열
    min_value = 99999999

    for i in range(N):
        arr.append(list(map(int, input().split())))

    permutation(0)  # 순열

    for i in range(len(p)):
        value = 0  # 각 경우의 수 합
        for j in range(N):
            value += arr[j][p[i][j]]
        if min_value > value:
            min_value = value

    # 겹치지 않는 열 합 중 최소값
    print('#{} {}'.format(tc, min_value))