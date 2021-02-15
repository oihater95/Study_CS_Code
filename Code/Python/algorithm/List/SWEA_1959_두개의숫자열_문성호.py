'''
입력
2
3 5
1 5 3
3 6 -7 5 4
7 6
6 0 5 5 -1 1 6
-4 1 8 7 -9 3

출력
#1 30
#2 63
'''
T = int(input())

for test_case in range(1, T+1):
    N, M = map(int, input().split())
    arr_A = list(map(int, input().split()))
    arr_B = list(map(int, input().split()))
    max_value = 0

    if M > N:
        for i in range(M - N + 1):
            tmp = 0

            for j in range(N):
                tmp += arr_B[i+j] * arr_A[j]

            if max_value < tmp:
                max_value = tmp

    else:
        for i in range(N - M + 1):
            tmp = 0

            for j in range(M):
                tmp += arr_A[i + j] * arr_B[j]

            if max_value < tmp:
                max_value = tmp

    print('#{} {}'.format(test_case, max_value))
