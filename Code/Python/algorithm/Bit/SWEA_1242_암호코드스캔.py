hexadecimal = {
    '0': '0000', '1': '0001', '2': '0010', '3': '0011',
    '4': '0100', '5': '0101', '6': '0110', '7': '0111',
    '8': '1000', '9': '1001', 'A': '1010', 'B': '1011',
    'C': '1100', 'D': '1101', 'E': '1110', 'F': '1111'
}

decode = {  # 1, 0, 1 개수 비율
    0: [2, 1, 1],
    1: [2, 2, 1],
    2: [1, 2, 2],
    3: [4, 1, 1],
    4: [1, 3, 2],
    5: [2, 3, 1],
    6: [1, 1, 4],
    7: [3, 1, 2],
    8: [2, 1, 3],
    9: [1, 1, 2],
}

for tc in range(1, int(input())+1):
    N, M = map(int, input().split())  # N: 세로 크기, M: 가로 크기
    arr = [input() for _ in range(N)]
    binary = [''] * N  # 2진수 담을 리스트
    ans = []
    codes = []  # 코드 중복 확인
    ratio = [0] * 3  # 1 0 1 개수 비율

    for i in range(N):
        for j in range(M):
            binary[i] += hexadecimal[arr[i][j]]

    for i in range(N):
        if binary[i] == '0'*4*M:  # 0만 있는 녀석은 믿거
            continue

        if i > 0 and binary[i] == binary[i-1]:  # 중복이면 넘어감
            continue

        code = []  # 암호코드 담을 리스트
        for j in range(4*M-1, -1, -1):  # 뒤에서부터 읽기
            if ratio[0] == 0 and ratio[1] == 0 and binary[i][j] == '1':  # 2번째 '1' 개수 세기
                ratio[2] += 1
            elif ratio[0] == 0 and ratio[2] != 0 and binary[i][j] == '0':  # 2번째 '0' 개수 세기
                ratio[1] += 1
            elif ratio[2] != 0 and ratio[1] != 0 and binary[i][j] == '1':  # 1번째 '1' 개수 세기
                ratio[0] += 1
            # 암호코드 1번째 '1' 앞에 '0'이 오면 읽었던 1 0 1 개수를 비율 처리
            if ratio[0] != 0 and ratio[1] != 0 and ratio[2] != 0 and binary[i][j] == '0':
                min_value = min(ratio)  # 최소값으로 나눠 비율 산출
                ratio[0] //= min_value
                ratio[1] //= min_value
                ratio[2] //= min_value

                # 암호코드 딕셔너리에 있으면 key값을 코드에 추가
                for key, value in decode.items():
                    if value == ratio:
                        code.append(key)
                        break
                ratio[0], ratio[1], ratio[2] = 0, 0, 0  # 비율 초기화

            if len(code) == 8:  # 코드가 8자리 모두 채워지면
                code = code[::-1]  # 뒤에서부터 읽었으니 뒤집어줌
                odd = 0
                even = 0
                for k in range(7):  # 마지막 코드 번호는 유효성 검사코드
                    if k % 2 == 0:  # 짝수 인덱스 => 홀수번째 암호코드
                        odd += code[k]
                    else:
                        even += code[k]
                valid = odd * 3 + even + code[7]

                # 유효성 검사
                if valid % 10 == 0:
                    if code not in codes:
                        codes.append(code)
                        ans.append(sum(code))

                else:
                    if 0 in ans:  # 중복 방지
                        pass
                    else:
                        ans.append(0)
                code = []

    print('#{} {}'.format(tc, sum(ans)))