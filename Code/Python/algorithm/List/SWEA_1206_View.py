def my_max(a, b):
    if a > b:
        return a
    # else:
    #     return b
    return b


for tc in range(1, 11):
    N = int(input())
    building = list(map(int, input().split()))

    ans = 0

    for idx in range(2, N-2):
        #my_max 전달인자로 2개를 가지니 왼쪽 두집 , 오른쪼두집 뽑힌 집들 을 이용해 함.
        max_h = my_max(my_max(building[idx-2], building[idx-1]) , my_max(building[idx+1], building[idx+2]))

        if building[idx] > max_h:
            ans += building[idx] - max_h

    print("#{} {}".format(tc, ans))
