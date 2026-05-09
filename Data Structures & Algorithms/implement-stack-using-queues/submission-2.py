class MyStack:

    def __init__(self):
        self.mainQueue = []
        self.sideQueue = []
        

    def push(self, x: int) -> None:
        self.mainQueue.append(x)

    def pop(self) -> int:
        while len(self.mainQueue) > 1:
            self.sideQueue.append(self.mainQueue.pop(0))

        result = self.mainQueue.pop(0)
        self.mainQueue = self.sideQueue.copy()
        self.sideQueue.clear()
        return result

    def top(self) -> int:
        while len(self.mainQueue) > 1:
            self.sideQueue.append(self.mainQueue.pop(0))

        result = self.mainQueue.pop(0)
        self.mainQueue = self.sideQueue.copy()
        self.mainQueue.append(result)
        self.sideQueue.clear()
        return result

    def empty(self) -> bool:
        return len(self.mainQueue) == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()