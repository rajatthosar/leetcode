class Solution:
    def reverseWords(self, s: str) -> str:
        init_ptr = 0
        tail_ptr = 0
        s = list(s)
        s.append(' ')
        while tail_ptr < len(s):
            if s[tail_ptr] == ' ':
                marker = tail_ptr
                while init_ptr < tail_ptr - 1:
                    s[init_ptr], s[tail_ptr - 1] = s[tail_ptr - 1], s[init_ptr]
                    init_ptr += 1
                    tail_ptr -= 1
                init_ptr, tail_ptr = marker + 1, marker
            tail_ptr += 1
        return ''.join(s[:len(s) - 1])


if __name__ == '__main__':
    sol = Solution()
    print(sol.reverseWords("Let's take LeetCode contest"))
