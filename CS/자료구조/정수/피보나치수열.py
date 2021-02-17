# 재귀함수 이용 (O(2^n))
def fib_recursive(n):
    if n < 2:
        return n
    else:
        return fib_recursive(n-1) + fib_recursive(n-2)


# 피보나치 수열 (O(n))
def fib(n):
    if n < 2:
        return n
    else:
        num1, num2 = 0, 1
        for i in range(n):
            num1, num2 = num2, num1 + num2

        return num1

print(fib(10))
print(fib_recursive(10))