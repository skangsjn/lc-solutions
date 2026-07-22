from collections import deque
class MovingAverage:

    def __init__(self, size: int):
        self.queue = deque()
        self.size = size
        # elements seen so far
        self.window_sum = 0
        self.count = 0

    def next(self, val: int) -> float:
        self.queue.append(val)
        self.count += 1

        # always popleft after we've seen the first {size} elements
        tail = self.queue.popleft() if self.count > self.size else 0
        self.window_sum = self.window_sum - tail + val

        return self.window_sum / min(self.size, self.count)


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)