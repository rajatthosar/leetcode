class Solution:
    def removeDuplicates(self, S: str) -> str:
        if not S:
            return ''
        stack = []

        for char in S:
            if stack and len(stack) > 1:
                if stack[-1] == stack[-2]:
                    stack.pop()
                    stack.pop()
            stack.append(char)
        if len(stack) > 1 and stack[-1] == stack[-2]:
            stack.pop()
            stack.pop()
        return ''.join(stack)


if __name__ == '__main__':
    sol = Solution()
    print(sol.removeDuplicates("aaaaaaaaa"))
