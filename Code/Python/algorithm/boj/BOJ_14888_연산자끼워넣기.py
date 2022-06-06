n = int(input())
numbers = list(map(int, input().split()))
plus, minus, mul, div = map(int, input().split())
max_result = -987654321
min_result = 987654321

def dfs(idx, num):
    global plus, minus, mul, div, max_result, min_result

    if idx == n:
        max_result = max(max_result, num)
        min_result = min(min_result, num)

    else:
        if plus > 0:
            plus -= 1
            dfs(idx + 1, num + numbers[idx])
            plus += 1

        if minus > 0:
            minus -= 1
            dfs(idx + 1, num - numbers[idx])
            minus += 1

        if mul > 0:
            mul -= 1
            dfs(idx + 1, num * numbers[idx])
            mul += 1

        if div > 0:
            div -= 1
            # // 을 사용할 경우, 음수를 양수로 나눌 때의 기준 C++14(양수로 나눈 후 음수로 변환)와 다르기 때문에 다른 값을 얻음
            dfs(idx + 1, int(num / numbers[idx]))
            div += 1

dfs(1, numbers[0])

print(max_result)
print(min_result)
