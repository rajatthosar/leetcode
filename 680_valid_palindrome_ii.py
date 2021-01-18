class Solution:
    def validPalindrome(self, s: str) -> bool:
        if not s or len(s) == 1:
            return True

        init_ptr = 0
        tail_ptr = len(s) - 1

        infractions = 0
        dyn_str = list(s)
        while init_ptr < tail_ptr:
            char1 = s[init_ptr]
            char2 = s[tail_ptr]

            if s[init_ptr] == s[tail_ptr]:
                dyn_str[init_ptr] = ''
                dyn_str[tail_ptr] = ''
                init_ptr += 1
                tail_ptr -= 1
            elif infractions == 0:
                infractions += 1
                if s[init_ptr] == s[tail_ptr - 1]:
                    tail_ptr -= 1
                elif s[init_ptr + 1] == s[tail_ptr]:
                    init_ptr += 1
                else:
                    return False
            elif infractions > 0:
                return False
        return True


if __name__ == '__main__':
    sol = Solution()
    print(sol.validPalindrome("ebcbbececabbacecbbcbe"))
