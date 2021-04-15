def permutation(idx):  # 순열
    if idx == N-1:  # 순열 인덱스 모두 채움
        temp = sel[:]  # 깊은 복사하지 않으면 마지막 순열만 들어감(list => mutable)
        perm.append(temp)

    else:
        for i in range(N-1):  # 순열 채우기
            if check[i] == 0:  # area의 i번째 인덱스 사용하지 않았다면
                sel[idx] = area[i]  # 순열 idx번째 인덱스에 area[i] 넣기
                check[i] = 1  # 사용 체크
                permutation(idx+1)  # 순열 idx+1번째로
                check[i] = 0  # 복구


for tc in range(1, int(input())+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    min_value = 987654321
    perm = []  # 순열 리스트
    area = list(range(1, N))
    sel = [0] * (N-1)  # 순열
    check = [0] * (N-1)  # area 사용 체크
    permutation(0)

    for i in range(len(perm)):
        battery = 0  # 배터리 사용량
        idx = 0  # 1에서 출발(index = 0)
        for j in perm[i]:  # ex) [1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1] ...
            battery += arr[idx][j]  # idx(출발지) -> j(도착지)로 갈 때 배터리 사용량
            idx = j  # 출발지 갱신
        battery += arr[idx][0]  # 마지막 도착지에서 1번 사무실로

        if min_value > battery:  # 최소값 갱신
            min_value = battery

    print('#{} {}'.format(tc, min_value))
