import math
N = int(input())  # 총 시험장 수
people = list(map(int, input().split()))
B, C = map(int, input().split())  # 총감독, 부감독 감시 인원
cnt = 0  # 필요한 감독관 수

for i in range(N):
    people[i] -= B
    cnt += 1
    if people[i] > 0:
        cnt += math.ceil(people[i] / C)  # 올림 사용

print(cnt)