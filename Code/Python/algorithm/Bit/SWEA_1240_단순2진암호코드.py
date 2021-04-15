encode = {
    '0': '0001101',
    '1': '0011001',
    '2': '0010011',
    '3': '0111101',
    '4': '0100011',
    '5': '0110001',
    '6': '0101111',
    '7': '0111011',
    '8': '0110111',
    '9': '0001011',
}

for tc in range(1, int(input())+1):
    N, M = map(int, input().split())  # N: 세로 크기, M: 가로 크기
    arr = []
    for i in range(N):
        string = list(input())
        if '1' in string:  # 1이 들어있는 행만 배열에 넣기
            arr.append(string)

    code = []
    arr[0] = arr[0][::-1]  # 뒤에서 부터 읽기 대신에 리스트 자체를 reverse
    idx = arr[0].index('1')  # code 시작 인덱스 ('1'부터 시작)

    for i in range(8):  # 암호코드는 8개
        temp = ''

        for j in range(7):  # 암호코드는 각각 7글자
            temp = arr[0][idx + 7*i + j] + temp  # temp를 뒤에 두어야 순서에 맞게 코드 나옴

        for key, value in encode.items():  # 코드 딕셔너리에서 찾기
            if value == temp:
                code.append(key)
                break

    code = code[::-1]  # 뒤집어 읽었으므로 코드는 역순으로 되어있음
    calc1 = 0
    calc2 = 0

    for i in range(len(code)-1):
        if i % 2 == 0:  # 홀수
            calc1 += int(code[i])
        else:  # 짝수
            calc2 += int(code[i])

    valid = calc1*3 + calc2 + int(code[-1])  # 유효성 검사
    if valid % 10 == 0:
        ans = 0

        for i in range(len(code)):
            ans += int(code[i])
    else:
        ans = 0

    print('#{} {}'.format(tc, ans))
