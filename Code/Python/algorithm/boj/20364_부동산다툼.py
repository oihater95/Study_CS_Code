import sys
N, Q = map(int, sys.stdin.readline().split())
visited = set()  # 리스트로 하면 시간초과

for i in range(Q):
    ans = 0
    estate = int(sys.stdin.readline())
    node = estate

    while node > 0:
        if node in visited:  # 점유되어 있음
            ans = node
        node //= 2
    if ans == 0:  # 점유되어 있지 않음
        visited.add(estate)

    print(ans)