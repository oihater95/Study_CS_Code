n = int(input())
dp = [0] * (n+1)

if n == 0:
    print(0)
elif n == 1:
    print(1)
else:
    dp[1] = 1
    for i in range(2, n + 1):
        dp[i] = dp[i - 2] + dp[i - 1]

    print(dp[-1])

######################################
# Memoization
def fibo(n):
    if memo[n] != 0:
        num = memo[n]

    else:
        num = fibo(n-1) + fibo(n-2)
        memo[n] = num
    return num


N = int(input())
memo = [0] * (N+1)
memo[0] = 0
memo[1] = 1
memo[2] = 1

ans = fibo(N)
print(ans)