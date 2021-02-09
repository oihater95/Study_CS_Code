nums = [1, 2, 3, 5, 5, 5]
cnt = [0] * 10

for num in nums:
    cnt[num] += 1

run = False
tri = False

if cnt[0] >= 3:
    tri = True
    cnt[0] -= 3
elif cnt[len(cnt)-1] >= 3:
    tri = True
    cnt[len(cnt)-1] -= 3

for i in range(1, len(cnt)-1):
    # tri
    if cnt[i] >= 3:
        tri = True
        cnt[i] -= 3
    # run
    if cnt[i] == 1 and cnt[i-1] == 1 and cnt [i+1] == 1:
        run = True

if tri and run:
    print('baby-gin')
else:
    print('nope')