
# 에라토스테네스의 체
def prime(n):
    for i in range(2, int(int(n) ** 0.5)+1):
        if int(n) % i == 0:
            return
    if len(n) == N:
        print(n)
        return

    for j in odds:
        prime(n + j)

N = int(input())
odds = ['1', '3', '7', '9']  # 짝수와 5로 끝나는 두자리이상의 수는 소수아님
nums = ['2', '3', '5', '7']  # 첫자리는 이것만 소수

for num in nums:
    prime(num)

