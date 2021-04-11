arr = list(map(int, input()))
arr.insert(0, 0)
dp = [0] * (len(arr))
if arr[1] == 0:
    print(0)

else:
    dp[0] = 1
    dp[1] = 1  # 1번째 자리는 1가지 경우만 가능

    for i in range(2, len(arr)):
        if 1 <= arr[i] <= 10:  # arr[i]를 한자리 수로 볼 때, arr[i] !=0
            dp[i] += dp[i-1]  # 이전 경우의 수와 같음

        temp = arr[i-1] * 10 + arr[i]  # arr[i]를 두자리 수로 볼 때
        if 10 <= temp <= 26:  # 두 자리수가 알파벳 범위 안에 들어올 경우
            dp[i] += dp[i-2]  # 전전 경우의 수만큼 더해줌

        dp[i] %= 1000000

    print(dp[-1])
