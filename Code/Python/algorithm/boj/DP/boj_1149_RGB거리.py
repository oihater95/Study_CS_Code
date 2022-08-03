N = int(input())  # 집 수
costs = [list(map(int, input().split())) for _ in range(N)]  # RGB 비용 리스트
dp = [[0,0,0] for _ in range(N)]  # i번째까지 R, G, B 칠한 것 중 최솟값

for i in range(3):
    dp[0][i] = costs[0][i]

for i in range(1, N):
    dp[i][0] += min(dp[i-1][1], dp[i-1][2]) + costs[i][0]  # i번째 R로 칠할 경우 최솟값(i-1번째까지 최솟값(G, B) + 현재 R비용)
    dp[i][1] += min(dp[i-1][0], dp[i-1][2]) + costs[i][1]  # i번째 G로 칠할 경우 최솟값(i-1번째까지 최솟값(R, B) + 현재 G비용)
    dp[i][2] += min(dp[i-1][0], dp[i-1][1]) + costs[i][2]  # i번째 B로 칠할 경우 최솟값(i-1번째까지 최솟값(R, G) + 현재 B비용)

print(min(dp[N-1]))