minimum, maximum = map(int, input().split())
check_nums = list(range(minimum, maximum+1))  # 확인할 수
cnt = 0
i = 2
while i**2 <= maximum:
    multi = minimum // i**2  # multi => 배수
    while multi * (i**2) <= maximum:  # 가장 작은 제곱수의 배수부터 시작
        if minimum <= multi * (i**2) <= maximum:
            check_nums[multi * (i**2) - minimum] = 0  # minimum을 빼서 인덱스를 맞춰준다, 나누어 떨어지는 것은 0으로 처리
        multi += 1  # 배수 증가
    i += 1  # 다음 제곱수

for num in check_nums:
    if num != 0:
        cnt +=1

print(cnt)
