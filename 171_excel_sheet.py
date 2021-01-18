class Solution:
    def titleToNumber(self, s: str) -> int:
        if not s:
            return 0

        exponent = 1
        val = (ord(s[-1]) - ord('A')) + 1

        for char_idx in range(len(s) - 2, -1, -1):
            val += ((ord(s[char_idx]) - ord('A') + 1) * 26 ** exponent)
            exponent += 1

        return val


if __name__ == '__main__':
    sol = Solution()
    print(sol.titleToNumber("AAZ"))
