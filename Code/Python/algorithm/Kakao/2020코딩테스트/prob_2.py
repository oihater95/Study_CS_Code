# p = "(()())()"
# p = ")("
# p = "()))((()"
answer = ''
temp = ''

def process(string):
    global answer, temp
    cnt_left = 0
    cnt_right = 0
    stk = []
    correct_flag = False
    u = ''
    v = ''


    if string == '':
        return ''

    # 균형잡힌 괄호 u, v
    for i in range(len(string)):
        if cnt_left > 0 and cnt_right > 0 and cnt_left == cnt_right:
            u = string[:i]
            if i+1 == len(string):
                v = ''
            else:
                v = string[i:]
            break

        if string[i] == '(':
            cnt_left += 1
        else:
            cnt_right += 1

    if u == '' and cnt_left == cnt_right:
        u = string[:]

    # 올바른 괄호
    for i in range(len(u)):
        if len(stk) > 0:
            if stk[-1] == '(' and u[i] == ')':
                stk.pop()
            else:
                stk.append(u[i])
        else:
            stk.append(u[i])

    if len(stk) == 0:
        correct_flag = True

    # u가 올바른 괄호인 경우
    if correct_flag == True:
        return u + process(v)

    # u가 올바른 괄호가 아닌 경우
    else:
        tmp = '('
        tmp += process(v)
        tmp += ')'
        temp_u = u[1:len(u)-1]
        new_u = ''
        for char in temp_u:
            if char == '(':
                new_u += ')'
            else:
                new_u += '('
        tmp += new_u
        return tmp

answer = process(p)
print(answer)