T = int(input())

for test_case in range(1, T+1):
    N, M = map(int, input().split())  # N X N 배열, M = 회문 길이
    arr = []
    answer = []
    arr_transpose = [[0 for i in range(N)] for j in range(N)]  # 전치행렬 (가로 세로 바꾼 행렬)

    for i in range(N):
        arr.append(list(input()))

    for i in range(N):  # 전치행렬 만들기
        for j in range(N):
            arr_transpose[i][j] = arr[j][i]

    # 가로 회문
    for i in range(N):
        for j in range(N-M+1):
            if arr[i][j:j+M] == arr[i][j:j+M][::-1]:  # 슬라이싱 활용 [::-1] -> reverse
                answer = arr[i][j:j+M]
                break
        if answer:
            break

    # 세로 회문 => 전치행렬을 이용
    for i in range(N):
        for j in range(N-M+1):
            if arr_transpose[i][j:j+M] == arr_transpose[i][j:j+M][::-1]:  # 슬라이싱 활용 [::-1] -> reverse
                answer = arr_transpose[i][j:j+M]
                break
        if answer:
            break

    print('#{} {}'.format(test_case, ''.join(answer)))