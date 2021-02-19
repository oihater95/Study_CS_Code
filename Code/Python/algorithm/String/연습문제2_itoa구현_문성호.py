def itoa(int_num):
    str_num = ''
    char_num = []  # 정수를 한 자리씩 string으로 변환한 데이터넣음(역순)

    if int_num < 0:  # 음수일 경우 - 추가
        str_num += '-'
        int_num *= -1

    while int_num:  # 일의 자리부터 한 자리씩 변환
        num = int_num % 10
        char_num.append(chr(ord('0') + num))
        int_num //= 10

    for i in range(len(char_num)-1, -1, -1):  # char_num에 역순으로 들어갔기 때문에 뒤에서부터 순회
        str_num += char_num[i]

    print(str_num, type(str_num))  # 반환 없음

itoa(1234)
itoa(-1234)