class Solution:
    def removeDuplicates(self, string: str) -> str:
        if not string:
            return ''
        stack = []
        for char in string:
            if not stack or stack[-1] != char:
                stack.append(char)
            elif stack[-1] == char:
                stack.pop()
        return ''.join(stack)


if __name__ == "__main__":
    sol = Solution()
    print(sol.removeDuplicates("ACCAABBC"))
