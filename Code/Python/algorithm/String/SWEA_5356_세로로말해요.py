T = int(input())

for test_case in range(1, T+1):
    arr = []
    result = ''
    for i in range(5):
        arr.append(list(input()))
    # 가장 긴 문자열
    max_len = 0
    for i in range(5):
        if max_len < len(arr[i]):
            max_len = len(arr[i])
    # 길이 짧은 문자열에 대해 길이가 가장 긴 문자열 기준으로 빈 부분 ''로 채우기
    for i in range(5):
        for j in range(max_len - len(arr[i])):
            arr[i].append('')

    # 세로 읽기
    for i in range(max_len):
        for j in range(5):
            result += arr[j][i]

    print('#{} {}'.format(test_case, result))
