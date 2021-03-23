for tc in range(1, 11):
    t = int(input())
    data = list(map(int, input().split()))  # 데이터 큐
    flag = True

    while flag:
        cnt = 1  # 1 ~ 5까지 뺌
        for i in range(5):  # 한 사이클은 5
            # pop(0) - cnt 한 값을 삽입
            tmp = data.pop(0) 
            tmp -= cnt
            cnt += 1
            # 0보다 작거나 같으면 0으로 설정 후 0을 삽입하고 동작을 멈춘다
            if tmp <= 0:
                tmp = 0
                data.append(tmp)
                flag = False
                break
            data.append(tmp)

    print('#{} {}'.format(tc, ' '.join(map(str, data))))
