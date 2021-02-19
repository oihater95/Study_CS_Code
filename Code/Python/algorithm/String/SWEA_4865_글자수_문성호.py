def my_max(arr):  # 리스트 중 최대값
    max_value = 0
    for i in range(len(arr)):
        if max_value < arr[i]:
            max_value = arr[i]

    return max_value


T = int(input())

for test_case in range(1, T+1):
    word_1 = input()
    word_2 = input()
    word_dict = dict()  # 빈 딕셔너리

    for char in word_1:  # 딕셔너리에 key 생성(key = word_1의 글자)
        if char not in word_dict.keys():
            word_dict[char] = 0  # 0으로 초기화

    for key in word_dict.keys():  # key와 word_2의 글자가 같다면 해당 key +1
        for j in word_2:
            if key == j:
                word_dict[key] += 1

    print('#{} {}'.format(test_case, my_max(list(word_dict.values()))))


