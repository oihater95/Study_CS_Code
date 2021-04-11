T = int(input())

for test_case in range(1, T+1):
    N = int(input())  # 돌아가야하는 학생 수
    student = []  # 학생 이동해야하는 방
    path = [0] * 200  # 경로

    for i in range(N):  # 0번 인덱스가 출발, 1번 인덱스가 도착
        student.append(sorted(list(map(int, input().split()))))

    for i in range(N):
        cnt = 0  # 겹치는 수
        # (1, 2) => 0번, (3, 4) => 1번, (5, 6) => 2번 ...
        for j in range((student[i][0]-1)//2, (student[i][1]-1)//2 + 1):
            path[j] += 1

    # 최댓값만큼 시간이 소요된다
    print('#{} {}'.format(test_case, max(path)))
