# 01D06079861D79F99F
# 0F97A3
hex = input()
numbers = ''
hexadecimal = '0123456789ABCDEF'

for i in range(len(hex)):
    temp = ''
    for j in range(4):
        # 16진수 -> 2진수
        # 10진수 & (1 << j) => 2진수로 바꿨을 때 j번째 자리가 1인지
        if hexadecimal.index(hex[i]) & (1<<j):
            temp = '1' + temp
        # j번째 자리가 1이 아니면 0 넣기
        else:
            temp = '0' + temp

    numbers += temp

for i in range(0, len(numbers), 7):  # 7bit 씩
    ans = 0
    if len(numbers[i:]) >= 7:
        num = numbers[i:i+7]
    else:
        num = numbers[i:]

    for j in range(len(num)-1, -1, -1):  # 2진수 -> 10진수
        if num[j] == '1':
            ans += 2 ** (len(num)-1-j)

    print(ans)