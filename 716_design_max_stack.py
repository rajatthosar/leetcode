class MaxStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []

    def push(self, x: int) -> None:
        max_val = max(x, self.stack[-1][1] if self.stack else x)
        self.stack.append((x, max_val))

    def pop(self) -> int:
        return self.stack.pop()[0]

    def top(self) -> int:
        return self.stack[-1][0]

    def peekMax(self) -> int:
        return self.stack[-1][1]

    def popMax(self) -> int:
        max_val = self.stack[-1][1]
        temp_stack = []
        is_top_removed = False
        while self.stack:
            if self.stack[-1][0] == max_val and not is_top_removed:
                self.stack.pop()
                is_top_removed = True
            else:
                temp_stack.append(self.stack.pop()[0])
        for element in temp_stack[::-1]:
            self.push(element)
        return max_val


# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()
if __name__ == '__main__':
    stack = MaxStack()
    stack.push(5)
    stack.push(1)
    stack.push(5)
    print(stack.top())
    print(stack.popMax())
    print(stack.top())
    print(stack.peekMax())
    print(stack.pop())
    print(stack.top())
