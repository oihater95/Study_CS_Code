T = int(input())

for test_case in range(1, T+1):
    process = input()
    pipe = 0  # 파이프 수
    cnt = 0  # 파이프 조각 수
    process += ' '  # out of index 방지

    for i in range(len(process)):
        if process[i] == '(':
            if process[i+1] == '(':  # 바로 ')'가 나오면 레이저
                pipe += 1
                cnt += 1  # 파이프 생성 시 조각 수 +1
        elif process[i] == ')':  # 인덱스 에러를 방지하고자 ' '을 하나 넣었기 때문에 elif처리
            if process[i-1] == '(':  # ')'는 단독으로 올 수 없다. 바로 이전이 '('라면 레이저
                cnt += pipe  # 레이저 절단 시 파이프 개수만큼 조각 수 생김
            else:  # 파이프 제거
                pipe -= 1

    print('#{} {}'.format(test_case, cnt))