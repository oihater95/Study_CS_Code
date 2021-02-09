'''
0 => 출발, N => 종점
M개의 충전기, 최대 이동 정류장 수 K

입력
3
3 10 5
1 3 5 7 9
3 10 5
1 3 7 8 9
5 20 5
4 7 9 14 17

출력
#1 3
#2 0
#3 4
'''
T = int(input())

for test_case in range(1, T+1):
    knm = list(map(int, input().split()))
    charge = list(map(int, input().split()))
    K, N, M = knm[0], knm[1], knm[2]
    cnt = 0  # 충전 횟수
    distance = 0  # 위치

    for i in range(M-1):
        # 충전소 사이 거리 > K, 첫번째 충전소 > K, 마지막 충전소와 종점 거리 > K => 완주 X
        if K < (charge[i+1] - charge[i]) or K < (N - charge[-1]) or charge[0] > K:
            cnt = 0
            break
            
        # 최소 정류장, range(M-1)이라 마지막 위치에 대한 처리 필요
        else:
            # i+1번째 정류장이 현재위치 + K보다 멀면 현재위치를 i번째 정류장으로 옮기고 cnt++(충전)
            if distance + K < charge[i+1]:
                distance = charge[i]
                cnt += 1
                # 현재위치가 마지막에서 두번째 정류장일 때
                if distance == charge[-2]:
                    # 현재 위치 + K >= 종점이면 충전 X
                    if distance + K >= N:
                        break
                    # 현재 위치 + K < 종점이면 마지막 정류장에서 충전 필요
                    else:
                        distance = charge[i+1]
                        cnt += 1
            # 현재 위치 + K가 >= 마지막 정류장이고 종점보다 작다면 충전 필요
            if distance + K >= charge[-1] and distance + K < N:
                distance = charge[-1]
                cnt += 1

    print('#{} {}'.format(test_case, cnt))
