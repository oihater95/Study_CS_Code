for test_case in range(1, 11):
    N = int(input())
    arr = list(input())
    s = []  # stack
    answer = 0  # 짝이 맞는지 안 맞는지
    # 첫번째 원소 삽입
    if arr[0] == '(' or '{' or '[' or '<':
        s.append(arr[0])

    # 원소 삽입, 짝이 맞으면 pop
    for i in range(1, N):
        # push
        if arr[i] in '({[<':
            s.append(arr[i])

        # stack의 top과 짝이 맞으면 pop
        elif arr[i] == ')' and s[len(s)-1] == '(':
            s.pop()
        elif arr[i] == '}' and s[len(s)-1] == '{':
            s.pop()
        elif arr[i] == ']' and s[len(s)-1] == '[':
            s.pop()
        elif arr[i] == '>' and s[len(s)-1] == '<':
            s.pop()
        # 규칙에 맞지 않는 경우 break, 0 출력
        else:
            break

    if len(s) == 0:
        answer = 1

    print('#{} {}'.format(test_case, answer))
