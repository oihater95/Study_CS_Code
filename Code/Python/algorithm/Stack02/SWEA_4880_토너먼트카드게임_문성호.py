def game(l, r):  # 가위바위보, 가위: 1, 바위: 2, 보: 3
    # 인덱스는 0부터 시작하므로 인덱스 접근 시 -1
    # 왼쪽이 이기거나 비김
    if card[l-1] == card[r-1]:  # 비김
        return l
    elif card[l-1] == 1 and card[r-1] == 3:  # 가위 vs 보
        return l
    elif card[l-1] == 2 and card[r-1] == 1:  # 바위 vs 가위
        return l
    elif card[l-1] == 3 and card[r-1] == 2:  # 보 vs 가위
        return l
    # 오른쪽이 이김
    return r

# 분할 재귀, 전체 반을 나누고 왼쪽부터 반 씩 나눔, left에 하나, right에 하나 남을 때 가위바위보
# 1 2 3 4 5 6 7 => 1 2 3 4 / 5 6 7 => 1 2 / 3 4 / 5 6 7 => 1 3 / 5 6 / 7 => 1 3 / 5 7 => 3 5 => 3
def division(first, second):
    if first == second:
        return first
    left = division(first, (first+second)//2)
    right = division((first+second)//2 + 1, second)
    return game(left, right)


for tc in range(1, int(input())+1):
    N = int(input())
    card = list(map(int, input().split()))
    start = 1
    end = N

    print('#{} {}'.format(tc, division(start, end)))