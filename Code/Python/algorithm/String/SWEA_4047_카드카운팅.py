T = int(input())

for test_case in range(1, T+1):
    deck = [['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13']
            for _ in range(4)]
    card = input()
    msg = ''  # 에러 메세지

    # 덱 중에 어떤 카드가 있는지, 덱에서 뺌
    for i in range(0, len(card), 3):
        if card[i] == 'S':  # 스페이드
            try:
                deck[0].remove(card[i+1:i+3])
            except:  # 이미 덱에서 뺀 경우 remove 에러처리
                msg += 'ERROR'

        elif card[i] == 'D':  # 다이아몬드
            try:
                deck[1].remove(card[i+1:i+3])
            except:
                msg += 'ERROR'

        elif card[i] == 'H':  # 하트
            try:
                deck[2].remove(card[i+1:i+3])
            except:
                msg += 'ERROR'

        elif card[i] == 'C':  # 클로버
            try:
                deck[3].remove(card[i+1:i+3])
            except:
                msg += 'ERROR'

    if msg == 'ERROR':
        print('#{} ERROR'.format(test_case))

    else:
        print('#{} {} {} {} {}'.format(test_case, len(deck[0]), len(deck[1]),
                                       len(deck[2]), len(deck[3])))

