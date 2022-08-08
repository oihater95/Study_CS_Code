# LeetCode 983 Minimum Cost For Tickets

# days = [1, 4, 6, 7, 8, 20]
# costs = [2, 7, 15]

# days = [1,2,3,4,5,6,7,8,9,10,30,31]
# costs = [2,7,15]

days = [1, 4, 6, 7, 8, 20]
costs = [7, 2, 15]

result = 987654321
# dp[current] => 현재 날짜 기준 최소 비용
dp = [result] * (days[-1] + 1)  # 1일부터 ~ 여행가는 마지막 날짜까지 모두 기록(안가는 날도 포함)
dp[0] = 0

for current in range(1, len(dp)):
    if current not in days:  # 여행가는 날짜가 아닐 때
        dp[current] = dp[current - 1]
        continue

    oneDayPass = dp[current - 1] + costs[0]  # 1-day pass 사용

    if current >= 7:
        weekPass = dp[current - 7] + costs[1]
    else:  # 현재 일이 7일보다 작을 때
        weekPass = dp[0] + costs[1]
    if current >= 30:
        monthPass = dp[current - 30] + costs[2]
    else:  # 현재 일이 30보다 작을 때
        monthPass = dp[0] + costs[2]
    # 현재 날짜 기준 최소 비용
    dp[current] = min(dp[current], oneDayPass, weekPass, monthPass)
    '''
<나영님 공유 코드>
dp[current] = min(dp[current], dp[current-1] + costs[0], dp[max(current-7, 0)] + costs[1], dp[max(current-30, 0)] + costs[2])
이렇게 쓰면 위의 분기 처리 필요없음
'''

print(dp[-1])