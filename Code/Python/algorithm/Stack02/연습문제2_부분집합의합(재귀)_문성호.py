def powerset(idx):
    if idx == N:
        result = 0
        ans = []
        for i in range(N):
            if sel[i]:
                result += arr[i]
                ans.append(arr[i])

        if result == 10:
            print(ans)


    else:
        for i in range(2):
            sel[idx] = i
            powerset(idx + 1)


arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
N = len(arr)
sel = [0] * N
print('합이 10인 부분집합들')
powerset(0)