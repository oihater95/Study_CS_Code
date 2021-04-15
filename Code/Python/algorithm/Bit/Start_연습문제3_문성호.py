'''
0DEC => 0000110111101100
0269FAC9A0
'''

hexadecimal = '0123456789ABCDEF'
hex = input()
ans = ''
binary = ''
code = {  # 암호코드
    '0': '001101',
    '1': '010011',
    '2': '111011',
    '3': '110001',
    '4': '100011',
    '5': '110111',
    '6': '001011',
    '7': '111101',
    '8': '011001',
    '9': '101111',
    }

# 16진수 -> 2진수
for num in hex:
    temp = ''
    decimal = hexadecimal.index(num)

    for i in range(3, -1, -1):  # 4자리수 인덱스 = 0 ~ 3
        if int(decimal) & (1 << i):  # i번째 자리가 1이면 1
            temp += '1'
        else:
            temp += '0'

    binary = binary + temp

temp = list(binary)  # 리스트에 char 하나씩
for i in range(len(temp)-1, -1, -1):  # 뒤에서 부터 읽기
    if temp[i] == '1':  # 1부터 읽기
        if i - 5 >= 0:  # (i+1) - 6 >= 0, 6자리가 되는지 확인
            check = binary[i-5:i+1]  # 뒤에서 부터 1인 지점부터 6자리
            for j in range(6):  # 암호화 가능한 것은 0으로 처리
                temp[i-5+j] = '0'

            for key, value in code.items():  # 6자리 암호코드 읽기
                if value == check:
                    ans = key + ans
                    break

print(ans)


