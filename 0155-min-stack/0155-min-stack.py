class MinStack:

    def __init__(self):
        self.stack = []
        self.pos = -1
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.pos += 1

    def pop(self) -> None:
        self.stack.pop(self.pos)
        self.pos -= 1
        

    def top(self) -> int:
        return self.stack[self.pos]
        

    def getMin(self) -> int:
        mini = self.stack[0]
        
        for number in self.stack:
            if number < mini:
                mini = number
        
        return mini


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()