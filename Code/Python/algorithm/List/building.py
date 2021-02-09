def max_func(*args):
    arr = list(args)
    max_value = arr[0]

    for i in range(1, len(arr)):
        if max_value < arr[i]:
            max_value = arr[i]

    return max_value

# 건물 4개씩 정렬하는 방법도 있음

for test_case in range(1, 11):
    T = int(input())
    ans = 0
    apartments = list(map(int, input().split()))
    if apartments[0] > max_func(apartments[1], apartments[2]):
        ans += apartments[0] - max_func(apartments[1], apartments[2])

    if apartments[1] > max_func(apartments[0], apartments[2], apartments[3]):
        ans += apartments[1] - max_func(apartments[0], apartments[2], apartments[3])

    if apartments[-2] > max_func(apartments[-1], apartments[-3], apartments[-4]):
        ans += apartments[-2] - max_func(apartments[-1], apartments[-3], apartments[-4])

    if apartments[-1] > max_func(apartments[-2], apartments[-3]):
        ans += apartments[-1] - max_func(apartments[-2], apartments[-3])

    for i in range(2, T-2):
        if apartments[i] == 0:
            continue
        else:
            if apartments[i] > max_func(apartments[i - 2], apartments[i - 1], apartments[i + 1], apartments[i + 2]):
                ans += apartments[i] - max_func(apartments[i - 2], apartments[i - 1], apartments[i + 1],
                                                apartments[i + 2])

    print('#{} {}'.format(test_case, ans))