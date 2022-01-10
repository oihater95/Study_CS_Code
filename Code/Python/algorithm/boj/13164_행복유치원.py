N, K = map(int, input().split())  # 원생 수, 조 수
kids = list(map(int, input().split()))
ans = 0
cnt = 0
idx = []
diff = []  # (인접 원생 키 차이, idx) 리스트

# 조가 1개
if K == 1:
    print(max(kids) - min(kids))
    exit()

# 각 조에 1명씩만
elif K == N:
    print(0)
    exit()

# 인접한 원생과 키 차이 가장 많이 나는 구간부터 조 나누기
for i in range(N-1):
    diff.append([kids[i+1] - kids[i], i+1])

diff = sorted(diff, key=lambda x: x[0], reverse=True)
for i in range(K-1):
    idx.append(diff[i][1])

# 나눠지는 구간
idx = sorted(idx)

# 구간별 최대-최소 더하기
for i in range(len(idx)):
    if i == 0:
        ans += max(kids[:idx[i]]) - min(kids[:idx[i]])
    else:
        ans += max(kids[idx[i-1]:idx[i]]) - min(kids[idx[i-1]:idx[i]])

        if i == len(idx) - 1:
            ans += max(kids[idx[i]:]) - min(kids[idx[i]:])

print(ans)

######################################
# 더 좋은 풀이
'''
n - k개의 조만 비교하면 됨, diff 오름차순으로 sum 바로 구함
n, k = map(int, input().split())
a = list(map(int, input().split()))
diff = []
for i in range(1, n):
    diff.append(a[i] - a[i - 1])

diff.sort()
sum = 0
for i in range(n - k):
    sum += diff[i]
print(sum)
'''

