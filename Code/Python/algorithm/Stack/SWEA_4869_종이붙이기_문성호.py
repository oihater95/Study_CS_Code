T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    dp = [1, 3]  # 첫번째, 두번째 항
    # bottom-up
    for i in range(2, N//10): # 세번째 항부터, N//10 => 항으로 보기위함
        # i-1은 오른쪽에 세로종이하나만, i-2는 가로2개종이 or 정사각 종이
        result = dp[i-1] + dp[i-2] * 2
        dp.append(result)

    print('#{} {}'.format(test_case, dp[-1]))

##########################################################
# Top-down
def paper(size):
    if size == 0:
        return 1
    elif size < 0:
        return 0

    return paper(size-10) + paper(size-20)*2


T = int(input())

for tc in range(1+ T+1):
    N = int(input())
    print(tc, paper(N))

################################################
# 수학적 접근
T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    stack = [1, 3]
    for i in range(2, N//10):
        stack.append(stack[-2] + 2**(i))
    print('#{} {}'.format(test_case, stack[-1]))