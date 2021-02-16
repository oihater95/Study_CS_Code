# 선택정렬
T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    for i in range(N-1):
        min_idx = i
        for j in range(i+1, N):  # i+1 부터 끝까지 최소값 찾기
            if arr[min_idx] > arr[j]:
                min_idx = j  # 최소값 인덱스만 갱신
        arr[i], arr[min_idx] = arr[min_idx], arr[i]  # 최소값과 i번째 수 교환

    print('#{} {}'.format(test_case, ' '.join(map(str, arr))))