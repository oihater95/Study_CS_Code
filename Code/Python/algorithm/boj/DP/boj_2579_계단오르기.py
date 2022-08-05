N = int(input())
steps = []
# dp[i][0] => i번째 계단 안밟고, i번째 최댓값
# dp[i][1] => i번째 계단 밟고 i번째 최댓값
dp = [[0, 0] for _ in range(N)]

for i in range(N):
    steps.append(int(input()))

dp[0][1] = steps[0]

if N < 2:
  print(steps[0])
  exit(0)


dp[1][0] = steps[0]
dp[1][1] = dp[0][1] + steps[1]

if N == 2:
  print(max(dp[1][0], dp[1][1]))
  exit(0)

dp[2][0] = dp[1][1]
dp[2][1] = steps[0] + steps[2]

for i in range(3, N):
		# i번째 안 밟았으면 3번째 전 안 밟은 것과 2번째 전 안 밟은 것 비교
    dp[i][0] = max(dp[i-3][0] + steps[i-2] + steps[i-1], dp[i-2][0] + steps[i-1])
		# i번째 밟았으면 1번째 전 안 밟거나 2번째 전 안 밟기
    dp[i][1] = max(dp[i-1][0], dp[i-2][0] + steps[i-1]) + steps[i]

print(dp[N-1][1])  # 마지막은 항상 밟는다