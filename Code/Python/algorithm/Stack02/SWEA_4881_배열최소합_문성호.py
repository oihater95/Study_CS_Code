def permutation(idx):  # 순열dfs, idx행
    global value, min_value
    if value > min_value:  # 더하는 도중에 min_value보다 크면 비교 의미없음 => 안하면 시간초과
        return
    if idx == N:  # 모든 행 순회
        if value < min_value:  # 최소값 갱신
            min_value = value
            return

    for j in range(N):
        if check[j] == 0:  # j번째 열 사용했는지 0: 미사용, 1: 사용
            value += arr[idx][j]  # idx행의 사용 안 한 열 더하기
            check[j] = 1  # 사용한 것으로 갱신
            permutation(idx+1)  # 다음 행으로
            # 다음 반복문 순회를 위해 원상복구
            value -= arr[idx][j]
            check[j] = 0


for tc in range(1, int(input())+1):
    N = int(input())
    arr = []
    check = [0] * N
    min_value = 9 * N  # 가장 큰 경우
    value = 0

    for i in range(N):
        arr.append(list(map(int, input().split())))

    permutation(0)  # 순열

    # 겹치지 않는 열 합 중 최소값
    print('#{} {}'.format(tc, min_value))