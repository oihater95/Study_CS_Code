N = int(input())
dp = [0] * N  # idx개 로프 사용 최대로 들어올릴 수 있는 중량
result = 0
ropes = []

for i in range(N):
    ropes.append(int(input()))

ropes = sorted(ropes, reverse=True)  # 버틸 수 있는 중량 순 정렬

for num in range(N):
    # num개 사용 시 버틸 수 있는 무게는 num번째로 많이 버티는 로프 * (num + 1)
    dp[num] = ropes[num] * (num + 1)

print(max(dp))

