# 델타, 이웃한 값과의 차 절대값
def absol(num):
    if num < 0:
        return -num
    else:
        return num


arr = []

# 25개의 수 초기화
for i in range(5):
    temp = []
    for j in range(5):
        temp.append(5 * i + j + 1)
    arr.append(temp)

dr = [0, 0, -1, 1]  # 좌우
dc = [1, -1, 0, 0]  # 상하
result = 0
for i in range(5):
    for j in range(5):
        for k in range(4):
            nr = i + dr[k]
            nc = j + dc[k]
            if nr < 0 or nc < 0 or nr >= len(arr) or nc >= len(arr[i]): continue
            result += absol(arr[nr][nc]-arr[i][j])

print(result)