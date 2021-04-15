hexadecimal = '0123456789ABCDEF'

for tc in range(1, int(input())+1):
    N, hex = input().split()
    binary = ''

    for i in range(len(hex)):
        temp = ''
        for j in range(4):
            if hexadecimal.index(hex[i]) & (1 << j):
                temp = '1' + temp
            else:
                temp = '0' + temp
        binary += temp

    print('#{} {}'.format(tc, binary))
