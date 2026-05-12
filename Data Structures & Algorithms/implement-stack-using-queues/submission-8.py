class MyStack:
    def __init__(self):
        self.stack = []
        self.isEmpty = True
        self.size = 0

    def push(self, x: int) -> None:
        self.stack.append(x)
        self.isEmpty = False
        self.size += 1

    def pop(self) -> int:
        self.size -= 1
        if self.size <= 0:
            self.isEmpty = True
        
        return self.stack.pop(self.size)

    def top(self) -> int:
        return self.stack[self.size - 1]

    def empty(self) -> bool:
        return self.isEmpty


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
