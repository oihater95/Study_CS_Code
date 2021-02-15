T = int(input())

for test_case in range(1, T+1):
    number = int(input())
    factor = [0 for i in range(5)]

    while number > 2:
        if number % 2 == 0:
            factor[0] += 1
            number = number // 2

        elif number % 3 == 0:
            factor[1] += 1
            number = number // 3

        elif number % 5 == 0:
            factor[2] += 1
            number = number // 5

        elif number % 7 == 0:
            factor[3] += 1
            number = number // 7

        elif number % 11 == 0:
            factor[4] += 1
            number = number // 11

    print('#{} {}'.format(test_case, ' '.join(map(str, factor))))

#####################################################33

T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    prime = [2, 3, 5, 7, 11]
    cnt = [0] * 5

    for i in range(len(prime)):
        while N % prime[i] == 0:
            cnt[i] += 1
            N //= prime[i]

    print('#{} {}'.format(test_case, ' '.join(map(str, cnt))))