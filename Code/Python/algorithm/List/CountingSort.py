arr = [0, 4, 1, 3, 1, 2, 4, 1]
cnt = [0] * (max(arr)+1)  # 카운트 리스트

for num in arr:  # 카운트
    cnt[num] += 1

for i in range(1, len(cnt)):  # 누적합
    cnt[i] = cnt[i-1] + cnt[i]

temp = [0] * len(arr)  # 정렬된 리스트

for i in range(len(arr)-1, -1, -1):
    temp[cnt[arr[i]]-1] = arr[i]
    cnt[arr[i]] -= 1

print(temp)