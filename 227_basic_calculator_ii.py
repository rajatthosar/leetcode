import math


class Solution:
    def calculate(self, s: str) -> int:
        '''
        3, 2, 4
        '''

        expression = s.strip()
        digit_set = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}
        op_set = {'+', '-', '*', '/'}
        stack = []

        for char in expression:
            if char in digit_set:
                if stack and stack[-1] == '*':
                    stack.pop()
                    stack.append(stack.pop() * int(char))
                elif stack and stack[-1] == '/':
                    stack.pop()
                    stack.append(stack.pop() // int(char))
                else:
                    stack.append(int(char))
            elif char in op_set:
                stack.append(char)
        while len(stack) > 1:
            operand = stack.pop()
            if stack[-1] in ['+','-']:
                operation = stack.pop()
                stack[-1] = stack[-1] + operand \
                if operation == '+' else stack[-1] - operand
            else:
                stack[-1] = stack[-1] * (10 ** (int(math.log10(operand)) + 1)) + operand
        return stack[0]


if __name__ == '__main__':
    sol = Solution()
    print(sol.calculate("1337"))
