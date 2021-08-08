def primeCheck(num):
    if num == 1:
        return False
    else:
        for i in range(2, int(num**0.5) + 1):  # 제곱근 이용 소수 판정
            if num % i == 0:
                return False
        return True


def palindromeCheck(num):
    num = str(num)
    reverseNum = num[::-1]  # 뒤집기

    if num == reverseNum:
        return True
    else:
        return False


n = int(input())
while True:
    if primeCheck(n) and palindromeCheck(n):
        print(n)
        break
    else:
        n += 1