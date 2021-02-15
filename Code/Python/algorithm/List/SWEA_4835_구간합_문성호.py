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

    for i in range(N - M + 1):
        sum_value = 0

        for j in range(M):
            sum_value += arr[i+j]

        result.append(sum_value)

    print('#{} {}'.format(test_case, my_max(result)-my_min(result)))


########################################################################
    # 저장하지 않고 그 때 그 때 갱신
T = int(input())

for test_case in range(1, T + 1):
    N, M = input().split()
    M = int(M)
    arr = list(map(int, input().split()))
    max_value = 0
    min_value = 9999999999999999
    
    for i in range(N - M + 1):
        tmp = 0
        for j in range(M):
            tmp += arr[i + j]
        
        # 최대값 갱신
        if max_value < tmp:
            max_value = tmp
        
        # 최소값 갱신
        if min_value > tmp:
            min_value = tmp

    print('#{} {}'.format(test_case, max_value - min_value))
########################################################################
# 중복 연산 피하기 이전 연산에서 중복되는 부분은 그대로 갖고 갱신되는 부분만 연산

T = int(input())

for test_case in range(1, T+1):
    N, M = input().split()
    M = int(M)
    arr = list(map(int, input().split()))

    tmp = 0  # 합
    for i in range(M):  # 첫 구간 합 (0 ~ M-1)
        tmp += arr[i]

    max_value = tmp  # 최대값 최소값 초기화
    min_value = tmp

    for i in range(M, N):  # 새로 추가되는 부분, 제거되는부분은 가장 첫 값을 빼면 됨 (M ~ N)
        tmp += arr[i] - arr[i-M]  # 새로 추가되는 수는 더하고 제거되는 부분은 뺀다

        if max_value < tmp:
            max_value = tmp

        if min_value > tmp:
            min_value = tmp

    print('#{} {}'.format(test_case, max_value - min_value))