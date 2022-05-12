class MinStack:

    def __init__(self):
        self.stack = []
        self.minVal = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)
    
        minVal = min(val, self.minVal[-1] if self.minVal else val)
        self.minVal.append(minVal)
    
    def pop(self) -> None:
        self.stack.pop()
        self.minVal.pop()
        

    def top(self) -> int:
        return self.stack[-1] if self.stack else None
        

    def getMin(self) -> int:
        return self.minVal[-1] if self.minVal else None
