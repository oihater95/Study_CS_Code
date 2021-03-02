for test_case in range(1, 11):
    N, pw = input().split()
    N = int(N)
    stack = []

    for i in range(N):
        if not stack:  # stack이 비어 있을 때
            stack.append(pw[i])  # 추가
        else:
            if pw[i] == stack[-1]:  # 중복되면 pop
                stack.pop()
            else:
                stack.append(pw[i])  # 중복 안되면 추가

    print('#{} {}'.format(test_case, ''.join(stack)))