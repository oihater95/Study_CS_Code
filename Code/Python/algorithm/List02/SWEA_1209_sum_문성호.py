def selection_sort_max(lst):
    for a in range(len(lst)-1):
        min_idx = a
        for b in range(a+1, len(lst)):
            if lst[min_idx] > lst[b]:
                min_idx = b
        lst[a], lst[min_idx] = lst[min_idx], lst[a]

    return lst[-1]


for test_case in range(1, 11):
    N = int(input())
    arr = list()
    my_sum = []

    for i in range(100):
        arr.append(list(map(int, input().split())))

    result_dig = 0
    result_dig_reverse = 0

    for i in range(100):
        result_row = 0
        result_col = 0

        for j in range(100):
            result_row += arr[i][j]
            result_col += arr[j][i]

        result_dig += arr[i][i]
        result_dig_reverse += arr[i][99-i]
        my_sum.extend([result_row, result_col, result_dig, result_dig_reverse])

    print('#{} {}'.format(test_case, selection_sort_max(my_sum)))