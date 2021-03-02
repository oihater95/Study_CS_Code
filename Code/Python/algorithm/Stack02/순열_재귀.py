arr = [1, 2, 3]

N = len(arr)
sel = [0] * N  # 결과들이 저장될 리스트
check = [0] * N  # 해당 원소를 사용했는지 안했는지에 대한 체크 0: 미사용 1: 사용

def permutation(idx):
    if idx == N:
        print(sel)

    else:
        for i in range(N):
            if check[i] == 0:  # i번째 자리 아직 안썼다면 사용
                sel[idx] = arr[i]
                check[i] = 1  # 사용했다는 표시
                permutation(idx+1)
                check[i] = 0  # 다음 반복문을 위해 원상복구

permutation(0)
print()


#################################
# nPr

arr2 = [1, 2, 3, 4, 5]
N2 = len(arr2)
sel2 = [0] * 3  # 5P3
check2 = [0] * N2

def permutation2(idx):
    if idx == 3:  # 5P3
        print(sel2)

    else:
        for i in range(N2):
            if check2[i] == 0:  # i번째 자리 아직 안썼다면 사용
                sel2[idx] = arr2[i]
                check2[i] = 1  # 사용했다는 표시
                permutation2(idx+1)
                check2[i] = 0  # 다음 반복문을 위해 원상복구

permutation2(0)

