# 보이어-무어
def move(pattern, char):  # 얼마나 shift?
    for k in range(N-2, -1, -1):
        if pattern[k] == char:  # 내부에 있으면 N-i-1만큼 shift
            return N-k-1
    return N  # 내부에 없으면 N만큼 shift


T = int(input())

for test_case in range(1, T+1):
    pattern = input()  # 찾을 문자열
    text = input()  # 전체 문자열
    i = 0  # 전체 문자열의 인덱스
    N, M = len(pattern), len(text)  # pattern, text의 길이
    answer = 0

    while i <= M-N:  # 마지막 i + N = M
        j = N-1  # pattern의 인덱스, 뒤에서부터 순회

        while j >= 0:
            if pattern[j] != text[i + j]:  # 끝자리부터 비교, 다르다면 shift
                shift = move(pattern, text[i + N - 1])  # text[i+N-1]이 pattern[:N-1] 내부에 있는지 확인 후 얼마나 shift하는지
                break
            j -= 1  # 같으면 끝자리부터 첫번째자리까지 비교

        if j == -1:  # 모두 같으면 검색 성공
            answer = 1
            break
        else:  # 끝자리가 서로 같았지만 중간이 다른 경우 shift
            i += shift

    print('#{} {}'.format(test_case, answer))
