class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        if not (S or T):
            return True
        if len(S) * len(T) == 0:
            return False
        if len(S) > len(T):
            S, T = T, S
        s_ptr = len(S) - 1
        t_ptr = len(T) - 1
        s_chars_to_ignore = 0
        t_chars_to_ignore = 0

        while s_ptr > -1 and t_ptr > -1:
            if S[s_ptr] == '#':
                s_chars_to_ignore += 1
            if T[t_ptr] == '#':
                t_chars_to_ignore += 1
            if S[s_ptr] != '#' and T[t_ptr] != '#':
                if S[s_ptr] != T[t_ptr]:
                    s_chars_to_ignore -= 1
                    t_chars_to_ignore -= 1
            if s_chars_to_ignore < 0 or t_chars_to_ignore < 0:
                return False
            s_ptr -= 1
            t_ptr -= 1
        return True


if __name__ == '__main__':
    sol = Solution()
    print(sol.backspaceCompare(S="abb#c", T="ac"))
