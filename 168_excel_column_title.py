class Solution:
    def convertToTitle(self, n: int) -> str:
        if not n:
            return ''

        title = ''

        while n > 0:
            n -= 1
            title += chr(ord('A') + n % 26)
            n //= 26

        return title[::-1]


if __name__ == '__main__':
    sol = Solution()
    print(sol.convertToTitle(27))
