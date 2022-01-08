T = int(input())
for tc in range(T):
    N = int(input())
    arr = list(map(int, input().split()))
    ans = []

    while len(arr) < N:
        arr.extend(list(map(int, input().split())))

    for i in range(N):
        if i % 2 == 0:
            arr_sort = arr[:i+1]
            arr_sort = sorted(arr_sort)
            ans.append(arr_sort[len(arr_sort) // 2])

    print(len(ans))
    for i in range(len(ans)):
        if i != 0 and i % 10 == 0:
            print()

        print(ans[i], end=" ")
    print()
