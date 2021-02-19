for test_case in range(1, 11):
    tc = int(input())
    search = input()  # 찾을 문자열
    text = input()  # 전체 문자열
    cnt = 0

    for i in range(len(text)):
        if text[i] == search[0]:  # 첫글자와 같을 경우
            if text[i:i + len(search)] == search:  # 찾을 문자열과 같은지 확인 같으면 cnt +1
                cnt += 1

    print('#{} {}'.format(tc, cnt))
