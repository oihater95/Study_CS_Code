testCase = int(input())
for tc in range(testCase):
    docCount, targetIdx = map(int, input().split())  # 문서 수, 찾을 문서 위치
    priority = list(map(int, input().split()))  # 우선 순위 입력
    priorityQueue = []  # [우선 순위, 시작 인덱스] 큐
    result = 0

    for i in range(docCount):  # [우선 순위, 시작 인덱스] 리스트 채우기
        priorityQueue.append([priority[i], i])

    while True:
		# 큐의 첫번째가 우선 순위 가장 높은지 check
        if priorityQueue[0][0] == max(priorityQueue)[0]: 
            result += 1
			# 찾을 문서 위치 맞는지 확인, 맞으면 break
            if priorityQueue[0][1] == targetIdx:
                break
			# 찾을 문서 위치가 아니라면 인쇄
            priorityQueue.pop(0)

        else:
			# 가장 높은 우선 순위가 아니라면 큐 맨 뒷 순서로
            temp = priorityQueue.pop(0)
            priorityQueue.append(temp)

    print(result)