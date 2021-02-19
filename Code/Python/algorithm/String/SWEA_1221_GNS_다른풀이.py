T = int(input())

for test_case in range(1, T+1):
    str_num = ['ZRO', 'ONE', 'TWO', 'THR', 'FOR', 'FIV', 'SIX', 'SVN', 'EGT', 'NIN']
    str_dict = {}
    result = []
    tc, N = map(str, input().split())
    N = int(N)
    arr = list(map(str, input().split()))
    cnt = [0] * 10  # 각 단어가 나온 수

    for value, key in enumerate(str_num):  # 각 단어가 의미하는 값
        str_dict[key] = value

    for word in arr:  # 각 단어 카운팅
        cnt[str_dict[word]] += 1

    for i in range(len(cnt)):
        word = str_num[i]
        result.extend([word] * cnt[i])

    print('#{}'.format(test_case))
    print(' '.join(result))
