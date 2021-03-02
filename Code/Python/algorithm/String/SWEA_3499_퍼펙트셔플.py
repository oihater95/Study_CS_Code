T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    card = list(input().split())
    result = [0 for _ in range(N)]

    if N % 2:  # 길이 홀수
        for i in range(N // 2):
            result[2 * i] = card[i]
            result[2 * i + 1] = card[N // 2 + i + 1]
        result[2 * (N//2)] = card[N//2]
    else:
        for i in range(N // 2):
            result[2 * i] = card[i]
            result[2 * i + 1] = card[N // 2 + i]

    print('#{} {}'.format(test_case, ' '.join(map(str, result))))