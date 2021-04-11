# 최소가 되려면 - 나오는 부분부터 다음 - 나오는 부분 전까지 ()
# ex) 10-20+30-50 => 10 - (20 + 30) - 50 = -90
expression = input()
ans = 0
num = ''
temp = 0
cnt = 0

for char in expression:
    if char == '-':
        cnt += 1
        if cnt % 2:  # 홀수번째 -
            if num:
                temp += int(num)
            ans += temp
            temp = 0
            num = ''

        elif cnt % 2 == 0 and cnt > 0:  # 짝수번째 -
            if num:
                temp += int(num)
            ans -= temp
            temp = 0
            num = ''
            cnt = 1

    else:
        if char == '+':
            temp += int(num)
            num = ''

        else:  # 숫자
            num += char

if num:  # 숫자 남아있는 경우
    if cnt == 0:  # 숫자 앞 연산자 + or 숫자만 있는 경우
        ans += int(num)
    else:  # 숫자 앞 연산자 -
        ans -= int(num)

if temp != 0:  # 남은 괄호 값 처리
    if cnt == 0:  # 괄호 앞 연산자가 +이거나 없음
        ans += temp
    else:  # 괄호 앞 연산자 -
        ans -= temp

print(ans)

