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

T = 10

for test_case in range(1, T+1):
    dumps = int(input())
    boxes = list(map(int, input().split()))

    for i in range(dumps):
        for j in range(len(boxes)):
            if my_max(boxes) == boxes[j]:
                max_idx = j
            elif my_min(boxes) == boxes[j]:
                min_idx = j

        if boxes[max_idx] - boxes[min_idx] <= 1:
            break
        else:
            boxes[max_idx] -= 1
            boxes[min_idx] += 1

    result = my_max(boxes) - my_min(boxes)
    print('#{} {}'.format(test_case, result))


##############################################################
def my_max():
    max_value = box[0]

    for i in range(1, len(box)):
        if max_value < box[i]:
            max_value = box[i]
            max_idx = i
    return max_idx


def my_min():
    min_value = box[0]

    for i in range(1, len(box)):
        if min_value > box[i]:
            min_value = box[i]
            min_idx = i
    return min_idx
T = 10

for test_case in range(1, T+1):
    N = int(input())  # dump 횟수
    box = list(map(int, input().split()))

    for i in range(N):
        box[my_max()] -= 1
        box[my_min()] += 1

    print('#{} {}'.format(test_case, box[my_max()] - box[my_min()]))

###################################################################
# 정렬활용 => 높이 카운팅
for test_case in range(1, 11):
    N = int(input())
    box = list(map(int, input().split()))

    # 높이 카운트
    h_cnt = [0] * 101

    # 초기화
    min_value = 100
    max_value = 1

    # 박스의 높이를 카운트하면서 최고점과 최저점을 찾기
    for i in range(100):
        h_cnt[box[i]] += 1
        if box[i] > max_value:
            max_value = box[i]
        if box[i] < min_value:
            min_value = box[i]

    while N > 0 and min_value < max_value-1:
        # 상자 옮기기
        h_cnt[min_value] -= 1
        h_cnt[min_value + 1] += 1

        h_cnt[max_value] -= 1
        h_cnt[max_value - 1] += 1

        # 포인터 변경
        if h_cnt[min_value] == 0:
            min_value += 1

        if h_cnt[max_value] == 0:
            max_value -= 1

        # 덤프 줄이기
        N -= 1

        print('#{} {}'.format(test_case, max_value - min_value))