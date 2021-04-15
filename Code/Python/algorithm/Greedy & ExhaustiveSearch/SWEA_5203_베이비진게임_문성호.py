def check_run(p):
    if p[-1] - 2 in p and p[-1] - 1 in p:  # 연속한 수 3개
        return True

    elif p[-1] + 2 in p and p[-1] + 1 in p:  # 연속한 수 3개
        return True

    elif p[-1] - 1 in p and p[-1] + 1 in p:  # 연속한 수 3개
        return True

    else:
        return False


def check_triplet(p):
    if p.count(p[-1]) == 3:  # 같은 수 3개
        return True
    else:
        return False


for tc in range(1, int(input())+1):
    draw = list(map(int, input().split()))
    player_1, player_2 = [], []
    ans = 0  # 무승부

    for i in range(12):
        if i % 2 == 0:
            player_1.append(draw[i])  # player1 카드 뽑음
            if i >= 4:  # player1 3장이상
                if check_run(player_1):  # run일 경우
                    ans = 1  # 1 승리
                    break  # 게임 끝

                elif check_triplet(player_1):  # triplet일 경우
                    ans = 1  # 1 승리
                    break  # 게임 끝

        else:
            player_2.append(draw[i])  # player2 카드 뽑음
            if i >= 5:  # player2 3장이상
                if check_run(player_2):  # run일 경우
                    ans = 2  # 2 승리
                    break  # 게임 끝

                elif check_triplet(player_2):  # triplet일 경우
                    ans = 2  # 2 승리
                    break  # 게임 끝

    print('#{} {}'.format(tc, ans))