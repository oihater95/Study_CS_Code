def sorting(lst):  # 선택정렬
    for i in range(len(lst)-1):
        min_idx = i
        for j in range(i+1, len(lst)):
            if lst[min_idx] > lst[j]:
                min_idx = j
        lst[i], lst[min_idx] = lst[min_idx], lst[i]

    return lst

T = int(input())

for test_case in range(1, T+1):
    str_num = ['ZRO', 'ONE', 'TWO', 'THR', 'FOR', 'FIV', 'SIX', 'SVN', 'EGT', 'NIN']
    tc, N = map(str, input().split())
    N = int(N)
    arr = list(map(str, input().split()))
    temp = []
    result = []

    # str -> int
    for i in range(len(arr)):
        for j in range(len(str_num)):
            if arr[i] == str_num[j]:
                temp.append(j)

    # selection sort
    temp = sorting(temp)

    # int -> str
    for i in range(len(temp)):
        result.append(str_num[temp[i]])

    print('#{}'.format(test_case))
    print(' '.join(result))
