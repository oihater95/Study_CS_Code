arr = [1, 2, 3]
N = 3
sel = [0] * N  # 뽑은 결과를 적음

# check => 10진수 정수
def permutation(idx, check):
    if idx == N:
        print(sel)
        return

    for j in range(N):
        if check & (1 << j): continue  # j번째 원소 사용했다면 다음 index로

        sel[idx] = arr[j]
        print((1<<j), check, check | (1<<j))
        permutation(idx+1, check | (1<<j))  # 일회성 사용이므로 원상복구가 필요없다

permutation(0, 0)

##########################################################################
arr = [1, 2, 3]
N = 3
sel = [0] * N  # 뽑은 결과 받기

def perm(idx, check):
    if idx == N:
        print(sel)

    for j in range(N):
        if check & (1 << j): continue  # 000 & 001 = 000 False

        else:
            sel[idx] = arr[j]
            # check = check | (i << j) 로 저장해버리면 원상복구하는 과정 필요
            perm(idx + 1, check|(1 << j))  # 000 | 001 = 001

perm(0, 0)  # check: 000부터
