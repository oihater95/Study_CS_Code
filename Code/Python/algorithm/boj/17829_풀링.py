import math
from copy import deepcopy

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
K = int(math.log2(N))

for l in range(K):
    result_arr = []
    for i in range(N//2):
        result_row = []

        for j in range(N//2):
            temp = []
            temp.append(arr[2 * i][2 * j])
            temp.append(arr[2 * i + 1][2 * j])
            temp.append(arr[2 * i][2 * j + 1])
            temp.append(arr[2 * i + 1][2 * j + 1])
            temp = sorted(temp, reverse=True)
            result_row.append(temp[1])

        result_arr.append(result_row)

    arr = deepcopy(result_arr)
    N //= 2

print(arr[0][0])
