def calc():
    for i in range(len(expression)):
        try:  # 연산 또는 출력 가능
            # 연산자일 때
            if expression[i] == '.':  # 계산 결과 출력
                if len(stack) == 1:
                    return int(stack.pop())
                else:  # 피연산자가 남아있는 경우
                    return 'error'

            # 연산 가능
            elif expression[i] == '+':
                a = stack.pop()
                b = stack.pop()
                result = a + b
                stack.append(result)
            elif expression[i] == '-':
                a = stack.pop()
                b = stack.pop()
                result = b - a
                stack.append(result)
            elif expression[i] == '*':
                a = stack.pop()
                b = stack.pop()
                result = a * b
                stack.append(result)
            elif expression[i] == '/':
                a = stack.pop()
                b = stack.pop()
                result = b / a
                stack.append(result)

            else:  # 숫자일 때
                stack.append(int(expression[i]))

        except:  # 연산 불가, 피연산자가 없거나 1개만 있는 경우
            return 'error'

T = int(input())

for test_case in range(1, T+1):
    expression = list(input().split())  # 입력 수식
    stack = []

    print('#{} {}'.format(test_case, calc()))