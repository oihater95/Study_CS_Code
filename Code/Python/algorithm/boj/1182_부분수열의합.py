def partial(idx, tmp):
    global ans, S

    if sum(tmp) == S:
        ans += 1

    if idx+1 < len(arr):
        for i in range(idx+1, len(arr)):
            tmp.append(arr[i])
            partial(i, tmp)
            tmp.pop()


N, S = map(int, input().split())
if N >= 2:
    arr = list(map(int, input().split()))
else:
    arr = [int(input())]
ans = 0
arr.sort()

for i in range(N):
    temp = [arr[i]]
    partial(i, sum(temp))

print(ans)

######################################
# 다른 풀이
# cnt = 0
# def dfs(idx, total):
#     global ans
#
#     if idx >= N:
#         return
#     total += arr[idx]
#     if total == S:
#         ans += 1
#     dfs(idx + 1, total - arr[idx])
#     dfs(idx + 1, total)
#
# dfs(0, 0)
# print(ans)