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

        boxes[max_idx] -= 1
        boxes[min_idx] += 1

    result = my_max(boxes) - my_min(boxes)
    print('#{} {}'.format(test_case, result))
