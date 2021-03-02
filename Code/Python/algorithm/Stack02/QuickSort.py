# 호어 파티션
def partition(a, begin, end):
    pivot = (begin + end) // 2  # pivot = 가운데
    L = begin
    R = end
    while L < R:
        while(a[L] < a[pivot] and L < R): L += 1  # L: 오른쪽으로 이동하며 피봇보다 크거나 같은 원소 찾기
        while (a[R] >= a[pivot] and L < R): R -= 1  # R: 왼쪽으로 이동하며 피봇보다 작은 원소 찾기

        if L < R:
            if L == pivot:
                pivot = R
            a[L], a[R] = a[R], a[L]

    a[pivot], a[R] = a[R], a[pivot]  # 피봇 위치 확정

    return R

def quickSort(a, begin, end):
    if begin < end:
        p = partition(a, begin, end)
        quickSort(a, begin, p-1)  # 왼쪽 부분 집합 정렬
        quickSort(a, p+1, end)  # 오른쪽 부분 집합 정렬