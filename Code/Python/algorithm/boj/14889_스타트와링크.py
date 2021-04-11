def combination(num, count):  # num: 사람 번호, count: 현재 팀 인원 수
    global min_score
    if count == N//2:
        start_score = 0
        link_score = 0
        temp_start = start_team[:]
        link_team = list(set(list(range(1, N+1)))-set(temp_start))

        for i in range(N//2-1):
            for j in range(i+1, N//2):
                start_score += arr[start_team[i]-1][start_team[j]-1] + arr[start_team[j]-1][start_team[i]-1]
                link_score += arr[link_team[i]-1][link_team[j]-1] + arr[link_team[j]-1][link_team[i]-1]

        score_diff = abs(start_score - link_score)
        if min_score > score_diff:
            min_score = score_diff


    else:
        if num < N:
            start_team.append(num)
            combination(num+1, count+1)
            start_team.pop()
            combination(num+1, count)


N = int(input())
arr = []
min_score = 987654321
start_team = []

for i in range(N):
    arr.append(list(map(int, input().split())))

min_score = combination(1, 0)
print(min_score)