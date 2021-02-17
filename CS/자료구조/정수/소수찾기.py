import math


def prime_brute(num):
    if 1 < num < 4:
        return True
    else:
        for i in range(2, num):
            if num % i == 0:
                return False
        else:
            return True


def prime_sqrt(num):
    if 1 < num < 4:
        return True
    else:
        for i in range(2, int(math.sqrt(num)) + 1):
            if num % i == 0:
                return False
        else:
            return True


print(prime_brute(17))
print(prime_sqrt(17))