def selection_sort(lst):  # 선택 정렬
    for i in range(len(lst)-1):
        min_idx = i
        for j in range(i+1, len(lst)):
            if lst[min_idx] > lst[j]:
                min_idx = j
        lst[i], lst[min_idx] = lst[min_idx], lst[i]
    return lst


T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    arr = selection_sort(arr)  # 오름차순 정렬
    result = []

    for cnt in range(len(arr)//2):  
        result.append(arr[len(arr) - 1 - cnt])
        result.append(arr[cnt])

    if len(arr) % 2:  # 길이가 홀수인 경우 중간값 하나가 남음
        result.append(arr[len(arr)//2])

    print('#{} {}'.format(test_case, ' '.join(map(str, result[:10]))))  # 10개까지만 출력
