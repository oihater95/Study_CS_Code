# 부분집합의 합
# 부분 집합의 합이 10이 되는 값들을 모두 출력
arr = list(map(int, input().split()))

print('original array: ', arr)
print()
print('합이 10인 부분집합')

for i in range(1 << len(arr)):  # 2^len(arr)
    result = 0
    temp = []
    for j in range(len(arr)+1):  # len(arr)만큼의 자리수 순회
        if i & (1 << j):  # i의 j번째 수가 1인지, 1이면 j번째 원소 추가
            temp.append(arr[j])
            result += arr[j]
    if result == 10:
        print(temp)
