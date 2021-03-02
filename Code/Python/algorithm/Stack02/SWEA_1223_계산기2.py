for test_case in range(1, 11):
    N = int(input())
    expression = input()
    op_stack = []  # 연산자 스택
    postfix = ''
    # 후위 표기법
    for char in expression:
        if char in '0123456789':  # 피연산자는 후위표기식에 push
            postfix += char

        else:  # 연산자 + or *
            if not op_stack:  # 연산자 스택 비어있다면 push
                op_stack.append(char)

            else:  # 연산자 스택의 top과 우선순위 비교
                if char == '+':
                    while op_stack:  # 스택 top 연산자 우선순위보다 낮으면 자신이 더 높을 때까지 pop
                        postfix += op_stack.pop()  # +의 경우 자신보다 낮은 우선순위는 없기에 스택이 빌 때까지 pop
                    op_stack.append(char)
                else:  # *연산자
                    if op_stack[-1] == '+':  # +보다 우선순위 높으므로 push
                        op_stack.append(char)
                    else:
                        while op_stack[-1] == '*':  # 같은 우선순위인 *이면 +나오거나 빌 때까지 pop 한 후 자신을 push
                            postfix += op_stack.pop()
                            if not op_stack:  # 연산자 스택 비어있으면 break후 push
                                break
                        op_stack.append(char)

    if op_stack:  # 스택에 남아있다면 모두 pop
        while op_stack:
            postfix += op_stack.pop()
    ################################################################3
    # 후위 표기식 연산
    calc = []

    for char in postfix:
        if char in '0123456789':  # 피연산자
            calc.append(int(char))
        else:  # 연산자, 스택은 LIFO 구조 => b를 먼저 초기화
            b = calc.pop()
            a = calc.pop()
            # 연산 결과를 calc 스택에 push
            if char == '+':
                calc.append(a+b)
            else:
                calc.append(a*b)

    print('#{} {}'.format(test_case, calc[0]))