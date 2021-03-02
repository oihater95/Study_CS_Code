arr = [1, 2, 3, 4, 5]
N = 5

def permutation(idx):
    if idx == N:
        print(arr)

    else:
        for i in range(idx, N):
            arr[idx], arr[i] = arr[i], arr[idx]
            permutation(idx + 1)
            arr[idx], arr[i] = arr[i], arr[idx]  # 다음 인덱스에서 사용하기 위해 원상복구


permutation(0)