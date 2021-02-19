# SWEA_3143_가장빠른문자열타이핑
def move(word, char):  # 얼마나 shift?
    for k in range(M-2, -1, -1):  # word[:M-2]
        if word[k] == char:
            return M - k - 1  # 범위에 있을 경우
    return M  # 범위에 없을 경우 word길이만큼 shift


T = int(input())

for test_case in range(1, T+1):
    text, word = input().split()  # 전체, 단어
    cnt = 0  # 단어 키 입력
    result = 0  # 전체 키 입력
    N, M = len(text), len(word)
    i = 0  # 전체 입력 인덱스

    # 보이어 무어
    while i <= N - M:
        j = M - 1  # 입력 단어 인덱스
        while j >= 0:
            if word[j] != text[i+j]:  # word의 뒤에서부터 비교, 다른 경우
                shift = move(word, text[i+M-1])  # word의 맨 끝자리와 비교한 text의 원소가 word에 있는지 확인
                break
            j -= 1  # 같은 경우

        if j == -1:  # 검색 성공
            cnt += 1
            i += M

        else:
            i += shift

    result = N - cnt * (M - 1)
    print('#{} {}'.format(test_case, result))