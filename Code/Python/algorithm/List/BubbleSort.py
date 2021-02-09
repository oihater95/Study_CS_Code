nums = [55, 7, 78, 12, 42]

for i in range(len(nums)):
    for j in range(len(nums)-1):  # 정렬된 뒷 부분도 확인
        if nums[j] > nums[j+1]:
            nums[j], nums[j+1] = nums[j+1], nums[j]
            nums
print(nums)

arr = [55, 7, 78, 12, 42]
for i in range(len(arr)-1, 0, -1):
    for j in range(i):  # 정렬된 뒷 부분은 제외
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]

print(arr)
