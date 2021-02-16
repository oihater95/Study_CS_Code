def binary_search(num):  # 이진 탐색
    start = 1  # 시작
    end = total  # 끝
    count = 0  # 몇 번 탐색했는지 카운트

    while start <= end:  # 시작과 끝이 같거나 시작이 더 커질 때 까지
        mid = int((start+end)/2)  # 중간값

        if mid > num:  # 중간값이 목표값보다 클 때
            end = mid  # 끝 값을 중간값으로 갱신
            count += 1
        elif mid < num:  # 중간값이 목표값보다 작을 때
            start = mid  # 시작 값을 중간값으로 갱신
            count += 1
        else:  # 목표값 탐색성공
            break
    return count


T = int(input())

for test_case in range(1, T+1):
    total, A, B = map(int, input().split())

    if binary_search(A) < binary_search(B):
        result = 'A'
    elif binary_search(A) > binary_search(B):
        result = 'B'
    else:
        result = 0

    print('#{} {}'.format(test_case, result))

