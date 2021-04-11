N = int(input())
P = list(map(int, input().split()))  # 돈 뽑는데 걸리는 시간
P.sort()  # 누적합이기 때문에 오름차순 정렬이 최소 누적합 (0번째 인덱스는 N번 더해짐, 1번째는 N-1번 ...)
total = 0
for i in range(N):
    total += P[i] * (N-i)

print(total)