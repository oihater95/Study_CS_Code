import heapq
import sys

heap = []  # heapq 모듈은 최소힙만 가능
N = int(input())

for i in range(N):
    cmd = int(sys.stdin.readline())

    if cmd:
        heapq.heappush(heap, -cmd)

    else:
        if len(heap):
            print(-heapq.heappop(heap))
        else:
            print(0)

