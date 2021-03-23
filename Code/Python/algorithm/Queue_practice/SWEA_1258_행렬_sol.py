def search_size(r, c):
    r_cnt = 0
    c_cnt = 0

    # 행의 크기 찾기
    for i in range(r, N):
        if arr[i][c] != 0:
            r_cnt += 1
        else:
            break
    # 열의 크기 찾기
    for i in range(c, N):
        if arr[r][i] != 0:
            c_cnt += 1
        else:
            break

    ans.append([r_cnt, c_cnt, r_cnt*c_cnt])
    init(r, c, r_cnt, c_cnt)


# 카운트 한 곳은 0으로 초기화
def init(r, c, r_cnt, c_cnt):
    for i in range(r, r+r_cnt):
        for j in range(c, c+c_cnt):
            arr[i][j] == 0


def counting_sort(idx):  # idx를 기준으로 카운팅 정렬
    cnt = [0] * 10001  # 문제에서 제시된 행렬 최대 크기 100*100, 각 원소가 몇 개 들었는지 카운트
    sort_ans = [0] * len(ans)  # 정렬된 리스트

    # 카운팅
    for i in range(len(ans)):
        cnt[ans[i][idx]] += 1

    # 누적합
    for i in range(1, len(cnt)):
        cnt[i] += cnt[i-1]

    # 정렬
    for i in range(len(ans) - 1, -1, -1):
        sort_ans[cnt[ans[i][idx]]-1] = ans[i]
        cnt[ans[i][idx]] -= 1

    return sort_ans



for tc in range(1, int(input())+1):
    N = int(input())  # 전체 크기
    arr = []  # 입력배열
    ans = []

    for i in range(N):
        arr.append(list(map(int, input().split())))

    # 시작점
    for i in range(N):
        for j in range(N):
            if arr[i][j] != 0:
                search_size(i, j)

    # 카운팅 정렬 행 기준으로 먼저 정렬 후에 곱 기준으로 정렬. => 카운팅 정렬은 안정정렬인 것을 이용
    ans = counting_sort(0)  # 행 기준
    ans = counting_sort(2)  # 곱 기준

    print('#{} {}'.format(tc, len(ans)), end=' ')
    for i in range(len(ans)):
        print('{} {}'.format(ans[i][0], ans[i][1]), end=' ')
    print()

########################################################################
# 내장함수 사용
for tc in range(1, int(input())+1):
    N = int(input())  # 전체 크기
    arr = []  # 입력배열
    ans = []

    for i in range(N):
        arr.append(list(map(int, input().split())))

    # 시작점
    for i in range(N):
        for j in range(N):
            if arr[i][j] != 0:
                r, c = i, j
                # 범위를 앞에 위치
                while r < N and arr[r][j] != 0:
                    r += 1
                while c < N and arr[i][c] != 0:
                    c += 1

                ans.append([r-i, c-j])

                # 초기화
                for a in range(i, r):
                    for b in range(j, c):
                        arr[a][b] = 0

    # 먼저 x[0]*x[1]기준으로 정렬 후 그 안에서 x[0]을 기준으로 정렬
    ans.sort(key = lambda x: (x[0]*x[1], x[0]))
