# 메모리 초과
N = int(input())
moo = 'moo'
cnt = 3

while N > len(moo):
    new_moo = moo + 'm' + ('o'*cnt) + moo
    cnt += 1
    moo = new_moo

print(moo[N-1])

#########################################
# 현재 문자열 = 이전 문자열 + 추가되는 문자열 + 이전 문자열
N = int(input())
present = 3  # 현재 문자열 길이, 처음 시작 moo
addition = 4  # 추가되는 문자열, 처음 시작 mooo

while N > present:
    present = present * 2 + addition
    addition += 1

addition -= 1
while True:
    previous = (present - addition) / 2  # 이전 문자열

    if N <= previous:  # N이 이전 문자열 길이보다 작거나 같을 때
        present = previous
        addition -= 1

    elif previous < N < previous + addition:
        N -= previous
        break

    else:  # N > previous + addition
        N -= previous + addition
        addition -= 1
        present = previous

if N == 1:
    print('m')
else:
    print('o')
