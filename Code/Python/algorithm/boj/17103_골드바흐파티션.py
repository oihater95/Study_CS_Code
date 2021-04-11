T = int(input())
nums = [int(input()) for _ in range(T)]
max_num = max(nums)  # 입력 받은 수 중 최대값
prime_check = [False, False] + [True] * (max_num-1)  # 소수인지 아닌지, 에라토스테네스의 체

for i in range(2, int(max_num**0.5)+1):  # 제곱근
    if prime_check[i]:  # 소수일 경우
        for j in range(i*2, max_num+1, i):  # 소수의 배수 제거
            prime_check[j] = False

for n in nums:
    cnt = 0
    for i in range(1, n//2+1):  # 같은 숫자 조합 순서만 다른 것은 카운트 X
        if prime_check[i] and prime_check[n-i]:  # n = i + n-i & 둘 다 소수일 경우
            cnt += 1

    print(cnt)