N = int(input())  # 상담 가능 일자
T = []  # 상담 걸리는 시간
P = []  # 상담 완료 금액
dp = [0] * (N+1)

for i in range(N):
    t, p = map(int, input().split())
    T.append(t)
    P.append(p)

for i in range(N-1, -1, -1):
    if T[i] + i <= N:  # 현재 날짜 + 상담 걸리는 시간이 N을 넘지 않는 경우
        dp[i] = max(dp[i+1], P[i] + dp[i + T[i]])
    else:  # 넘는 경우
        dp[i] = dp[i+1]

