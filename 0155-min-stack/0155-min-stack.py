class MinStack:

    def __init__(self):
        self.stack=[]
        self.minst=[]

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.minst or self.minst[-1]>=val:
            self.minst.append(val)
        

    def pop(self) -> None:
        x=self.stack.pop()
        if x==self.minst[-1]:
            self.minst.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minst[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()