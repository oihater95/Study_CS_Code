# test case 10개 중 9개맞음
T = int(input())

for test_case in range(1, T+1):
    arr = list(input())
    s = []
    cnt = 0  # append, pop된 횟수 => 열린괄호 없어 발생한 빈 스택 처리

    for i in range(len(arr)):
        if arr[i] == '(' or arr[i] == '{':  # 열린괄호 스택에 삽입
            s.append(arr[i])
            cnt += 1
        elif arr[i] == ')' or arr[i] == '}':  # 닫힌 괄호
            if len(s) == 0:  # 스택 비어있으면 break answer = 0
                break
            # 스택 안 비어 있음
            elif (arr[i] == ')' and s[-1] == '(') or (arr[i] == '}' and s[-1] == '{'):  # 닫힌 괄호가 이전 괄호랑 짝이 맞으면 pop
                s.pop()
                cnt += 1
            else:  # 짝이 맞지 않으면 break answer = 0
                break

    if cnt:  # 열린 괄호가 없는 문자열이 아닐 때
        if not s:  # 모두 순회하고 짝이 모두 맞았을 때 answer = 1
            answer = 1
        else:
            answer = 0

    print('#{} {}'.format(test_case, answer))



#####################################
T = int(input())
for test_case in range(1, T+1):
    data = input()
    stack = []
    result = 0
    for i in range(len(data)):
        if data[i] == '(' or data[i] == '{':  # 여는괄호가 올 경우 stack에 push
            stack.append(data[i])
        elif data[i] == ')' or data[i] == '}':  # 닫는괄호 이며 stack이 빈 경우
            if len(stack) == 0:  # 처음부터 닫는 괄호가 오는 경우 (스택이 빈 경우)
                stack = [data[i]]
                break  # 입력된 괄호와 stack의 top에 있는 괄호와 일치하지 않는 경우
            elif (data[i] == '}' and stack[-1] != '{') or (data[i] == ')' and stack[-1] != '('):
                stack = [data[i]]
                break
            else:  # stack에 저장된 괄호와 일치하는 닫는 괄호가 오는 경우
                stack.pop()

    if len(stack) == 0:
        result = 1
    else:
        result = 0
    print('#{} {}'.format(test_case, result))