def check():
    ans = 0
    # 정렬
    card_nums.sort()
    for key in card.keys():
        card[key].sort()

    # 1번 규칙 & 4번 규칙
    for key, value in card.items():
        if len(card[key]) == 5:  # 모두 같은 색
            num = card[key][0]
            continuous = list(range(num, num + 5))  # 연속된 숫자
            if card[key] == continuous:
                ans += 900 + card[key][-1]
                return ans
            else:
                ans += 600 + card[key][-1]
                return ans

    # 2번, 3번, 6번
    cnt = []
    number = []
    for n in card_nums:
        cnt.append(card_nums.count(n))
        number.append(int(n))
    max_cnt = max(cnt)
    # 2번 규칙
    if max_cnt == 4:
        ans += 800 + number[cnt.index(4)]
        return ans

    # 3번 규칙
    elif max_cnt == 3:
        if 2 in cnt:
            ans += number[cnt.index(3)]*10 + number[cnt.index(2)] + 700
            return ans

        # 6번 규칙
        else:
            ans += number[cnt.index(3)] + 400
            return ans

    # 7번, 8번
    elif max_cnt == 2:
        cnt_num = []
        for i in range(5):
            if cnt[i] == 2:
                cnt_num.append(number[i])
        # 7번
        if len(cnt_num) == 4:
            cnt_num = sorted(list(set(cnt_num)))
            ans += cnt_num[0] + cnt_num[1]*10 + 300
            return ans
        elif len(cnt_num) == 2:
            ans += 200 + cnt_num[0]
            return ans

    # 5번 규칙
    continuous = list(range(card_nums[0], card_nums[0] + 5))  # 연속된 숫자
    if card_nums == continuous:
        ans += 500 + card_nums[-1]
        return ans

    return 100 + card_nums[-1]
card = {
    'R': [],
    'B': [],
    'Y': [],
    'G': []
}
card_nums = []

for i in range(5):
    C, N = map(str, input().split())
    card[C].append(int(N))
    card_nums.append(int(N))


print(check())
