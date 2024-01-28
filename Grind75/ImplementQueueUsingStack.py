class MyQueue:

    def __init__(self):
        self.enqueue_list = []
        self.dequeue_list = []

    def push(self, x: int) -> None: # Enqueue
        self.enqueue_list.append(x)

    def pop(self) -> int: # Dequeue
        if len(self.dequeue_list) == 0:
            if len(self.enqueue_list) == 0:
                return None
            while self.dequeue_list:
                self.dequeue_list.append(self.enqueue_list.pop())
        return self.dequeue_list.pop()

    def peek(self) -> int:
        if len(self.dequeue_list) == 0:
            if len(self.enqueue_list) == 0:
                return None
            while self.dequeue_list:
                self.dequeue_list.append(self.enqueue_list.pop())
        return self.dequeue_list[-1]

    def empty(self) -> bool:
        if len(self.enqueue_list) + len(self.dequeue_list) == 0:
            return True
        else:
            return False

# Your MyQueue object will be instantiated and called as such:
obj = MyQueue()
obj.push(1)
obj.push(2)
obj.push(3)
param_2 = obj.pop()
param_3 = obj.peek()
param_4 = obj.empty()