from collections import deque

for tc in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    trees = deque()
    ans = 0

    for i in range(n):
        if i % 2:
            trees.appendleft(arr[i])
        else:
            trees.append(arr[i])

    for i in range(n-1):
        if ans < abs(trees[i] - trees[i+1]):
            ans = abs(trees[i] - trees[i+1])

    if ans < abs(trees[0] - trees[-1]):
        ans = abs(trees[0] - trees[-1])

    print(ans)