# 3 #전체 테스트 케이스의 수
# 9 # 아래의 원소수
# 7 4 2 0 0 6 0 7 0 #원소들 (리스트)
# 9
# 7 4 2 0 0 6 7 7 0
# 20
# 52 56 38 77 43 31 11 87 68 64 88 76 56 59 46 57 75 85 65 53
#1 7

#2 6

#3 13

def my_max(arr):  # 리스트 중 최대 값 반환
    max_value = arr[0]

    for i in range(1, len(arr)):
        if max_value < arr[i]:
            max_value = arr[i]

    return max_value


def CountingSort(lst):  # 카운팅 정렬
    cnt = [0] * (my_max(lst)+1)
    result = [0] * len(lst)
    for num in lst:  # 카운팅
        cnt[num] += 1

    for i in range(1, len(cnt)):  # 누적합
        cnt[i] += cnt[i-1]

    for i in range(len(lst)-1, -1, -1):  # 정렬
        result[cnt[lst[i]]-1] = lst[i]
        cnt[lst[i]] -= 1

    return result


N = int(input())  # Test case 수

for i in range(N):
    num_elem = int(input())  # 원소 수
    arr = list(map(int, input().split()))  # 원소 리스트
    height = []  # 각각의 열 마다 최대 낙하 높이

    for j in range(num_elem-1):
        sorted_box = CountingSort(arr[j+1:])

        if arr[j] > sorted_box[-1]:
            height.append(num_elem - j - 1)
            break

        else:
            height.append(num_elem - j - 1)
            for box in sorted_box:
                if arr[j] <= box:
                    height[j] -= 1

    print(my_max(height))  # 최대 낙하 높이


