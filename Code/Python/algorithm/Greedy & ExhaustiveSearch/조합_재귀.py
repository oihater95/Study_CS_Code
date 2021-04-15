# nCr
n = 5
r = 3
arr = [1, 2, 3, 4, 5]
sel = [0] * r

def combination(idx, sel_idx):
    if sel_idx == r:
        print(sel)
        return

    if idx == n:
        return

    sel[sel_idx] = arr[idx]
    combination(idx+1, sel_idx+1)  # 뽑고 가기
    combination(idx+1, sel_idx)  # 안뽑고 가기

combination(0, 0)