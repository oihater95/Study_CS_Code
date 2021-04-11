class Stack:  # LIFO
    # 리스트를 이용하여 스택 생성
    def __init__(self):
        self.top = []

    # 스택 초기화
    def clear(self):
        self.top = []

    # 삽입
    def push(self, item):
        self.top.append(item)

    # 삭제
    def pop(self):
        # if Stack is not empty
        if self.size() > 0:
            # pop and return
            return self.top.pop(-1)
        else:
            print("스택이 비어있습니다")

    # 스택에서 top의 값을 읽어온다
    def peek(self):
        if self.size() > 0:
            return self.top[-1]
        else:
            print("스택이 비어있습니다")

    # 스택이 비어있는지 확인
    def isEmpty(self):
        if len(self.top) == 0:
            print('Empty')
        else:
            print('Not Empty')

    # 스택 크기 반환
    def size(self):
        return len(self.top)

stk = Stack()
stk.push(1)
stk.push(2)
stk.push(3)
print('stack: ', stk.top)
print('top: ', stk.peek())
stk.isEmpty()
print('size: ', stk.size())
print(stk.pop())
print('stack: ', stk.top)
stk.clear()
stk.isEmpty()
print(stk.pop())
print('stack: ', stk.top)
print('top: ', stk.peek())
print('size: ', stk.size())