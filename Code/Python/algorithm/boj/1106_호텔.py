C, N = map(int, input().split())  # 목표 고객 수와 도시 수
infos = []  # 주어지는 정보
dp = [0] * ((1000 * 100) + 1)
ans = 0

for i in range(N):
    invest, customer = map(int, input().split())
    infos.append([invest, customer])

# dp[i] => i만큼의 돈으로 홍볼 할 수 있는 최대 인원을 각 도시를 돌면서 확인하여 최대값으로 갱신
for i in range(1, len(dp)):
    for j in range(N):
        if infos[j][0] <= i:
            dp[i] = max(dp[i], dp[i-infos[j][0]] + infos[j][1])

    if dp[i] >= C:
        print(i)
        break


