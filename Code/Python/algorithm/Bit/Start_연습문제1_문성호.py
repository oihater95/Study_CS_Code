# 0000000111100000011000000111100110000110000111100111100111111001100111
import math
binary= input()
numbers = []

# 7bit씩 끊어 읽기
for i in range(math.ceil(len(binary)/7)):
    if len(binary[7*i:]) >= 7:
        numbers.append(binary[7*i: 7*i+7])
    elif 0 < len(binary[7*i:]) < 7:
        numbers.append(binary[7*i:])
    else:
        continue

# 2진수 -> 10진수
for i in range(len(numbers)):
    ans = 0
    length = len(numbers[i])

    for j in range(length-1, -1, -1):
        if numbers[i][length-1-j] == '1':
            ans += 2**j
    print(ans, end=' ')
