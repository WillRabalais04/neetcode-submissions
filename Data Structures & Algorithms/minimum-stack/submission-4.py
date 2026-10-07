class MinStack:

    def __init__(self):
        self.stack = []
        self.m = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.m == [] or val <= self.m[-1]:
            self.m.append(val)

    def pop(self) -> None:
        if self.stack.pop() == self.m[-1]:
            self.m.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.m[-1]

        
