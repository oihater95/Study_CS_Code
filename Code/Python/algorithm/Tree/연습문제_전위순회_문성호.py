'''
13
1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13
'''
def preorder(n):
    if n > 0:  # 0이면 연결X
        print(n, end=' ')
        preorder(left[n])
        preorder(right[n])


def inorder(n):
    if n > 0:  # 0이면 연결X
        inorder(left[n])
        print(n, end=' ')
        inorder(right[n])


def postorder(n):
    if n > 0:  # 0이면 연결X
        postorder(left[n])
        postorder(right[n])
        print(n, end=' ')


V = int(input())  # 정점
E = V - 1  # 간선
tree = list(map(int, input().split()))  # 연결 상태

left = [0] * (V+1)  # 왼쪽 자식 번호, 인덱스 = 부모
right = [0] * (V+1)  # 오른쪽 자식 번호, 인덱스 = 부모
par = [0] * (V+1)  # 부모 번호, 인덱스 = 자식

for i in range(E):
    p, c = tree[2*i], tree[2*i + 1]
    if left[p] == 0:
        left[p] = c
    else:
        right[p] = c

    par[c] = p

# 루트 찾기
root = 0
for i in range(1, V+1):
    if par[i] == 0:
        root = i
        break

print('preorder: ', end='')
preorder(root)
print()
print('inorder: ', end='')
inorder(root)
print()
print('postorder: ', end='')
postorder(root)