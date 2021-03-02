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
adj_List = [[] for _ in range(V)]

for i in range(V):
    A, B = map(int, input().split())
    adj_List[A-1].append(B-1)
    adj_List[B-1].append(A-1)

for i in adj_List:
    print(*i)