# Selection Sort 선택 정렬
# 바로바로 교환하지 않아 계산량이 적다
arr = [10, 15, 2, 19, 6, 14]

for i in range(len(arr)-1):  # 두번째로 큰 값까지 정렬하면 가장 큰 값은 따로 안해줘도 됨
    min_idx = i

    for j in range(i+1, len(arr)):
        if arr[j] < arr[min_idx]:
            min_idx = j  # 인덱스만 옮겨줌, 바로바로 교환하지 않음

    # i+1 ~ 마지막 범위까지 가장 작은 값과 i번째 값 교환
    arr[i], arr[min_idx] = arr[min_idx], arr[i]
    print('기준 idx: ', i, arr)