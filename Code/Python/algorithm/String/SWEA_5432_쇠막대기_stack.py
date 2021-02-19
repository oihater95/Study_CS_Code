T = int(input())

for test_case in range(1, T+1):
    iron_bar = input()
    stk = []  # stack, FILO (First In Last Out)
    ans = 0
    for i in range(len(iron_bar)):
        # 열린 괄호이면 stk리스트에 넣기
        if iron_bar[i] == '(':
            if iron_bar[i] == '(':
                stk.append('(')
        else:
            # 무조건 꺼내기
            stk.pop()
            # 레이저
            if iron_bar[i-1] == '(':
                ans += len(stk)
            else:
                ans += 1
    print('#{} {}'.format(test_case, ans))