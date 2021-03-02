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
class Stack:
    def __init__(self, n):
        self.top = -1
        self.stack = [0]*n

    def push(self, data):
        if self.top == len(self.stack) - 1:
            return None
        self.top += 1
        self.stack[self.top] = data
        print(self.stack)

    def pop(self):
        if self.top == 0:
            return None
        self.top -= 1
        p = self.stack[self.top+1]
        self.stack[self.top+1] = 0
        print(self.stack)
        return p




my_stack = Stack(5)
my_stack.push(1)
my_stack.push(2)
my_stack.push(3)
print(my_stack.top)
print(my_stack.pop())
print(my_stack.pop())