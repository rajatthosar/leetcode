class Solution:
    def decodeString(self, s: str) -> str:
        if not s:
            return ''

        stack = []
        multiplier_stack = []
        char_idx = 0
        while char_idx < len(s):
            temp_int = ''
            while s[char_idx].isnumeric():
                temp_int += s[char_idx]
                char_idx += 1
            if temp_int:
                multiplier_stack.append(int(temp_int))
                temp_int = ''
            if s[char_idx] == ']':
                temp_str = ''
                if stack:
                    ch = stack.pop()
                    while stack and ch != '[':
                        temp_str += ch
                        ch = stack.pop()
                mult = 1 if not multiplier_stack else multiplier_stack.pop()
                stack.append(temp_str[::-1] * mult)
            else:
                stack.append(s[char_idx])
            char_idx += 1
        return ''.join(stack[::])


if __name__ == '__main__':
    sol = Solution()
    print(sol.decodeString("3[a]2[bc]"))
