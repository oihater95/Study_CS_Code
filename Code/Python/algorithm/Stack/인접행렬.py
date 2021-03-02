'''
7 8  정점의 수, 간선의 수
1 2  간선의 수만큼 반복 되면서 두개의 정점 주어짐
1 3  정점의 시작 번호가 1인지 0인지
2 4
2 5
4 6
5 6
6 7
3 7
'''

V, E = map(int, input().split())
# V*V 크기의 0으로 초기화 된 2차원 리스트
adj_arr = [[0] * V for _ in range(V)]

for i in range(E):
    A, B = map(int, input().split())
    # 무향
    adj_arr[A-1][B-1] = 1
    adj_arr[B-1][A-1] = 1  # 유향이면 생략

for i in adj_arr:
    print(*i)