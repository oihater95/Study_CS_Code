'''
N개의 정수 리스트
이웃한 M개 수 합

입력
3
10 3
1 2 3 4 5 6 7 8 9 10
10 5
6262 6004 1801 7660 7919 1280 525 9798 5134 1821
20 19
3266 9419 3087 9001 9321 1341 7379 6236 5795 8910 2990 2152 2249 4059 1394 6871 4911 3648 1969 2176

출력
#1 21
#2 11088
#3 1090
'''

def my_max(arr):
    max_value = arr[0]

    for i in range(1, len(arr)):
        if max_value < arr[i]:
            max_value = arr[i]
    return max_value

def my_min(arr):
    min_value = arr[0]

    for i in range(1, len(arr)):
        if min_value > arr[i]:
            min_value = arr[i]
    return min_value

T = int(input())

for test_case in range(1, T+1):
    N, M = input().split()
    M = int(M)
    arr = list(map(int, input().split()))
    result = []

    for i in range(len(arr)-M+1):
        sum_value = 0

        for j in range(M):
            sum_value += arr[i+j]

        result.append(sum_value)

    print('#{} {}'.format(test_case, my_max(result)-my_min(result)))
