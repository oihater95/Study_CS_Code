for tc in range(1, int(input())+1):
    N = int(input())
    truck = [list(map(int, input().split())) for _ in range(N)]
    time = [False] * 24  # 해당 시간대에 작업 중인지 확인
    cnt = 0  # 시간 배정한 화물 수
    truck = sorted(truck, key=lambda x: x[1]-x[0])  # 작업시간 짧은 순으로 정렬

    for i in range(N):
        start, end = truck[i][0], truck[i][1]  # 시작시간, 완료시간
        for j in range(start, end):  # end+1이 아닌 end까지인 이유 => 작업 완료 시간에 작업 시작 가능
            if time[j]:  # 해당 시간대에 이미 할당된 화물이 있는 경우
                break
        else:  # 해당 시간대에 할당된 화물이 없는 경우
            cnt += 1
            for k in range(start, end):  # 작업 완료 시간에 작업 시작 가능
                time[k] = True  # 작업 체크

    print('#{} {}'.format(tc, cnt))