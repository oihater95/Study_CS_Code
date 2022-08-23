n, k = map(int, input().split())
arr = list(range(1, n+1))
idx = 0
result = []

while len(result) != n:
    idx += k - 1  # idx = 0부터 카운트 & pop된 요소 다음부터 카운트 시작

    if idx >= len(arr):
        idx = idx % len(arr)

    result.append(arr.pop(idx))

print("<", end="")
for i in range(n):
    print(result[i], end="")
    if i != n - 1:
        print(",", end=" ")
print(">")
