N = int(input())
paper_numbers = list(map(int, (input().split())))
result = [1]
num = paper_numbers[0]  # 첫번째로 확인한 종이 번호
paper_numbers[0] = 0  # 무조건 1번 풍선부터 터뜨림, value  = 0 => 터진 풍선
idx = 0

while paper_numbers.count(0) != N:
    if num > 0:  # 확인한 숫자 양수
        cnt = 0
        while cnt != num:
            idx += 1

            if idx == N:  # 오른쪽 끝 범위 over
                idx = 0  # 0번째 index로
            if paper_numbers[idx] != 0:
                cnt += 1

    else:
        cnt = 0
        while cnt != abs(num):
            idx -= 1

            if idx == -1:  # 왼쪽 끝 범위 over
                idx = N - 1  # -1번째 index로
            if paper_numbers[idx] != 0:
                cnt += 1

    result.append(idx + 1)  # 풍선 번호는 1부터 시작
    num = paper_numbers[idx]  # 터뜨린 풍선 종이 번호 갱신
    paper_numbers[idx] = 0  # 터뜨림

# 출력 맞춰주기
for i in result:
    print(i, end=" ")


###################################################################################
# 처음 풀이(더티 코드)
'''
N = int(input())
circular_que = list(range(1, N + 1))
paper_number = list(map(int, (input().split())))
result = [1]
circular_que[0] = 'x'  # 무조건 1번 풍선부터 터뜨림
list_cnt, cnt, list_idx, idx = 0, 0, 0, 0

if N == 1:
    pass
else:
    while list_cnt < len(paper_number) - 1:
        # 풍선은 원형 큐
        if (paper_number[list_idx] > 0):
            while cnt < paper_number[list_idx]:
                idx += 1
                if idx == N:
                    idx = 0

                while circular_que[idx] == 'x':
                    idx += 1
                    if idx == N:
                        idx = 0

                cnt += 1

            result.append(circular_que[idx])
            circular_que[idx] = 'x'
            list_idx = idx
            cnt = 0

        else:
            while cnt < -paper_number[list_idx]:
                idx -= 1

                if idx == -1:
                    idx = N - 1

                while circular_que[idx] == 'x':
                    idx -= 1
                    if idx == -1:
                        idx = N - 1

                cnt += 1

            result.append(circular_que[idx])
            circular_que[idx] = 'x'
            list_idx = idx
            cnt = 0

        list_cnt += 1

for i in result:
    print(i, end=" ")

'''
