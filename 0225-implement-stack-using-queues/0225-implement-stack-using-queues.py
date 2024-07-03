from collections import deque

class MyStack:

    def __init__(self):
        self.popQueue = deque()
        self.pushQueue = deque()

    def push(self, x: int) -> None:
        self.pushQueue.append(x)
        
        # 把老的放到后面新的在第一个
        while self.popQueue:
            self.pushQueue.append(self.popQueue.popleft())
        
        self.pushQueue, self.popQueue = self.popQueue, self.pushQueue

    def pop(self) -> int:
        return self.popQueue.popleft()
        
    def top(self) -> int:
        return self.popQueue[0]

    def empty(self) -> bool:
        return not self.popQueue


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()