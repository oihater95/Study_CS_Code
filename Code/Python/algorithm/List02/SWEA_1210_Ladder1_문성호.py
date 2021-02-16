# 사다리 타기 => 당첨 시작점 찾기
# 끝점부터 역으로 시작점 찾기
for test_case in range(1, 11):
    N = int(input())
    arr = []

    for i in range(100):
        arr.append(list(map(int, input().split())))

    for i in range(100):  # 끝점 찾기
        if arr[99][i] == 2:
            end_idx = i
            break

    for i in range(99, -1, -1):  # 끝점 => 시작점
        if i == 0:  # 시작점 도달하면 시작점을 출력
            start = end_idx
            break
        if 0 < end_idx < 99:  # 양 쪽 끝이 아닐 경우
            if arr[i][end_idx - 1]:
                for j in range(end_idx-1, -1, -1):  #
                    if arr[i-1][j]:
                        end_idx = j
                        break

            elif arr[i][end_idx + 1]:
                for j in range(end_idx+1, 100):
                    if arr[i+1][j]:
                        end_idx = j
                        break

        elif end_idx == 0:
            if arr[i][end_idx + 1]:
                for j in range(end_idx+1, 100):
                    if arr[i+1][j]:
                        end_idx = j
                        break

        else:
            if arr[i][end_idx - 1]:
                for j in range(end_idx - 1, -1, -1):
                    if arr[i - 1][j]:
                        end_idx = j
                        break


    print('#{} {}'.format(test_case, start))