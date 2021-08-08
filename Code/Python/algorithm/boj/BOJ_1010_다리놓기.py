for tc in range(1, int(input())+1):
    N, M = map(int, input().split())
    factorial = [1] * (M+1)

    # factorial 리스트
    for i in range(2, M+1):
        factorial[i] = factorial[i-1] * i

    # mCn => 순서를 따지지 않는다, m개 중 n개를 뽑아 정렬하면 가능한 경우가 됨
    ans = factorial[M] // (factorial[N] * factorial[M-N])
    print(ans)

