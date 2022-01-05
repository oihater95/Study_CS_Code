C, N = map(int, input().split())  # 목표 고객 수와 도시 수
infos = []  # 주어지는 정보
dp = [0] * ((1000 * 100) + 1)
ans = 0

for i in range(N):
    invest, customer = map(int, input().split())
    infos.append([invest, customer])

for i in range(len(infos)):
    for j in range(1, len(dp)):
        if j - infos[i][0] >= 0:
            dp[j] = max(dp[j], dp[j-infos[i][0]] + infos[i][1])

for i in range(1, len(dp)):
    if dp[i] >= C:
        print(i)
        break


