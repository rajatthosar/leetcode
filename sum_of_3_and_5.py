class Solution:
    def sumOf3and5(self, n):
        addition = 0
        for number in range(1, n):
            if number % 3 == 0 or number % 5 == 0:
                addition += number

        return addition


if __name__ == '__main__':
    n = 1000
    sol = Solution()
    print(sol.sumOf3and5(n))
