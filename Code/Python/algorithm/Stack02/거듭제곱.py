# 반복문 사용한 선형시간 O(n)

def iteraive_power(x, n):  # 2^8 => 7번 연산
    result = 1

    for i in range(1, n+1):
        result *= x

        return result

# 분할 정복 거듭제곱 O(logn)
def Recursive_power(x, n):  # 2^8 => 2*2*2*2 * 2*2 * 2 * 2  => 4번연산?
    if n == 1: return x
    if n % 2 == 0:
        y = Recursive_power(x, n//2)
        return y * y
    else:
        y = Recursive_power(x, (n-1) // 2)
        return y * y * x