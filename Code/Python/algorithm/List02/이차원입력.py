arr = [[1, 2, 3, 4], [1, 2, 3]]

for i in arr:
    print(i)

'''
3 4
1 2 3 4
5 6 7 8
9 1 2 3
'''

N, M = map(int, input().split())

arr = []

for i in range(N):
    arr.append(list(map(int, input().split())))

for i in arr:
    print(i)

######################################################
arr2 = [list(map(int, input().split())) for _ in range(N)]

for i in arr2:
    print(i)