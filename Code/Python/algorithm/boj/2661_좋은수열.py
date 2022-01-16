def check(string):

    for i in range(1, len(string)//2 + 1):
        if string[-i:] == string[-2 * i: -i]:
            return False
    else:
        return True


def backTracking(num):
    global n

    if len(num) == n:
        print(num)
        exit()

    for i in '123':
        if check(num + i):
            backTracking(num + i)
    return

n = int(input())
backTracking('1')

