class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)

    def pop(self) -> None:
        val = self.stack.pop()

    def top(self) -> int:
        return self.stack[len(self.stack) -1]

    def getMin(self) -> int:
        min = self.stack[0]
        for s in self.stack: 
            if s < min: 
                min = s
        return min