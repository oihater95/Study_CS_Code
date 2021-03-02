# 피보나치 재귀 => 중복되는 연산 너무 많음
def fibo(n):
    if n < 2:
        return n
    else:
        return fibo(n-1) + fibo(n-2)


print(fibo(10))


#####################################################################
# 피보나치 DP (Memoization), recursive
# 리스트 길이 미리 할당 X
# fibo(n)값을 계산하자마자 저장 실행시간 O(n)
# memo를 위한 배열 할당, 모두 0으로 초기화
# memo[0] = 0, memo[1] = 1  => 0과 1은 구하지 않음

def fibo_memo(n):
    global memo
    if n >= 2 and len(memo) <= n:  # len(memo) > n => 이미 값이 구해져있다
        memo.append(fibo_memo(n-1) + fibo_memo(n-2))
    return memo[n]

memo = [0, 1]

print(fibo_memo(40))
#####################################################################
# 피보나치 DP2, recursive
# 배열 크기 미리 할당
memo2 = [-1] * 21
memo2[0] = 0
memo2[1] = 1


def fibo_memo2(n):
    if memo2[n] == -1:  # 아직 안 구했다면
        memo2[n] = fibo_memo2(n-1) + fibo_memo2(n-2)

    return memo2[n]  # 이미 구해져있다면


print(fibo_memo2(10))

####################################################################
# 피보나치 iterative (bottom-up)
def fibo_iter(n):
    f = [0, 1]

    for i in range(2, n+1):
        f.append(f[i-1] + f[i-2])

    return f[n]

print(fibo_iter(10))