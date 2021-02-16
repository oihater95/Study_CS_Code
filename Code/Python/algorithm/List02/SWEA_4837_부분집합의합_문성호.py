def my_sum(lst):
    result = 0
    for num in lst:
        result += num
    return result


T = int(input())

for test_case in range(1, T+1):
    N, set_sum = map(int, input().split())
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    cnt = 0  # 합이 set_sum 인 부분 집합의 개수

    for i in range(1 << 12):  # 2^N (부분집합의 총 개수)
        temp = []
        for j in range(13):  # 각 경우의 수,
            if i & (1 << j):  # 12개의 요소가 각각 있는지 없는지
                temp.append(arr[j])

        # 요소 개수 N개, 합이 set_sum인 부분 집합의 개수 세기
        if len(temp) == N and my_sum(temp) == set_sum:
            cnt += 1

    print('#{} {}'.format(test_case, cnt))