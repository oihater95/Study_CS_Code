n = int(input())
arr = []
for i in range(n):
    arr.append(list(map(int, input().split())))

# arr[i][j]가 될 수 있는 경우
# arr[i-1][j] + arr[i][j] or arr[i-1][j-1] + arr[i][j]
for i in range(1, n):
    for j in range(len(arr[i])):
        if j == 0:
            arr[i][j] = arr[i][j] + arr[i-1][j]
        elif j == i:
            arr[i][j] = arr[i][j] + arr[i-1][j-1]
        else:
            arr[i][j] = max(arr[i][j] + arr[i-1][j], arr[i][j] + arr[i-1][j-1])

print(max(arr[n-1]))
