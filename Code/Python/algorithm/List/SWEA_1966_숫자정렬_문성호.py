def my_max(arr):
    max_value = arr[0]
    for i in range(1, len(arr)):
        if max_value < arr[i]:
            max_value = arr[i]
    return max_value


T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    numbers = list(map(int, input().split()))

    # Bubble Sort
    for i in range(N-1, 0, -1):
        for j in range(i):
            if numbers[j] > numbers[j+1]:
                numbers[j], numbers[j+1] = numbers[j+1], numbers[j]

    print('#{} {}'.format(test_case, ' '.join(map(str, numbers))))

    # Counting Sort
    cnt = [0] * (my_max(numbers)+1)
    tmp = [0] * N
    for i in range(N):  # 카운트 리스트
        cnt[numbers[i]] += 1

    for i in range(1, len(cnt)):  # 누적합
        cnt[i] += cnt[i-1]

    for i in range(N-1, -1, -1):
        tmp[cnt[numbers[i]] - 1] = numbers[i]
        cnt[numbers[i]] -= 1

    print('#{} {}'.format(test_case, ' '.join(map(str, tmp))))