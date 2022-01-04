T = input()
for tc in range(int(T)):
    # (100+1+|01)+
    pattern = input()
    # state를 담고 있는 코드
    code = [
        [7, 1],
        [2, 8],
        [3, 8],
        [3, 4],
        [7, 5],
        [6, 5],
        [3, 0],
        [8, 0],
        [8, 8]  # 8번 state는 무조건 false
    ]

    state = 0  # 초기 상태 = 0, 상태: 0 ~ 7

    for i in range(len(pattern)):
        state = code[state][int(pattern[i]) - 0]

    # state가 0 or 4 or 5 => 패턴 끝
    '''
    state = 0 => ...01로 끝난 경우
    state = 4 => 100...1 로 끝난 경우
    state = 5 => 100...1...1로 끝난 경우
    '''
    if state == 0 or state == 4 or state == 5:
        print('YES')
    else:
        print('NO')