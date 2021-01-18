class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min = float('inf')

    def push(self, x: int) -> None:
        self.min = min(x, self.min)
        self.stack.append([x, self.min])

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]


if __name__ == '__main__':
    minstack = MinStack()
    minstack.push(-2)
    minstack.push(0)
    minstack.push(-3)
    print(minstack.top())
    minstack.pop()
    print(minstack.getMin())
