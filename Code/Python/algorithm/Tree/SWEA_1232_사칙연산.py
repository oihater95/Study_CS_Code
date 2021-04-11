def postorder(num):  # 후위연산
    if num > 0:
        postorder(left[num])
        postorder(right[num])
        calc_order.append(num)


for tc in range(1, 11):
    V = int(input())  # 정점 수
    tree = [0] * (V+1)  # 트리 노드
    left = [0] * (V+1)  # 왼쪽 자식 노드 번호, 인덱스 = 부모 노드
    right = [0] * (V+1)  # 오른쪽 자식 노드 번호, 인덱스 = 부모 노드
    calc_order = []  # 계산 순서
    calc_stack = []  # 계산 스택

    for i in range(1, V+1):
        arr = list(input().split())
        if len(arr) == 4:  # 연산자인 경우
            tree[int(arr[0])] = arr[1]  # 연산자 넣기
            left[int(arr[0])] = int(arr[2])  # 왼쪽 자식 노드
            right[int(arr[0])] = int(arr[3])  # 오른쪽 자식 노드

        else:  # 숫자만 있는 경우
            tree[int(arr[0])] = int(arr[1])  # 숫자 넣기

    postorder(1)  # 수식 후위 표현, 루트는 1

    for idx in calc_order:
        if tree[idx] == '+' or tree[idx] == '-' or tree[idx] == '*' or tree[idx] == '/':  # 연산자인 경우
            operator = tree[idx]
            b = calc_stack.pop()
            a = calc_stack.pop()
            if operator == '+':
                calc_stack.append(a + b)

            elif operator == '-':
                calc_stack.append(a - b)

            elif operator == '*':
                calc_stack.append(a * b)

            elif operator == '/':
                calc_stack.append(a / b)

        else:  # 피연산자인 경우
            calc_stack.append(tree[idx])

    print('#{} {}'.format(tc, int(calc_stack[0])))
