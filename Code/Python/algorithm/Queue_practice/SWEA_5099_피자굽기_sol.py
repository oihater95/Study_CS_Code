
for tc in range(1, int(input())+1):
    N, M = map(int, input().split())  # 화덕크기 피자 갯수
    pizza_cheese = list(map(int, input().split()))
    oven = []

    for i in range(N):
        oven.append((i+1, pizza_cheese[i]))  # 피자번호는 1번부터 시작 (피자번호와 치즈 튜플로 묶음)

    next_pizza = N
    # last_pizza = -1

    while len(oven) > 1:  # 모든 피자가 녹을 때까지 하지 않고 피자 하나 남으면 끝내도 됨
    # while oven:
        num, cheese = oven.pop(0)  # num: 피자번호, cheese: 남은 치즈

        cheese //= 2
        # last_pizza = num
        # 치즈의 양이 남아있다면 다시 화덕에 넣는다. 맨 뒷순서로
        if cheese:
            oven.append((num, cheese))
        else:
            if next_pizza < M:  # 피자 남았다면
                oven.append((next_pizza+1, pizza_cheese[next_pizza]))
                next_pizza += 1

    # print('#{} {}'.format(tc, last_pizza))
    print('#{} {}'.format(tc, oven[0][0]))