'''
N = 노선 개수
A, B = i번째 버스가 다니는 정류장 번호 범위
P = 버스 정류장 개수
C = 버스 정류장 번호
'''

T = int(input())

for test_case in range(1, T+1):
    N = int(input())  # 버스 노선 개수
    bus = []  # 각 버스가 다니는 정류장 저장할 리스트

    for i in range(N):
        AB = list(map(int, input().split()))  # A, B
        bus.append(AB)  # [[1, 3], [2, 5], ...]

    P = int(input())  # 버스 정류장 개수
    bus_stop = [0] * 5001  # 모든 버스 정류장 리스트

    for A, B in bus:  # 각 버스 노선이 지나가는 정류장에 +1
        for j in range(A, B+1):
            bus_stop[j] += 1

    bus_num = []
    for i in range(P):
        bus_num.append(bus_stop[int(input())])

    print('#{} {}'.format(test_case, ' '.join(map(str, bus_num))))

############################################################

T = int(input())

for test_case in range(1, T+1):
    N = int(input())  # 버스 노선 개수
    bus_stop = [0] * 5001  # 모든 정류장 리스트

    for i in range(N):
        A, B = map(int, input().split())
        for j in range(A, B+1):  # 해당 정류장에 지나는 버스 수
            bus_stop[j] += 1

    P = int(input())  # 확인하고 싶은 버스 정류장의 수

    print('#{}'.format(test_case), end=" ")
    for i in range(P):
        C = int(input())  # 확인하고 싶은 정류장의 번호
        print(bus_stop[C], end=" ")
    print()
