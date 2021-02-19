def palindrome(lst):  # 최대 회문 길이 반환 함수
    ans = 0

    for M in range(100, -1, -1):  # M = 회문 길이
        for i in range(100):
            for j in range(100-M+1):
                if lst[i][j:j+M] == lst[i][j:j+M][::-1]:  # 슬라이싱 활용 [::-1] -> reverse,
                    ans = M  # 가장 긴 회문 길이
                    return ans
    return ans


for test_case in range(1, 11):
    N = int(input())
    arr = []
    arr_transpose = [[0 for i in range(100)] for j in range(100)]  # 전치행렬 (가로 세로 바꾼 행렬)
    answer = 0

    for i in range(100):
        arr.append(list(input()))

    for i in range(100):  # 전치행렬 만들기
        for j in range(100):
            arr_transpose[i][j] = arr[j][i]

    if palindrome(arr) >= palindrome(arr_transpose):  # 가로 회문 vs 세로 회문
        answer = palindrome(arr)
    else:
        answer = palindrome(arr_transpose)

    if answer == 0:  # 회문 없을 경우 1
        answer = 1

    print('#{} {}'.format(test_case, answer))