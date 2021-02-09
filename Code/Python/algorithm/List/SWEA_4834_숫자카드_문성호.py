'''
입력
3
5
49679
5
08271
10
7797946543

출력
#1 9 2
#2 8 1
#3 7 3
'''
def my_max(arr):
    max_value = arr[0]
    for i in range(1, len(arr)):
        if max_value < arr[i]:
            max_value = arr[i]
    return max_value

T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    arr = list(map(int, input()))
    count = [0] * 10

    for i in range(len(arr)):
        count[arr[i]] += 1

    max_count = my_max(count)
    for j in range(len(count)):
        if count[j] == max_count:
            idx = j

    print('#{} {} {}'.format(test_case, idx, max_count))
