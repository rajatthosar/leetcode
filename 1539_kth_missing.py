from typing import List


class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        expected = 1
        value_set = set(arr)

        for _ in range(arr[-1]):
            if expected not in value_set:
                k -= 1
            if k == 0:
                return expected
            expected += 1
        return arr[-1] + k


if __name__ == '__main__':
    sol = Solution()
    print(sol.findKthPositive(arr=[2, 3, 4, 7, 11], k=5))
