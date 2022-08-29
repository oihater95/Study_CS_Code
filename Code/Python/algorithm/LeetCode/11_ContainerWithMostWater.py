# Two Pointers
height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
start, end, max_area = 0, len(height) - 1, 0


while start < end:
    area = (end - start) * min(height[start], height[end])

    if max_area < area:
        max_area = area

    # 더 낮은 값의 포인터 이동 (start는 오른쪽으로 end는 왼쪽으로)
    if height[start] < height[end]:
        start += 1
    else:
        end -= 1

print(max_area)