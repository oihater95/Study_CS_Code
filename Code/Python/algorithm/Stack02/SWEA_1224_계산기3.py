# 계산기
for tc in range(1, 11):
    N = int(input())
    expression = input()  # 수식
    stack = []
    postfix = ''  # 후위 연산식

    '''
    우선순위가중치 (스택 안: isp, 스택 밖: icp)
    연산자     스택 안    스택 밖
    (            0          3
    )            -          -  
    *, /         2          2
    +, -         1          1
    '''

    for char in expression:
        # 스택 밖에서의 연산자 우선도
        if char == '(':
            icp = 3
        elif char == '*':
            icp = 2
        elif char == '+':
            icp = 1

        if stack:  # 스택 내 연산자 우선도
            if stack[-1] == '(':
                isp = 0
            elif stack[-1] == '*':
                isp = 2
            elif stack[-1] == '+':
                isp = 1

        if char in '0123456789':  # 피연산자
            postfix += char
        else:  # 연산자
            if not stack:  # 스택이 비었을 경우
                stack.append(char)
            else:  # 스택에 연산자 있을 경우 우선순위 비교
                if char == ')':  # 우선도 비교하지 않음 top에 '('가 올 때까지 pop
                    while stack[-1] != '(':
                        postfix += stack.pop()
                    stack.pop()  # stack top이 '('이면 pop만 수행

                else:  # 그 외 연산자는 우선도 비교
                    if icp > isp:  # 연산자 우선도가 스택의 top 연산자보다 높으면 push
                        stack.append(char)
                    else:  # 높지 않다면 스택top 연산자 우선도가 높을 때 까지 pop한 후 자신을 push
                        while icp <= isp:
                            postfix += stack.pop()
                            if stack[-1] == '(':
                                isp = 0
                            elif stack[-1] == '*':
                                isp = 2
                            elif stack[-1] == '+':
                                isp = 1
                        stack.append(char)

    if stack:  # 스택에 남아있다면 모두 pop
        while stack:
            postfix += stack.pop()

    ##########################################
    # 후위연산 계산
    calc = []  # 계산 스택

    for char in postfix:
        if char in '0123456789':
            calc.append(int(char))
        else:
            # 스택은 LIFO 구조 => 가장 최근 값을 b로 설정
            b = calc.pop()
            a = calc.pop()

            # 연산결과 추가
            if char == '+':
                calc.append(a+b)
            elif char == '*':
                calc.append(a*b)

    print('#{} {}'.format(tc, calc[-1]))