def power(b, e, ans, answer):
    if e == 0:
        answer.append(ans)  # 정답 리스트
        return

    ans *= b # b를 e번 곱한다
    e -= 1  # 한번 곱할 때 마다 e - 1
    power(b, e, ans, answer)


for tc in range(1, 11):
    N = int(input())
    base, exp = map(int, input().split())  # 밑과 지수
    result = 1
    answer = []  # 정답을 담을 리스트, test case 갱신될때 리스트도 빈 리스트로 갱신
    power(base, exp, result, answer)
    print('#{} {}'.format(tc, answer[0]))