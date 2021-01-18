class Solution:
    def fib(self, N: int) -> int:
        # recursion
        # T(n) = O(2**N)
        # if N==0:
        #     return 0
        # if N==1 or N==2:
        #     return 1
        # return self.fib(N-1) + self.fib(N-2)

        # Using Golden Ratio
        #         golden_ratio = (1 + 5 ** 0.5) / 2
        #         return int((golden_ratio ** N + 1) / 5 ** 0.5)

        # DP
        if N == 0:
            return 0
        result = [0] * (N + 1)
        result[1] = 1
        if N > 0 and result[N] != 0:
            return result[N]
        else:
            for res_index in range(2, N + 1):
                result[res_index] = result[res_index - 1] + result[res_index - 2]

        return result[N]


if __name__ == '__main__':
    N = 6
    sol = Solution()
    print(sol.fib(N))
