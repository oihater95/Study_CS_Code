# 선형 큐
class queue:
    def __init__(self, n):
        self.front = -1
        self.rear = -1
        self.queue = [0] * n

    def enQueue(self, item):
        if self.isFull(): print('Queue_Full')
        else:
            self.rear += 1
            self.queue[self.rear] = item
            print(self.queue)

    def deQueue(self):
        if self.isEmpty(): print('Queue_Empty')
        else:
            self.front += 1
            elem = self.queue[self.front]
            self.queue[self.front] = 0
            print(self.queue)
            return elem

    def isEmpty(self):
        if self.front == self.rear:
            return True
        else:
            return False

    def isFull(self):
        if self.rear == len(self.queue) - 1:
            return True
        else:
            return False

    def Qpeek(self):
        if self.isEmpty(): print('Queue_Empty')
        else:
            return self.queue[self.front+1]

my_queue = Queue(3)
my_queue.enQueue(1)
my_queue.enQueue(2)
my_queue.enQueue(3)
print('front is ',my_queue.Qpeek())
print('Full? ', my_queue.isFull())
my_queue.deQueue()
my_queue.deQueue()
my_queue.deQueue()
print('Empty? ', my_queue.isEmpty())
# 앞 공간 있지만 Full로 인식 => 해결하려면 큐를 앞으로 당겨와야함(비효율적)
my_queue.enQueue(1)
my_queue.enQueue(2)

print()
# 원형큐
class Circularqueue:
    def __init__(self, n):
        self.front = 0
        self.rear = 0
        self.queue = [0] * n

    def enQueue(self, item):
        if self.isFull(): print('Queue_Full')
        else:
            self.rear = (self.rear + 1) % len(self.queue)
            self.queue[self.rear] = item
            print(self.queue)

    def deQueue(self):
        if self.isEmpty(): print('Queue_Empty')
        else:
            self.front = (self.front + 1) % len(self.queue)
            elem = self.queue[self.front]
            self.queue[self.front] = 0
            print(self.queue)
            return elem

    def isEmpty(self):
        if self.front == self.rear:
            return True
        else:
            return False

    def isFull(self):
        if (self.rear + 1) % len(self.queue) == self.front:
            return True
        else:
            return False

    def Qpeek(self):
        if self.isEmpty(): print('Queue_Empty')
        else:
            return self.queue[self.front+1]

my_queue = CircularQueue(3)
my_queue.enQueue(1)
my_queue.enQueue(2)
my_queue.enQueue(3)
print('front is ',my_queue.Qpeek())
print('Full? ', my_queue.isFull())
my_queue.deQueue()
my_queue.deQueue()
my_queue.deQueue()
print('Empty? ', my_queue.isEmpty())
# 원형 큐는 index가 범위 넘어가면 다시 처음으로 돌아옴(선형 큐와의 차이점)
my_queue.enQueue(1)
my_queue.enQueue(2)