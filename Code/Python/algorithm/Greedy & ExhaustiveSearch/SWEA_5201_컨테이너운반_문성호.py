for tc in range(1, int(input())+1):
    N, M = map(int, input().split())  # N: 컨테이너 수, M: 트럭 수
    container = list(map(int, input().split()))
    truck = list(map(int, input().split()))
    ans = 0  # 운반 가능한 컨테이너 중량 합
    idx = 0  # 컨테이너 인덱스

    container = sorted(container, reverse=True)  # 무거운 순으로 정렬
    truck = sorted(truck, reverse=True)  # 적재용량 높은 순으로 정렬

    for i in range(M):  # i번째 트럭 운반
        if idx < N:  # 컨테이너 남아 있음
            for j in range(idx, N):  # idx번째 컨테이너부터 끝까지 순회
                if truck[i] >= container[j]:  # i번째 트럭 적재용량 > j번째 컨테이너 중량이면 운반
                    ans += container[j]  # 운반
                    idx = j+1  # idx 갱신 (무게 순으로 정렬했기 때문에 0 ~ j번째 컨테이너는 확인할 필요없다)
                    break  # 다음 트럭으로

        else:  # 컨테이너 모두 순회하면 끝냄
            break

    print('#{} {}'.format(tc, ans))