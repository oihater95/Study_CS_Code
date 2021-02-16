T = int(input())

for test_case in range(1, T+1):
    D, L, N = map(int, input().split())  # D: 데미지, L: 레벨, N: 공격횟수
    total = 0  # 총 데미지

    for i in range(N):
        total += D * (1 + i * L * 0.01)  # i = 이전까지 공격한 횟수

    print('#{} {}'.format(test_case, int(total)))