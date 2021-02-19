T = int(input())

for test_case in range(1, T+1):
    memory = input()
    origin = '0000'
    cnt = 0
    previous_key = [0]

    for i in range(len(memory)):
        if cnt == 0:
            if origin[i] != memory[i]:
                cnt += 1
                previous_key[0] = memory[i]
        else:
            if memory[i] != previous_key[0]:
                cnt += 1
                previous_key[0] = memory[i]

    print('#{} {}'.format(test_case, cnt))