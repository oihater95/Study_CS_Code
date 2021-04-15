for tc in range(1, int(input())+1):
    n = float(input())
    binary = ''
    idx = 1
    while n != 0:
        if 2 ** (-idx) > n:
            idx += 1
            binary += '0'

        else:
            n -= 2 ** (-idx)
            binary += '1'
            idx += 1

        if len(binary) > 12:
            binary = 'overflow'
            break

    print('#{} {}'.format(tc, binary))