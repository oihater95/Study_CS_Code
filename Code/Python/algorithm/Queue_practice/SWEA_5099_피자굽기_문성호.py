for tc in range(1, int(input())+1):
    N, M = map(int, input().split())  # 화덕크기 피자 갯수
    pizza_cheese = list(map(int, input().split()))
    oven = [0] * N
    pizza_index = list(range(1, N+1))  # 화덕 안의 피자 번호
    idx = 0
    # 피자 화덕에 넣기
    for i in range(N):
        if oven[i] == 0:
            oven[i] = pizza_cheese.pop(0)
    # 화덕이 다 비워 질 때까지 굽기
    while True:
        oven[idx % N] //= 2  # 1번 자리 치즈 절반(원형 큐 개념으로 나머지연산 사용)

        if oven[idx % N] == 0:  # 다 구워진 경우
            if pizza_cheese:  # 교체할 피자가 남아있으면 피자 교체
                oven[idx % N] = pizza_cheese.pop(0)  # 피자 교체
                pizza_index[idx % N] = max(pizza_index) + 1  # 교체한 피자 번호 갱신
                idx += 1
                continue
            else:
                last = pizza_index[idx % N]  # 마지막 피자 번호
                pizza_index[idx % N] = 0  # 비어있는 화덕이 되니까 피자 번호 0
        idx += 1

        for i in range(N):  # 오븐이 모두 비었으면 while break
            if oven[i] != 0:
                break
        else:
            break

    print('#{} {}'.format(tc, last))