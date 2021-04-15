for tc in range(1, int(input())+1):
    num, cnt = input().split()
    numbers = list(map(int, num))
    cnt = int(cnt)
    ans = 0

    if cnt < len(numbers):
        for i in range(cnt):  # 모두 정렬 불가한 경우
            # i번째 자리에 올 수 구하기
            # 뒤에서부터 읽기 => [i:]에서 최대값이 여러개인 경우 자리수가 가장 낮은 최대값과 바꾸기 위함
            for j in range(len(numbers)-1, i, -1):
                swap_sort_idx = numbers[:cnt]
                if max(numbers[i:]) == numbers[j]:
                    idx = j
                    break
            numbers[i], numbers[idx] = numbers[idx], numbers[i]

    elif cnt == len(numbers):  # 큰 순서대로 모두 정렬하려면 카드 수만큼 이동하면 됨
        numbers = sorted(numbers, reverse=True)

    else:
        numbers = sorted(numbers, reverse=True)  # 카드 수만큼 이동횟수 사용하면 큰 순서로 모두 정렬
        cnt -= len(numbers)  # 남은 횟수
        swap_idx1, swap_idx2 = 0, 0

        # 같은 숫자 찾기
        for i in range(len(numbers)):
            if numbers.count(numbers[i]) > 1:
                for j in range(i+1, len(numbers)):
                    if numbers[j] == numbers[i]:
                        swap_idx1, swap_idx2 = i, j
                        break
        if swap_idx1 == 0 and swap_idx2 == 0:  # 같은 수 없는 경우
            for i in range(cnt):  # 남은 횟수만큼 1의자리와 10자리 바꿈
                numbers[-2], numbers[-1] = numbers[-1], numbers[-2]
        else:
            for i in range(cnt):  # 같은 수 있는 경우
                numbers[swap_idx1], numbers[swap_idx2] = numbers[swap_idx2], numbers[swap_idx1]

    for i in range(len(numbers)):
        ans += numbers[i] * (10 ** (len(numbers)-1-i))

    print('#{} {}'.format(tc, ans))