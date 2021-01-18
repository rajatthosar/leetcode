class Solution:
    def getSum(self, a: int, b: int) -> int:
        if a < 0:
            a = (~a) + 1
        if b < 0:
            b = (~b) + 1
        return a | b


if __name__ == '__main__':
    sol = Solution()
    print(sol.getSum(1, 2))
    print(sol.getSum(-2, 3))
    print(sol.getSum(-2, -3))
    print(sol.getSum(2, -1))

