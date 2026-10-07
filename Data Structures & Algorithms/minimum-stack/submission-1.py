class MinStack:

    def __init__(self):
        self.stack = []
        self.minElem = []
        self.minElem.append(2147483647)

    def push(self, val: int) -> None:
        if val <= self.minElem[-1]:
            self.minElem.append(val)
        self.stack.append(val)
        
    def pop(self) -> None:
        e = self.stack.pop()
        if e == self.minElem[-1]:
            self.minElem.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return (self.minElem[-1] if self.minElem else 0)

        
