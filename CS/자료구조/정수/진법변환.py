# n진법 -> 10진법 (n= 2 ~ 9)
def convert_to_decimal(number, base):
    result = 0
    i = 0
    while number > 0:
        result += (base**i) * (number % 10)
        i += 1
        number //= 10

    return result


# 10진법 -> n진법 (n = 2 ~ 9)
def convert_from_decimal(number, base):
    result = 0
    i = 1
    while number > 0:
        result += (number % base) * i
        number //= base
        i *= 10

    return result


# 10진법 -> n진법 재귀(n = 2 ~ 20진법)
def convert_from_dec_recursive(number, base):
    converting = '0123456789ABCDEFGHIJ'
    if number < base:
        return converting[number]
    else:
        return convert_from_dec_recursive(number // base, base) + str(number % base)


print(convert_to_decimal(1001, 2))
print(convert_from_decimal(9, 2))
print(convert_from_dec_recursive(9, 2))
print(convert_from_dec_recursive(100, 16))
