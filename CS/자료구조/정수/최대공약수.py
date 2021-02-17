# 최대공약수 GCD
def gcd(a, b):
    while b:
        result = b
        a, b = b, a % b
    return result

print(gcd(16, 12))