from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if not tokens:
            return 0

        stack = []
        ops = {
            '+': lambda param1, param2: param1 + param2,
            '-': lambda param1, param2: param1 - param2,
            '*': lambda param1, param2: param1 * param2,
            '/': lambda param1, param2: int(param1 / param2)
        }

        for token in tokens:
            if token in ops:
                operand_2 = stack.pop()
                operand_1 = stack.pop()
                operation = ops[token]

                stack.append(operation(operand_1, operand_2))
            else:
                stack.append(int(token))

        return stack[-1]


if __name__ == '__main__':
    sol = Solution()
    print(sol.evalRPN(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]))
