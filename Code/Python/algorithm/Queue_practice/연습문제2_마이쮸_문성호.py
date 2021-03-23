def MyChew(n):
    queue = []  # 대기열
    distribute = dict()  # 1인당 나눠주는 마이쮸 딕셔너리 key = 사람번호, value = 해당 번호의 사람이 받을 마이쮸 수
    new_person = 1  # 새로 들어오는 사람

    while n > 0:
        queue.append(new_person)  # 새로 들어오는 사람 대기열에 추가

        if len(distribute) < new_person:  # 새로 들어 온 사람 딕셔너리에 추가
            distribute[new_person] = 1

        print()
        print('정보를 출력하려면 Enter입력')
        enter = input()
        if enter == '':
            print('현재 큐에 있는 사람: {} {}명'.format(queue, len(queue)))
            print('현재 1인당 나눠주는 마이쮸 수 = {}'.format(distribute))
            print('현재까지 나눠준 마이쮸 수:', mychews - n)

        person = queue.pop(0)  # 마이쮸 받고 대기열에 나온 사람
        n -= distribute[person]  # 남은 마이쮸 수 갱신
        queue.append(person)  # 마이쮸 받고 나온 사람 다시 대기열에 추가
        distribute[person] += 1  # 해당 번호의 사람이 받을 마이쮸 수 +1
        new_person += 1  # 새로 들어오는 사람의 번호 갱신

    print()
    print('마지막 마이쮸의 주인공: {}'.format(person))


print('초기 마이쮸 개수를 입력하세요')
mychews = int(input())
MyChew(mychews)