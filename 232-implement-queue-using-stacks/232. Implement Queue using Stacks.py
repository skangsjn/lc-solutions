class MyQueue:

    def __init__(self):
        self.queue = []
        self.holder = []
        self.size = 0

    def push(self, x: int) -> None:
        self.queue.append(x)
        self.size += 1
        
    def pop(self) -> int:
        while self.size > 1:
            self.holder.append(self.queue.pop())
            self.size -= 1

        removed = self.queue.pop()
        self.size -= 1
        
        while self.holder:
            self.queue.append(self.holder.pop())
            self.size += 1
        
        return removed

    def peek(self) -> int:
        while self.size > 1:
            self.holder.append(self.queue.pop())
            self.size -= 1
        front = self.queue[-1]
        
        while self.holder:
            self.queue.append(self.holder.pop())
            self.size += 1
        
        return front

    def empty(self) -> bool:
        return self.size == 0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()