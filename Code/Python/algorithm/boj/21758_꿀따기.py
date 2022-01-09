# 55점
N = int(input())
honey = list(map(int, input().split()))

# 벌통이 오른쪽 끝에 있는 경우(벌 1마리는 왼쪽 끝)
bee_1, store, temp_1 = 0, N-1, 0
sum_honey = sum(honey[1:N])
for i in range(1, N-1):
    temp = sum_honey - honey[i] + sum(honey[i+1:N])
    if temp > temp_1:
        temp_1 = temp

# 벌통이 왼쪽 끝에 있는 경우 (벌 1마리는 오른쪽 끝)
bee_1, store, temp_2, = N-1, 0, 0
sum_honey = sum(honey[0:N-1])

for i in range(1, N-1):
    temp = sum_honey - honey[i] + sum(honey[0:i])
    if temp > temp_2:
        temp_2 = temp

# 벌통이 벌 사이에 있는 경우(벌 두 마리는 왼쪽, 오른쪽 끝에 위치, 벌통은 그 사이 가장 꿀 많은 곳에 위치)
# 벌통이 꿀 가장 많은 곳에 위치하는 이유: 벌통 위치만 중복 될 것이기 때문에
temp_3 = sum(honey[1:N-1]) + max(honey[1:N-1])

print(max(temp_1, temp_2, temp_3))


####################
# 100점
#
# # 벌통을 가운데에 뒀을 때
# a = sum(honey[1 : n-1]) + max(honey[1 : n-1])
# # 벌통을 왼쪽에 뒀을 때
# left = l_total = sum(honey[1:n])
# l_max = r_max = 0
# for i in range(1, n-1):
#     l_total -= 2 * honey[i]
#     if l_max < l_total:
#         l_max = l_total
#     l_total += honey[i]
# # 벌통을 오른쪽에 뒀을 때
# right = r_total = sum(honey[0:n-1])
# for i in range(n-2, -1, -1):
#     r_total -= 2 * honey[i]
#     if r_max < r_total:
#         r_max = r_total
#     r_total += honey[i]
# print(max(a, l_max + left, r_max + right))