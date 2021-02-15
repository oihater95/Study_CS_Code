# 공집합을 포함한 부분집합의 수는 2^n개
# 부분집합 (2진수)
bit = [0] * 4

for i in range(2):
    bit[0] = i
    for j in range(2):
        bit[1] = j
        for k in range(2):
            bit[2] = k
            for l in range(2):
                bit[3] = l
                print(bit)

arr = [1, 2, 3, 4]
for i in range(1 << len(arr)):  # 1 << n == 2^n
    for j in range(len(arr)+1):  # 원소의 수만큼 비트 비교
        if i & (1 << j):  # i의 j번째 비트가 1이면 j번째 원소 출력
            print(arr[j], end=', ')
    print()
print()
