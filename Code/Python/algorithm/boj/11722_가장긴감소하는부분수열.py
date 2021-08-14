N = int(input())
arr = list(map(int, input().split()))
dp = [0] * N
dp[0] = 1

for i in range(1, N):
    for j in range(i):
        if arr[i] < arr[j] and dp[i] < dp[j]:  # i번째 수 이전에 i번째 수보다 크고 dp가 가장 큰 값을 따라감
            dp[i] = dp[j]
    dp[i] += 1

print(max(dp))