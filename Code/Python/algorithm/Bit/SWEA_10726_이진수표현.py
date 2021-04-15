for tc in range(1, int(input())+1):
    N, M = map(int, input().split())
    binary = ''
    idx = 0
    on = '1' * N

    # 10진수 -> 2진수
    if M == 0:
        binary = '0'
    else:
        while 2**idx <= M:
            if M & (1 << idx):  # M을 2진수로 바꿨을 때 뒤에서 idx+1번째 자리수가 1인지
                binary = '1' + binary
            else:
                binary = '0' + binary
            idx += 1

    if binary[len(binary)-N:] == on:
        print('#{} {}'.format(tc, 'ON'))
    else:
        print('#{} {}'.format(tc, 'OFF'))