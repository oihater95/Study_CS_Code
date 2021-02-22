# 리스트의 경우(크기 지정 x)
def push(item):  # 삽입
    s.append(item)


def pop():
    if len(s) == 0:  # 공백검사, underflow
        return
    else:
        return s.pop()  # s.pop(-1), pop의 경우 default가 맨 마지막 값

s = []
#######################################################################
# 배열의 경우 (크기 지정 o)
def top():
    if len(arr):
        return arr[len(arr)-1]
    else:  # arr 비어있을 때
        return -1


def push_arr(item):



arr = []