# 정렬되지 않은 경우 탐색
arr = [4, 9, 11, 23, 19, 7]

key = 2  # key = 9인 경우 1번 index에 존재

for i in range(len(arr)):
    if key == arr[i]:
        print(i, '에 위치하고 있음')
        break
else:  # 끝까지 탐색했으나 못 찾음
    print('못찾음')

# 정렬되어 있는 경우
arr2 = [4, 7, 9, 11, 19, 23]
key2 = 10

for i in range(len(arr)):
    if key2 == arr2[i]:
        print(i, '에 위치하고 있음')
        break
    elif key < arr2[i]:  # 이 뒤로는 key보다 큰 값 밖에 없기때문에 더이상 탐색 의미없음음
        print(i, '번째까지만 탐색해봄')
        break

else:  # 끝까지 탐색했으나 못 찾음
    print('못찾음')


