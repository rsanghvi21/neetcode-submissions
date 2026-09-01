class MinStack:

    def __init__(self):
        self.stack = []
        self.mini = []
        
    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.mini:
            self.mini.append(val)
        else:
            self.mini.append(min(val, self.mini[-1]))
    
    def pop(self) -> None:
        if self.stack:
            self.stack.pop()
            self.mini.pop()

    def top(self) -> int:
        if self.stack: 
            return self.stack[-1]
    
    def getMin(self) -> int:
        if self.mini: 
            return self.mini[-1]
        
