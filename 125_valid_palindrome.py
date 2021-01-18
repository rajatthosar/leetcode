class Solution:
    def isPalindrome(self, s: str) -> bool:
        if not s:
            return False
        s = s.lower()
        s = list("".join(s.split(' ')))

        start_ptr = 0
        end_ptr = len(s) - 1

        while start_ptr < end_ptr:
            if s[start_ptr].isalnum() and s[end_ptr].isalnum():
                if s[start_ptr] != s[end_ptr]:
                    return False
                else:
                    start_ptr += 1
                    end_ptr -= 1
            else:
                if not s[start_ptr].isalnum():
                    start_ptr += 1
                if not s[end_ptr].isalnum():
                    end_ptr -= 1

        return True


if __name__ == '__main__':
    s = "A man, a plan, a canal: Panama"
    sol = Solution()
    print(sol.isPalindrome(s))