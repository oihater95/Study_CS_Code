T = int(input())

for test_case in range(1, T+1):
    string = input()
    stack = []  # 반복되지 않은 문자열

    for i in range(len(string)):
        if not stack:  # 스택이 비어있을 때
            stack.append(string[i])  # 스택에 추가
        else:
            if string[i] == stack[-1]:  # 현재 들어오는 문자가 이전문자(스택의 top)와 같다면 반복된 문자
                stack.pop()  # 반복 제거
            else:
                stack.append(string[i])  # 반복되지 않았다면 추가

    print('#{} {}'.format(test_case, len(stack)))
