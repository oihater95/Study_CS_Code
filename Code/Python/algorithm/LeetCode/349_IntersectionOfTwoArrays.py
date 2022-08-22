# nums1 = [1,2,2,1]
# nums2 = [2,2]

nums1 = [4,9,5]
nums2 = [9,4,9,8,4]


# 풀이 1
set_nums1 = set(nums1)
set_nums2 = set(nums2)

print(list(set_nums1.intersection(set_nums2)))


# 풀이 2
result = []

for i in range(len(nums1)):
    if nums1[i] in nums2 and nums1[i] not in result:
        result.append(nums1[i])

print(result)