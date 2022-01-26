def splitSection(x):
    min_x, max_x = arr[0], arr[0]
    cnt = 1

    for i in range(1, n):
        max_x = max(max_x, arr[i])
        min_x = min(min_x, arr[i])

        if max_x - min_x > x:
            cnt += 1
            max_x = arr[i]
            min_x = arr[i]

    return cnt

n, m = map(int, input().split())
arr = list(map(int, input().split()))
ans = 0
left, right = 0, max(arr)

while left <= right:
    mid = (left + right) // 2

    if splitSection(mid) <= m:
        right = mid - 1
        ans = mid
    else:
        left = mid + 1

print(ans)