'''
내장함수 X
입력
3
5
477162 658880 751280 927930 297191
5
565469 851600 460874 148692 111090
10
784386 279993 982220 996285 614710 992232 195265 359810 919192 158175

출력
#1 630739
#2 740510
#3 838110
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
for i in range(1, T+1):
    N = int(input())
    numbers = list(map(int, input().split()))
    result = my_max(numbers) - my_min(numbers)
    print('#{} {}'.format(i, result))

