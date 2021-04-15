arr = [1, 2, 3, 4, 5]
n, r = 5, 3
sel = [0] * r
# nCr

def combination(idx, sel_idx):
    if sel_idx == r:
        print(sel)
        return

    if idx == n:
        return

    else:
        sel[sel_idx] = arr[idx]
        combination(idx+1, sel_idx+1)
        combination(idx+1, sel_idx)

combination(0, 0)
